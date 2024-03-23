'''
类的一些使用
'''

'''
1、__repr__、__str__
    {0.x!r} 0表示第一个参数  !r 表示__repr__输出 而不是默认的str()方式输出
    __repr__一般用于在解释器中的一些输出
    __str__ 在print函数输出的时候调用
'''

print("1"+"-"*60)

class Pair:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __repr__(self):
        #self.x 使用 __repr__方式输出
        return 'Pair({0.x!r},{0.y!r})'.format(self)
    def __str__(self):
        return  '({0.x!s},{0.y!s})'.format(self)
    
p = Pair(3,4)

#print 最终调用的 __str__函数
print(p)



'''
2、自定义格式化输出
   自定义format输出
'''
_formats = {
    'ymd':'{d.year}-{d.month}-{d.day}',
    'mdy':'{d.month}/{d.day}/{d.year}',
    'dmy':'{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self,year,month,day) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __format__(self,code) -> str:
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

print("2"+"-"*60)
d = Date(2012,7,12)
print(format(d))
print(format(d,'mdy'))

#{:ymd} 指定了ymd的code ymd
s1 = 'The date is {:ymd}'.format(d)
print(s1)

s2 = 'The date is {:mdy}'.format(d)
print(s2)

'''
3、让类支持上下文的操作 with xxx as xxxx
   __enter__、__exit__方法
   一般c++会在对象的析构函数中做一些资源释放的操作

   当遇到with语句的时候,enter方法执行,返回值作为as的变量,当退出with的代码块中,exit函数执行做一些释放资源的清理工作
'''
from socket import socket,AF_INET,SOCK_STREAM
print("3"+"-"*60)

class LazyConnection:
    def __init__(self,address,family=AF_INET,type = SOCK_STREAM) -> None:
        self.address = address
        self.family = family
        self.type = type
        self.sock = None
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family,self.type)
        self.sock.connect(self.address)
        #注意return的返回值就是with  xxx  as xxx的变量的赋值
        return self.sock
    def __exit__(self,exec_ty,exc_val,tb):
        self.sock.close()
        self.sock = None
from functools import partial

conn = LazyConnection(('www.pthon.org',80))
#with 开启上下文
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host:www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv,8192),b''))
    print(resp)

'''
上面的v1版本是无法进行with嵌套的语句写法的
'''
class LazyConnection_v2:
    def __init__(self,address,family=AF_INET,type = SOCK_STREAM) -> None:
        self.address = address
        self.family = family
        self.type = type
        self.connection = []
    def __enter__(self):
        sock = socket(self.family,self.type)
        sock.connect(self.address)
        self.connection.append(sock)
        #注意return的返回值就是with  xxx  as xxx的变量的赋值
        return sock
    def __exit__(self,exec_ty,exc_val,tb):
        self.connection.pop().close()

conn1 = LazyConnection_v2(('www.pthon.org',80))
#嵌套的用法
with conn1 as s1:
   with conn1 as s2:
    pass


'''
4、__slots__是python中用于限制对象属性的特殊属性,通过slots你可以指定一个类中允许存在的属性
  从而限制实例化对象时可以拥有的属性数量,提高内存利用率
  代码中尽量不要使用__slots__属性,如果单纯地使用字段属性，并且对象数量比较大的时候,可以使用
'''

class Person:
    __slots__ = ('name','age')

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

print("4"+"-"*60)

p1 = Person('zyz',30)
#不可以添加额外的属性
#p1.sex = 'man'

'''
5、类中的没有下划线的属于public属性
   单划线的属于private属性
   双下划线的属于属性重整,属性重整的作用就是避免类在继承的环境下属性被覆盖
   重整的规则就是类名+属性名这种方式重新命名
'''

'''
5、创建可管理的属性
   property属性的应用,加了property相当于定义了一个属性 尽管是def 开头的方法 只能加在方法上
   当需要额外的处理任务的时候,可以使用property 一般情况下不需要使用
'''
class Student:
    def __init__(self,first_name) -> None:
        self.first_name = first_name

    @property
    def first_name(self):
        #实际数据保存到_first_name_1中
        return self._first_name_1
    
    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError('Expected a string')
        self._first_name_1 = value
    
    @first_name.deleter
    def first_name(self):
        raise AttributeError('cannot dele attribute')
    
print("5"+"-"*60)
stu1 = Student("zyz")
print(stu1.first_name)
#stu1.first_name = 43  exception expected a string
#del stu1.first_name  cannot  del attribute

#stu2 = Student(87)  构造函数也是要调用setter方法 87是int所以赋值不成功

