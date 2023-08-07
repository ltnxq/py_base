'''
1、创建符合python风格的对象
'''
from array import array
import math

class Vector2d:
    __slots__ = ('__x','__y')
    typecode = 'd'
    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y    
    '''
    定义__iter__方法,把Vector2d实例变成可迭代的对象,
    这样才能拆包,(例如 x, y=my_vector)。这个方法的实现方式很简单，直接调用生成器表达式一个接一个产出分量
    '''    
    def __iter__(self):
        return (i for i in(self.x,self.y))
    '''
    {!r}%r表示的用repr()处理;类似于的%s 或者{!s}表示用str()处理一样
    '''
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self) 
    '''
    利用对象的__iter__方法来构造tuple对象
    '''
    def __str__(self):
        return str(tuple(self))
    def __bytes__(self):
        return (bytes([ord(self.typecode)])) + bytes(array(self.typecode,self))
    
    # == 运算符最终调用的方法
    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x,self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __format__(self, fmt_spec='') -> str:
        components = (format(c,fmt_spec) for c in self)
        return '({},{})'.format(*components)
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    
    
    @classmethod
    def frombytes(cls,octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

'''
2、对象的格式化输出 format()函数  或者 str.format()
   {x!r} == repr(x) {x!s} == str(x) {x!a} == ascii(x)
'''
br1 = 1/2.43
print(br1)
print(format(br1,'0.4f'))

#rate 代表后面formate的参数名称 和 格式化规则无关 保留两位小数
'''
第2条标注指出了一个重要知识点:'{0.mass:5.3e}'这样的格式字符串其实包含两部分，冒号左边的'0.mass'在代换字段句法中是字段名，冒号后面的'5.3e'是格式说明符
'''
s1= '1 BRL = {rate:0.2f} USD'.format(rate = br1)
print(s1)

# '''
#  #b\x\ f  \% 表示百分号的表示形式
# '''
#1代表保留一位有效数字
print(format(2/3,'.1%'))

'''
3、对象可hash的条件
  ①-实现hash方法
  ②-实现__eq__方法
  ③-对象不可变才可以hash 实例的散列值绝不应该变化,对象实现只读特性只读特性。
'''

'''
4、python的私有属性,带__下划线的属性被称为私有属性,py会把属性名存入实例的__dict__属性中,而且会在前面加上一个下划线和类名 __Dog__mod
'''
v1 = Vector2d(3,4)
print(v1.__dict__)
#开后门的修改方式,这方式比java相比 不安全
v1._Vector2d__x = 8.0
print(v1)

'''
5、__slots__类属性节省空间 python会在实例中名为__dict__的字典中存储实例属性,为了使用底层的散列表提升访问速度,字典会消耗大量内存
  通过在类中重新定义__slots__(使用元组),能节省大量内存
  如果不把__weakref_加入__slots__,实例就不能作为弱引用目标

  如果要处理数百万个数值对象,应该使用NumPy数组(参见2.9.3节)。NumPy数组能高效使用内存,而且提供了高度优化的数值处理函数,其中很多都一次操作整个数组
'''

'''
6、覆盖类属性
   python有个独特的属性 类属性可用于为实例属性提供默认值,Vector2d的typecode属性就是类的属性
   但是为实例添加一个typecode属性会把同名的属性覆盖
'''