
'''
1、元类的使用
'''

'''
不想任何人创建实例
'''

print("10"+"-"*60)
class NoInstance(type):
    def __call__(self,*args,**kwargs):
        raise TypeError("Cannot instantiate directly")

class Sapm_v5(metaclass= NoInstance):
    @staticmethod
    def grok(x):
        print('Spam.grok')

Sapm_v5.grok(42) #Cannot instantiate directly
#s = Sapm_v5()

'''
单例的实现
'''
class Singleton(type):
    def __init__(self,*args,**kwargs):
        self.__instance = None
        super().__init__(*args,**kwargs)
    
    def __call__(self,*args,**kwargs):
      if self.__instance is None:
        self.__instance = super().__call__(*args,**kwargs)
        return self.__instance
      else:
          return self.__instance

class Spam_v6(metaclass=Singleton):
    def __init__(self) -> None:
        print('Creating Spam')

print("11"+"-"*60)
a = Spam_v6()
b = Spam_v6()
c = Spam_v6()

print(a is b)
print(b is c)
print(a is c)


'''
缓存创建的实例
'''
print("12"+"-"*60)

import inspect
import logging
import weakref
class Cached(type):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self,*args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

class Spam_v6(metaclass= Cached):
    def __init__(self,name) -> None:
        print('Creating Spam({!r})'.format(name))
        self.name = name

a = Spam_v6('test')
b = Spam_v6('test_v1')
c = Spam_v6('test')

print(a is b)
print(a is c)


'''
python __new__ 、 __init__
new是对象实例化之前执行,init是实例化后初始化时候调用
'''
print("13"+"-"*60)
class MyClass_v2:
    def __new__(cls,*args,**kwargs):
        print("Creating instance using __new__")
        instance = super(MyClass_v2,cls).__new__(cls)
        return instance
    
    def __init__(self,value):
        print("Initializing instance using __init__")
        self.value = value
obj = MyClass_v2(20)


'''
获取类属性的定义顺序
__prepare__是一个特殊的方法,用于在定义类时指定以恶自定义的映射类型(通常是字典)以存储类属性和方法的名称和定义
必须返回一个映射类型的对象
'''
print("14"+"-"*60)
from collections import OrderedDict

class Typed:
    _expected_type = type(None)
    def __init__(self,name=None) -> None:
        self._name = name
    def __set__(self,instance,value):
        if not isinstance(value,self._expected_type):
            raise TypeError('Expected '+str(self._expected_type))
        instance.__dict__[self._name] = value

class Integer(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

#创建一个类、拒绝重复定义属性
class NoDupOrderedDict(OrderedDict):
    def __init__(self,clsname):
        self.clsname = clsname
        super().__init__()

    def __setitem__(self,name,value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name,self.clsname))
        super().__setitem__(name,value)



class OrderedMeta(type):
    def __new__(cls,clsname,bases,clsdict):
        d = dict(clsdict)
        order = []
        for name ,value in clsdict.items():
            if isinstance(value,Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls,clsname,bases,d)
    
    @classmethod
    def __prepare__(cls,clsname,bases):
        #使用一个有序的集合来存储类属性和方法的名称
        #return OrderedDict()
        #使用NoDupOrderedDict 继承了原始的字典,不允许key重复
        return NoDupOrderedDict(clsname)

class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self,name)) for name in self._order)

# Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()
    
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
s = Stock('GOOG',100,489.1)
print(s.name)
print(s.as_csv())

#测试重复定义
# class A(metaclass = OrderedMeta):
#     def spam(self):
#         pass
#     def spam(self):
#         pass

'''
定义一个能接受可选参数的元类
需要在定义时候__prepare__()、__new__()以及__init__()方法时使用keyword-only参数来指定他们
①-__prepare__() 方法创建类名称空间
②-__new__() 最终实例化得到对象
③-__init__() 实例化后的初始化
'''
class MyMeta(type):
    @classmethod
    def __prepare__(cls,name,bases,*,debug = False,synchronize=False):
        #custom processing
        return super().__prepare__(name,bases)
    
    #required
    def __new__(cls,name,bases,ns,*,debug=False,synchronize=False):
        #custom processing
        return super().__new__(cls,name,bases,ns)
    
    #Required
    def __init__(self,name,bases,ns,*,debug=False,synchronize=False):
        #custom processing
        return super().__init__(name,bases,ns)
    

'''
在*args 和 *kwargs 上强制规定一种参数签名
'''
from inspect import Signature,Parameter, signature
print("15"+"-"*60)