'''
property被用来需要计算的属性类似于vue的计算属性
'''
import math
class Circle:
    def __init__(self,radius) -> None:
        self.radius = radius

    @property
    def area(self):
      return math.pi * self.radius ** 2
    
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
    
print("6"+"-"*60)

c = Circle(4)
print(c.area)   #没有 () 
print(c.perimeter) #没有 ()


'''
6、super的用法
'''
print("7"+"-"*60)

class Base:
    def __init__(self) -> None:
        print('Base.__init__')

class A(Base):
    def __init__(self) -> None:
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self) -> None:
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self) -> None:
       super().__init__()
       print('C.__init__')
c = C()

#通过mro表来确定方法的调用顺序 
#(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)
print(C.__mro__)


'''
7、创建一种新形式的类属性和实例属性
'''
print("8"+"-"*60)
class Integer:
    def __init__(self,name) -> None:
        self.name = name
    #get分为两种情况,第一种就是实例对象访问 instance 不为None 
    #如果是类访问 那么instance 就为None
    def __get__(self,instance,cls):
        print(cls)
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
        
    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError('Expected an int')
        print(type(instance))   # class Point
        instance.__dict__[self.name] = value

    def __delete__(self,instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

p = Point(3,4)

print(p.x) 
p.y = 5
print(p.y)


#对get访问参数的不同体现
print(p.x)      #Calls Point.x_get__(p,Point)
print(Point.x)  #Calls Point.x__get__(None,Point)


'''
8、让属性具有惰性求值能力
'''
print("9"+"-"*60)
class lazyproperty:
    def __init__(self,func) -> None:
        self.func = func
    
    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            #调用对应的函数或者方法
            value = self.func(instance)
            setattr(instance,self.func.__name__,value)
            return value

class Circle_v2:
    def __init__(self,radius) -> None:
        self.radius = radius
    
    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2
    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi* self.radius
c = Circle_v2(4)
print(vars(c))
print(c.area)
print(vars(c))
print(c.area)
#删除了area的属性,那么就会重新计算
del c.area
print(c.area)

#有个缺点就是可以改变area的值
c.area = 26
print(c.area)

print(c.perimeter)
print(c.perimeter)


'''
v2版本解决了 c.area的可变性问题?为啥 没看懂这块处理
'''

'''
9、简化数据结构的初始化过程
'''
print("10"+"-"*60)

class Structure:
    _fields = []
    def __init__(self,*args,**kwargs) -> None:
        if len(args)  > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        
        for name,value in zip(self._fields,args):
            setattr(self,name,value)
        
        #set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self,name,kwargs.pop(name))
        if kwargs:
            raise TypeError('Invalid argument(s):{}'.format(''.join(kwargs)))
'''
有个公共的基础类,下面三个类去继承它
'''
class Stock(Structure):
    _fields = ['name','shares','price']

class Point(Structure):
    _fields  = ['x','y']

class Circle(Structure):
    _fields = ['radius']
    def area(self):
        return math.pi * self.radius ** 2

s = Stock('ACME',50,91.1)
p = Point(2,3)
c = Circle(4.5)
s2 = Stock('ACER',89,90)


'''
10、定义一个接口或者抽象基类
'''
print("11"+"-"*60)

from abc import ABCMeta,abstractmethod

class Istream(metaclass = ABCMeta):
    @abstractmethod
    def read(self,maxbytes = -1):
        pass

    @abstractmethod
    def write(self,data):
        pass

'''
抽象基类允许其他类向其注册
'''
import io

#将内置的I/O classes 注册为我们的接口
Istream.register(io.IOBase)
f = open('foo.txt')
print(isinstance(f,Istream))


'''
11、实现一种数据模型或者类型系统
'''
print("12"+"-"*60)

#base class Use a decriptor to set a value
class Descriptor:
    def __init__(self,name=None,**opts) -> None:
        self.name = name
        for key,value in opts.items():
            setattr(self,key,value)
    def __set__(self,instance,value):
        instance.__dict__[self.name] = value

'''
下面的三个类可以作为构建一个数据模型或者类型系统的基础组件
'''
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self,instance,value):
        if not isinstance(value,self.expected_type):
            raise TypeError('expected '+str(self.expected_type))
        super().__set__(instance,value)

class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super().__set__(instance,value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts) -> None:
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name,**opts)
    
    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('size must be < '+str(self.size))
        super().__set__(instance,value)

class Integer_v2(Typed):
    expected_type = int

class UnsignedInteger(Integer_v2,Unsigned):
    pass

