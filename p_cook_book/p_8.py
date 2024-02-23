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

# @check_attributes(name=SizedString(size=8),shares=UnsignedInteger,price=UnsignedFloat)
# class Stock_v3:
#     def __init__(self,name,shares,price) -> None:
#         self.name = name
#         self.shares = shares
#         self.price = price

# print("13"+"-"*60)

# s = Stock_v3('ACME',52,91.4)


class Person_v3:
    def __init__(self, name):
        self.name = name

setattr(Person_v3,'age',UnsignedInteger('age'))
p3 = Person_v3('zyz')
print(p3.age)