# make a signature for a func(x,y=42,*,z=None)
# 必传参数x 
params = [Parameter('x',Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y',Parameter.POSITIONAL_OR_KEYWORD,default=42),
          Parameter('z',Parameter.KEYWORD_ONLY,default=None)
          ]
sig = Signature(params)
print(sig)    #(x,y=42,*,z=None)

#通过签名对象将参数绑定到方法上

def func(*args,**kwargs):
    bound_values = sig.bind(*args,**kwargs)
    for name,value in  bound_values.arguments.items():
        print(name,value)

# func(1,2,z=3)
# func(1)
func(1,z=3)

#func(1,2,3,4,5,z=8)  #too many positional arguments

'''
更一般的签名方式
'''

print("16"+"-"*60)

def make_sig(*names):
    parms = [Parameter(name,Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class Structure_v2:
    #空的 不能使用 [] 去代替
    __signature__ =make_sig()
    
    def __init__(self,*args,**kwargs) :
        bound_values = self.__signature__.bind(*args,**kwargs)
        for name,value in bound_values.arguments.items():
            setattr(self,name,value)

class Stock(Structure_v2):
    __signature__ = make_sig('name','shares','price')

class Point(Structure_v2):
    __signature__ = make_sig('x','y')

print(inspect.signature(Structure_v2))
print(inspect.signature(Stock))
print(inspect.signature(Point))

s1 = Stock('ACME',100,490.1)
#s2 = Stock('ACME',100) # 必须要有三个参数 否则bind的时候就会报错
 

'''
自定义元类创建签名对象
'''
print("17"+"-"*60)
class StructureMeta(type):
    def __new__(cls,clsname,bases,clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields',[]))
        return super().__new__(cls,clsname,bases,clsdict)

class Structure_v3(metaclass = StructureMeta):
    _fields = []
    def __init__(self,*args,**kwargs):
        bound_values = self.__signature__.bind(*args,**kwargs)
        for name,value in bound_values.arguments.items():
            setattr(self,name,value)

class Stock_v2(Structure_v3):
    _fields = ['name','shares','price']
class Point_v2(Structure_v3):
    _fields = ['x','y']

s1_1 = Stock_v2('ACME',89,90)  #参数必须和签名的一致


'''
元类检查子类是否重新定义了方法（这个不太理解为啥做这么复杂）
'''
print("18"+"-"*60)
class MatchSignatureMeta(type):
    def __init__(self,clsname,bases,clsdict):
        super().__init__(clsname,bases,clsdict)
        sup = super(self,self)
        for name ,value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue

            # get the previous definition (if any) and compare the signatures
            prev_dfn = getattr(sup,name,None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',value.__qualname__,prev_sig,val_sig)

#定义一个根类
class Root(metaclass = MatchSignatureMeta):
    pass

class A(Root):
    def foo(self,x,y):
        pass
    def spam(self,x,*,z):
        pass

class B(A):
    def foo(self,a,b):
        pass

    def spam(self,x,z):
        pass

'''
通过编程的方式来定义类
代替通过exec(str)的方式来生成 这种方式更优雅
'''

print("19"+"-"*60)
def __init__(self,name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

cls_dict = {
    '__init__':__init__,
    'cost':cost
}

import types
#第四个参数是返回一个命名空间的函数  第二个可以是bases 基类  返回的是一个新的class
Stock = types.new_class('Stock',(),{},lambda ns:ns.update(cls_dict))
#每当定义一个类时，其__module__属性中包含的名称就是定义该类时所在的模块名
Stock.__module__ = __name__

s = Stock('ACME',50,91.1)
print(s.cost())


'''
使用元类达到namedtuple的同样功能
'''
print("20"+"-"*60)

import operator
import sys

def named_tuple(classname,fieldnames):
    #
    cls_dict = {name:property(operator.itemgetter(n)) for n,name in enumerate(fieldnames)}

    def __new__(cls,*args):
       if len(args) != len(fieldnames):
           raise TypeError('Expected {} arguments'.format(len(fieldnames)))
       return tuple.__new__(cls,args)
    
    cls_dict['__new__'] = __new__

    # make the class 注意是types  注意这里继承了tuple 这个class 重新定义了 __new__函数
    cls = types.new_class(classname,(tuple,),{},lambda ns : ns.update(cls_dict))
    #将模块的名称赋值给他
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls

Point_v3 = named_tuple('Point_v3',['x','y'])
print(Point_v3)
p = Point_v3(5,6)
print(len(p))
print(p.x)
print(p.y)