class Float(Typed):
    expected_type = float

#value > 0 并且是Float
class UnsignedFloat(Float,Unsigned):
    pass

class String(Typed):
    expected_type = str

#是string 并且是最大长度的限制
class SizedString(String,MaxSized):
    pass

class Stock_v2:
    #下面三个都是类的属性 构造函数进行再次赋值而已
    name = SizedString('name',size = 8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self,name,shares,price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

s = Stock_v2('ACME',50,91.1)
print(s.name)

s.shares = 78

print(s.shares)

#s.price = 'a lot'  
#s.name = 'AHSHSHHSHSHH'


'''
使用装饰器来达到类型的约束
'''
def check_attributes(**kwargs):
    def decorate(cls):
        #在类上设置一些属性 对象访问属性的时候就是访问对应的类属性
        for key ,value in kwargs.items():
            if isinstance(value,Descriptor):
                value.name = key
                setattr(cls,key,value)
            else:
                t = value(key)
                setattr(cls,key,t)
        return cls
    return decorate

@check_attributes(name=SizedString(size=8),shares=UnsignedInteger,price=UnsignedFloat)
class Stock_v3:
    def __init__(self,name,shares,price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

print("13"+"-"*60)

s = Stock_v3('ACME',52,91.4)


class checkedmeta(type):
    def __new__(cls,clsname,bases,methods):
        for key ,value in methods.items():
            if isinstance(value,Descriptor):
                value.name = key
        return type.__new__(cls,clsname,bases,methods)
        
class Stock_v4(metaclass = checkedmeta):
    name = SizedString(size = 8)
    shares = UnsignedInteger()
    price = UnsignedFloat()
    def __init__(self,name,shares,price) -> None:
        self.name = name 
        self.shares = shares
        self.price = price
           
s = Stock_v4('HTWE',52,91.4)


'''
总结一下:类型系统的真正的本质
        首先定义一些类型的class,class在set一些值的时候要做一些额外的检查 主要是isinstance
        setattr在class对应的属性上设置一些值,如果是对象直接访问对应的属性,那么就是访问class的属性
        例如:p3.age p4.age 一开始都是对应的Person_v3.age
        当重新赋值后,p3.age = 19 p4.age = 29 ,会在赋值的时候做一些检查(set)
        那么p3 和 p4对应的字段又有自己对应的属性
类和对象的关系这块
'''

class Person_v3:
    def __init__(self, name):
        self.name = name

setattr(Person_v3,'age',UnsignedInteger('age'))
p3 = Person_v3('zyz')
p4 = Person_v3('waq')
print(p3.age)
print(p4.age)

p3.age = 19   #修改p3的年龄
p4.age = 21   #修改p4的年龄

print(p3.age)
print(p4.age)
print(Person_v3.age)


'''
11、委托的属性访问
'''
print("14"+"-"*60)

#1-简单的委托访问  类似于静态的代理
class A:
    def spam(self,x):
        print('a SPAM')
        pass

    def foo(self):
        pass

class B:
    def __init__(self) -> None:
        self._a = A()
    
    def spam(self,x):
        return self._a.spam(x)
    
    def foo(self):
        return self._a.foo()
    
    def bar(self):
        pass

#2-使用getattr批量委托
    
class B_v1:
     def __init__(self) -> None:
        self._a = A()
     def bar(self):
        pass
     
     #expose all of the method defined on class A
     # getattr 用来查找所有属性  当代码中访问一个不存在的属性的时候,就会进入这个方法
     def __getattr__(self,name):
         return getattr(self._a,name)
b = B_v1()
b.bar()
b.spam(43)    #调用A.spam()方法 b没用spam方法 调用到A的spam方法
print(b.spam)

#3-代理
class Proxy:
    def __init__(self,obj) -> None:
        self._obj = obj

    def __getattr__(self,name):
        print('getattr:',name)
        return getattr(self._obj,name)
    
    def __setattr__(self, name, value) -> None:
        if name.startswith('_'):
            super().__setattr__(name,value)
        else:
            print('setattr:',name,value)
            setattr(self._obj,name,value)
    def __delattr__(self, name) -> None:
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:',name)
            delattr(self._obj,name)
class Spam:
    def __init__(self,x) -> None:
        self.x = x
    def bar(self,y):
        print("Spam.bar",self.x,y)
spam1 = Spam(43)
sp = Proxy(spam1)

print(sp.x)
sp.bar(42)
sp.x = 89
print(sp.x)


'''
12、在类中定义多个构造函数
'''

print("15"+"-"*60)
import time
class Date:
    def __init__(self,year,month,day) -> None:
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        print(cls)
        t = time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)
a = Date(2012,10,12)
b = Date.today()

class NewDate(Date):
    pass
c = NewDate.today()  # cls ----> NewDate


'''
13、不使用init方法构造对象
'''
print("16"+"-"*60)

d = Date.__new__(Date)

data = {'year':2012,'month':8,'day':18}
for key,val in data.items():
    setattr(d,key,val)
print(d.year)


'''
13、mixin的使用
    ①-命名的时候都是以mixin作为结尾
    ②-mixin 一般没有状态的 没有__init__ 没有属性 __slots__ = ()  创建一个空的元组对象
    ③-使用super()将下一个调用转移到 MRO 表的下一个类上 这个super() 也是必须的
'''
print("17"+"-"*60)

class LoggedMappingMixin:
    '''
    add logging to get/set/delete operation for debuging
    '''

    __slots__ = ()

    def __getitem__(self,key):
        print('Getting ' + str(key))
        return super().__getitem__(key)
    
    def __setitem__(self,key,value):
        print('Setting {} = {!r}'.format(key,value))
        return super().__setitem__(key,value)
    
    def __delitem__(self,key):
        print("Deleting " + str(key))
        return super().__delitem__(key)
    
class SetOnceMappingMixin:

    '''
    Only allow a key to be set once 
    '''

    __slots__ = ()

    def __setitem__(self,key,value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key,value)
    
class StringKeyMappingMixin:
    '''
    Restrict keys to strings only
    '''
    __slots__ = ()

    def __setitem__(self,key,value):
        if not isinstance(key,str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key,value)
    
'''
带日志的dict mixin的使用
混合了 dict和 LoggedMappingMixin
'''
class LoggedDict(LoggedMappingMixin,dict):
    pass

d = LoggedDict()
d['x'] = 23
print(d['x'])

del d['x']

from collections import defaultdict
class SetOnceDefaultDict(SetOnceMappingMixin,defaultdict):
    pass

d = SetOnceDefaultDict(list)
d['x'].append(2)
d['y'].append(3)
d['x'].append(10)
#d['x'] = 23  x already set

from collections import OrderedDict
class StringOrderedDict(StringKeyMappingMixin,SetOnceMappingMixin,OrderedDict):
    pass

d = StringOrderedDict()
d['x'] = 27
#d[42] = 10  # keys must be strings
#d['x'] = 45  # x already set

'''
使用装饰器同样能达到mixin的效果
'''
print("18"+"-"*60)
def LoggedMapping(cls):
    cls_getitem  = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self,key):
        print('Geting ' + str(key))
        return cls_getitem(self,key)
    
    def __setitem__(self,key,value):
         print('Setting {} = {!r}'.format(key,value))
         return cls_setitem(self,key,value)

    def __delitem__(self,key):
        print("Deleting " + str(key))
        return cls_delitem(self,key)
    
    #从dict继承下来 get、set、delete 替换为新的 
    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls

