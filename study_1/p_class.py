'''
1、两个下划线开头表示private属性
2、def定义类的方法的时候,第一个参数必须是self self == this
3、__开头的方法为private method
'''

#私有属性
from typing import Any


class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()

print(counter.publicCount)
# print(counter.__secretCount)

#私有方法
class site:
    def __init__(self,name,url):
        self.name = name
        self.url = url
    
    def who(self):
        print('name : ',self.name)
        print('url: ',self.url)

    def __foo(self):
        print("这是私有方法")
    
    def foo(self):
        print("这是公有方法")
        self.__foo()
    def __repr__(self) -> str:
        return "cccccc"
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return "invoke"

x = site("python exercise",'www.runoob.com')
x.who()
x.foo()
print(x)
print(x())


#class 的专有方法 类似于c++运算符的重载 < > () hash !=   __int__  __del__ 析构函数、__repr__、__len__、_cmp__、__call__、__hash__、__str__类似于java toSting 方法
#python 的class还有反向运算符的重载方法
'''
静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用。
普通方法: 默认有个self参数,且只能被对象调用。
类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器。

'''
#关于name属性属于python的内置属性 name __main__时候就是这个程序的主线程函数，但在别人的模块调用就是这个程序的名称