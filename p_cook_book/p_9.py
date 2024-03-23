'''
元编程技术
装饰器和元类
'''

'''
1、装饰器技术的使用
   内建的装饰器有staticmethod、classmethod、property
   @wrapper(func)可以用来保存函数的元数据  不加的话 函数的元数据编程被包装后的函数的元数据
'''
print("1"+"-"*60)

import time
import mysql.connector

from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        #获取当前时间戳 单位是秒 从1970年开始到现在的秒数
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1
print(countdown)
countdown(1000000)

'''
对装饰器进行解包装
__wrapped__属性来访问原始函数
'''

'''
定义一个可接受参数的装饰器
'''
print("2"+"-"*60)
from functools import wraps
import logging

def logged(level,name=None,message = None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        def wrapper(*args,**kwargs):
            print("wrapper exec")
            log.log(level,logmsg)
            return func(*args,**kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x,y):
    return x + y

@logged(logging.CRITICAL,'example')
def spam():
    print('spam!')

print(add)

'''
定义一个属性可由用户修改的装饰器
见9-1.py文件
'''

'''
9.6 节的内容好好区理解 装饰器的最佳实践
①装饰器的执行流程
②-定义一个能接收可选参数的装饰器
'''
from functools import partial

def logged_v2(func=None,*,level = logging.DEBUG,name=None,message = None):
    if func is None:
        #partial 返回一个可调用的对象  对logged_v2做参数绑定成为新的可调用对象
        return partial(logged_v2,level = level,name = name,message = message)
    #类似于三元表达式的作用
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    
    @wraps(func)
    def wrapper(*args,**kwargs):
        log.log(level,logmsg)
        return func(*args,**kwargs)
    return wrapper

@logged_v2
def add_v2(x,y):
    return x + y

#add = logged_v2(add)

@logged_v2(level=logging.CRITICAL,name='example')
def spam_v2():
    print('Spam!')
#spam_v2 = logged_v2(level=logging.CRITICAL,name='example')(spam_v2)

spam_v2()


from inspect import signature




'''
利用装饰器对函数参数做强制性检查
'''

def typeassert(*ty_args,**ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func
        sig = signature(func)
        #bind_partial提供了类型到参数名的绑定
        bound_types = sig.bind_partial(*ty_args,**ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args,**kwargs):
            bound_values = sig.bind(*args,**kwargs)

            for name,value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value,bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name,bound_types[name]))

            return func(*args,**kwargs)
        
        return wrapper  
    
    return decorate   

@typeassert(int,int)
def add(x,y):
    return x + y   

#print(add(2,3))
#add(2 , 'hello')

@typeassert(int,z=int)
def spam(x,y,z=42):
    print(x,y,z)

'''
inspect.signature() 函数 提取出参数签名的信息
'''
print("4"+"-"*60)

def test_inspect_sig(x,y,z=42):
    pass
sig = signature(spam)
print(sig)
print(sig.parameters)  #OrderedDict
print(sig.parameters['z'].default)

bound_types = sig.bind_partial(int,z = int)
print(bound_types)
print(bound_types.arguments)


'''
在类中定义装饰器
'''

class A:
    # decorator as an instance method
    def decorator1(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator 1')
            return func(*args,**kwargs)
        return wrapper
    
    @classmethod
    def decorator2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator 2')
            return func(*args,**kwargs)
        return wrapper

#如何使用类的装饰器
a = A()

#对象上的装饰器
@a.decorator1
def spam():
    pass

@A.decorator2
def grok():
    pass

spam()
grok()

'''
把装饰器定义成类
'''
print("5"+"-"*60)
import types

class Profield:
    def __init__(self,func) -> None:
        wraps(func)(self)
        self.ncalls = 0 
    
    def __call__(self, *args, **kwargs) :
        self.ncalls += 1
        return self.__wrapped__(*args,**kwargs)
    
    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            #见下面的示例分析
            return types.MethodType(self,instance)

@Profield
def add_v3(x,y):
    return x + y

class Spam_v3:
    @Profield
    def bar(self,x):
        print(self,x)

print(add_v3)
print(add_v3(3,4))

s = Spam_v3()
s.bar(1)
s.bar(2)
s.bar(3)
print(Spam_v3.bar.ncalls)


'''
使用 types.MethodType 可以将一个函数绑定到特定的实例上，从而创建一个方法。这个方法将成为该实例的一部分，并且可以像普通的实例方法一样被调用
'''
print("6"+"-"*60)

class MyClass:
    def __init__(self,value) -> None:
        self.value = value
#
def custom_method(self):
    print("Custom method called with value:",self.value)

obj1 = MyClass(1)
obj2 = MyClass(2)

obj1.custom_method = types.MethodType(custom_method,obj1)
obj1.custom_method()

#obj2的方法不存在
#obj2.custom_method()


'''
把装饰器作用到类和静态方法上
但是要保证装饰器放在@classmethod和staticmethod之前

具体原因就是@classmethod 和 @staticmethod 并不会实际创建可直接调用的对象
创建的是特殊的描述符对象
'''
print("7"+"-"*60)

class Spam:
    @timethis
    def instance_method(self,n):
        print(self,n)
        while n > 0:
            n -= 1
    
    
    @classmethod
    @timethis
    def class_method(cls,n):
        print(cls,n)
        while n > 0:
            n -= 1
    
    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1

s = Spam()
s.instance_method(10000000)
Spam.class_method(10000000)
Spam.static_method(1000000)


'''
装饰器为被包装的函数添加参数
'''
import inspect

print("8"+"-"*60)
def optional_debug(func):

    @wraps(func)
    def wrapper(*args,debug=False,**kwargs):
        if debug:
            print('Calling',func.__name__)
        return func(*args,**kwargs)
   
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',inspect.Parameter.KEYWORD_ONLY,default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper

@optional_debug
def spam_v4(a,b,c):
    print(a,b,c)

spam_v4(1,2,3)
spam_v4(1,23,4,debug=True)

#打印函数签名  inspect
print(inspect.signature(spam_v4))


'''
利用装饰器给类定义打补丁
'''
print("9"+"-"*60)
def log_getattribute(cls):
    # get the original implementation
    orig_getattribute = cls.__getattribute__

    #make a new definition
    def new_getattribute(self,name):
        print('getting:',name)
        return orig_getattribute(self,name)

    #修改了类的属性
       
    cls.__getattribute__ = new_getattribute
    return cls

@log_getattribute
class A:
    def __init__(self,x) -> None:
        self.x = x
    def spam(self):
        pass

a = A(4)
print(a.x)
a.spam()

