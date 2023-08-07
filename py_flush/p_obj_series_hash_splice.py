from array import array
import reprlib
import math
import numbers
from typing import Any

'''
通过len和getitem实现类可切片的序列
'''
class Vector:
    typecode = 'd'
    def __init__(self,components) -> None:
        self._components = array(self.typecode,components)
    
    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)])+bytes(self._components)) 
    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
    def __len__(self):
        return len(self._components)
    def __getitem__(self,index):
        #获取self对应的类,后面通过cls来实例化对象
        cls = type(self)
        #针对[1:4:2]返回切片对象本身
        if isinstance (index,slice):
           return cls(self._components[index])
        #单个索引的话,返回某一个值
        elif isinstance(index,numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls = cls))
    shortcut_names = 'xyzt'
    def __getattr__(self,name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0<= pos <= len(self._components):
                return self._components[pos]
            msg = '{.__name__!r} object has no attribute {!r}'
            raise AttributeError(msg.format(cls,name))
    
    def __setattr__(self, name,value) -> None:
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = "readonly attribute {attr_name!r}"
            elif name.islower():
                error = "cannot set attributes 'a' to 'z' in {cls_name!r} "
            else:
                error = ""
            if error:
                msg = error.format(cls_name = cls.__name__,atrr_name = name)
                raise AttributeError(msg)
        #
        super().__setattr__(name,value)
    
    def __eq__(self,other) -> bool:
        #使用tuple有个缺点就是需要把self或者other对象转换为tuple对象,去调用tuple对应的eq方法,对于含有维度比较多的向量效率不高
        #return tuple(self) == tuple(other)
        #推荐使用zip函数去解决
        return len(self) == len(other) and all(a==b for a,b in zip(self,other))

    def __hash__(self) -> int:
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor,hashes,0)       
    


    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

class MySeq:
    def __getitem__(self,index):
        return index
s = MySeq()
print(s[1])
print(s[1:4])
print(s[1:4:2])
print(s[1:4:2,9])
print(s[1:4:2,7:9])

'''
1、关于slice 
   ①-slice是内置的类型,含有indices方法
   ②-S.indices(len)-> (start, stop, stride)  给定长度为len的序列
     计算S表示的扩展切片的起始(start)和结尾(stop)索引,以及步幅(stride)。超出边界的索引会被截掉，这与常规切片的处理方式一样
     换句话说
     indices方法开放了内置序列实现的棘手逻辑,用于优雅地处理缺失索引和负数索引，
     以及长度超过目标序列的切片。这个方法会“整顿”元组,把start、stop和stride都变成非负数,而且都落在指定长度序列的边界内
'''

s1 = "abcde"
#虽然切片的stop不合法的,但是被内置的slice.indce 进行了合理的优化了
print(s1[0:10:2])
print(s1[-3:])

'''
2、切片原理就是类实现 len 和 getitem的逻辑方法,具体参考 上面的 class Vector
'''

#测试切片后的用法
v7 = Vector(range(7))
# print(v7[-1])
# print(v7[1:4])
# print(v7[-1:])
# print(v7[1,2])

# print(v7.k)

'''
3、__setattr__和__getattr__动态实现存取属性
'''

'''
4、reduce函数接收两个参数,第一个参数是接收两个参数的函数fn,第二个是可迭代的对象s,第三个参数是初始值 对于加法一般是0 乘法一般是1 reduce(fn,iter,initValue)
   具体运行就是fn(s[0],s[1]) 得到s0+s1的值r1 =》fn(r1+s[2])
'''
import functools
re = functools.reduce(lambda a,b:a*b,range(1,6))
print(re)

#三种求解疑惑的方式
#① for循环
n = 0
for i in range(1,6):
    n = n^i

print(n)

#②-reduce
n1 = functools.reduce(lambda a,b:a^b,range(1,6))
print(n1)

#③-使用内置函数取代lambda
import operator
n2 = functools.reduce(operator.xor,range(1,6))
print(n2)