@LoggedMapping
class LoggedDict(dict):
    pass

d = LoggedDict()
d['x'] = 1
print(d['x'])
d['y'] = 3

del d['y']


'''
14、设计一个状态机  对象含有状态 只有对象在一个状态下才能有一些操作
'''
print("19"+"-"*60)
class Connection:
    def __init__(self) -> None:
        self.state = 'CLOSED'
    
    def read(self):
        if self.state != 'OPEN' :
            raise RuntimeError('conn not open')
        print('reading')

    def write(self,data):
        if self.state != 'OPEN':
            raise RuntimeError('conn not open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('conn already open')
        #打开一个连接 将状态设置为连接状态
        self.state = 'OPEN'
    
    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('conn already close')
        #打开一个连接 将状态设置为连接状态
        self.state = 'CLOSED'

class Connection_v2:
    def __init__(self) -> None:
        self.new_state(ClosedConnectionState)

    def new_state(self,newstate):
        self._state = newstate  #把class对象赋值给对应的state变量
    
    def read(self):
        return self._state.read(self)
    
    def write(self,data):
        return self._state.write(self,data)
    
    def open(self):
        return self._state.open(self)
    
    def close(self):
        return self._state.close(self)

#定义一个baseClass    
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()
    
    @staticmethod
    def write(conn, data):
        raise NotImplementedError()
 
    @staticmethod
    def open(conn):
        raise NotImplementedError()
 
    @staticmethod
    def close(conn):
        raise NotImplementedError()

#open状态的连接    
class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')
 
    @staticmethod
    def write(conn, data):
        print('writing')
 
    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')
 
    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)    
    
#关闭状态下
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')
 
    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')
 
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)
 
    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')
    
c = Connection_v2()
print(c._state)  #<class '__main__.ClosedConnectionState'>
#c.read()
c.open()
print(c._state)
c.read()
c.write(89)
c.close()
print(c._state)


'''
15、调用对象上的方法 方法名通过字符串给出
'''
print("20"+"-"*60)

class Point_v2:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return 'Point_v2({!r:},{!r:})'.format(self.x,self.y)
    
    def distance(self,x,y):
        return math.hypot(self.x-x,self.y - y)

p = Point_v2(4,3)
#得到一个可调用的对象
d = getattr(p,'distance')(0,0)
print(d)

#另一种方法
import operator
#接收一个参数
call_c = operator.methodcaller('distance',0,0)
print(call_c(p))

points = [Point_v2(1,2),
          Point_v2(3,0),
          Point_v2(10,-3),
          Point_v2(-5,-7),
          Point_v2(-1,8),
          Point_v2(3,2)]
points.sort(key=operator.methodcaller('distance',0,0))

print(points)


'''
16、访问者模式设计
'''

print("21"+"-"*60)

class Node:
    pass

class UnaryOperator(Node):
    def __init__(self,operand) -> None:
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self,left,right) -> None:
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass
class Sub(BinaryOperator):
    pass
class Mul(BinaryOperator):
    pass
class Div(BinaryOperator):
    pass
class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self,value) -> None:
       self.value = value

class NodeVisitor:
    def visit(self,node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self,methname,None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
    
    def generic_visit(self,node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
    
class Evaluator(NodeVisitor):
    def visit_Number(self,node):
        return node.value
    
    def visit_Add(self,node):
        return self.visit(node.left) + self.visit(node.right)
    
    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)
 
    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)
 
    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)
 
    def visit_Negate(self, node):
        return -node.operand

t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)

e = Evaluator()
print(e.visit(t4))

t5 = Negate(5)
print(e.visit(t5))

'''
17、让类支持比较操作 > < = >= <=  类中定义一些重载的函数
    通过加上total_ordering注解 类中只要定义eq(必须) lt gt其中任意即可
    自动补全 gt 等其他方法
'''
from functools import total_ordering

class Room:
    def __init__(self,name,length,width) -> None:
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self,name,style) -> None:
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)
    
    def add_room(self,room):
        self.rooms.append(room)
    
    def __str__(self):
        return '{}:{} square foot {}'.format(self.name,self.living_space_footage,self.style)
    
    def __eq__(self, other) -> bool:
        return self.living_space_footage == other.living_space_footage
    
    def __lt__(self,other) -> bool:
        return self.living_space_footage == other.living_space_footage
    

'''
18、类的缓存机制
'''
print("22"+"-"*60)

import logging
a = logging.getLogger('foo')
b = logging.getLogger('bar')
c = logging.getLogger('foo')

print(a is b)
print(a is c)

'''
19、类缓存的使用
    weakref 的使用
'''
print("23"+"-"*60)
import weakref
    
class CachedSpamManager:
    def __init__(self) -> None:
        self._cache = weakref.WeakValueDictionary()
    
    def get_spam(self,name):
        if name not in self._cache:
            s = Spam_v1(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
    def clear(self):
        self._cache.clear()

#这种方法有个缺陷就是放开了缺口new了

class Spam_v1:
    #类级别的变量
    cache_manager = CachedSpamManager()

    def __init__(self,name) -> None:
        self.name = name  
    
    #类中的变量 不可以直接引用 必须加上类.变量的形式
    @classmethod
    def get_spam_v1(cls,name):
        return Spam_v1.cache_manager.get_spam(name)

a = Spam_v1.get_spam_v1('foo')
b = Spam_v1.get_spam_v1('foo')
print(a is b)

'''
下面的一个版本就是不对外暴露init方法
'''
print("24"+"-"*60)

class Spam_v2:
    def __init__(self,*args,**kwargs) -> None:
        raise RuntimeError("cannot init directly")
    @classmethod
    def _new(cls,name):
        self = cls.__new__(cls)
        self.name = name
        return self


class CachedSpamManager_v2:
    def __init__(self) -> None:
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self,name):
        if name not in self._cache:
            s = Spam_v2._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
cache_manager = CachedSpamManager_v2()
a = cache_manager.get_spam('ss')
b = cache_manager.get_spam('ss')
print(a is b)