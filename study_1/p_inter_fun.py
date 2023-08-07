'''
1、setattr() 函数 ,setattr(object, name, value) 为某个对象设置某个属性,如果没有就添加这个属性
   getattr(object,name)   获取对象的某个属性值
   hasattr(object, name)  函数用于判断对象是否包含对应的属性
   delattr(object, name)  函数用于删除属性
'''
from typing import Any


class A:
    bar = 1
a = A()
#
print(getattr(a,'bar'))
setattr(a,'bar',10)
print(getattr(a,'bar'))
setattr(a,"bar2","helloworld")
print(getattr(a,'bar2'))

'''
2、all 判断可迭代器对象是否为TRUe  0 NONE "" 都是false 注意:空元组、空列表返回值为True 这里要特别注意。
   any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False 则返回 False 如果有一个为 True 则返回 True。
'''
print(all([0,1,2,3]))
print(all([9,1,2,3]))
print(all(()))
print(any([0,1]))

'''
3、hex()  == 转换为16进制
   bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
   oct() 函数将一个整数转换成 8 进制字符串,8 进制以 0o 作为前缀表示
'''

'''
4、next() 返回下一个迭代的项目
'''

'''
5、slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
'''

myslice = slice(5)
arr = [1,2,3,4,4,5,6,6,7,7]
print(arr[myslice])

'''
6、id - 返回对象的唯一标识
'''

'''
7、object() 函数返回一个空对象，我们不能向该对象添加新的属性或方法。
   object() 函数返回的对象是所有类的基类，它没有任何属性和方法，只有 Python 内置对象所共有的一些特殊属性和方法，例如 __doc__ 、__class__、__delattr__、__getattribute__ 等。
   object() 是 Python 中最基本的对象,其他所有对象都是由它派生出来的。因此object() 对象是所有 Python 类的最顶层的超类（或者称为基类或父类），所有的内置类型、用户定义的类以及任何其他类型都直接或间接地继承自它。
'''

'''
8、sort 与 sorted 区别：
   sorted(iterable, key=None, reverse=False)   reverse 降序还是升序  key 作为排序的准则  可以是lambda
   key可以是 lambda x:(x[0],x[1])  奖牌榜的排序比较方便  金牌 ==》 银牌 ==》铜牌
   sort 是应用在 list 上的方法,sorted 可以对所有可迭代的对象进行排序操作。
   list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list,而不是在原来的基础上进行的操作  效率比较高
'''

list = [7,6,6,3,9,10]
list1 = sorted(list)
print(id(list))
print(id(list1))

'''
9、enumerate(sequence, [start=0]) sequence -- 一个序列、迭代器或其他支持迭代对象。 start 起始的索引 返回枚举对象
'''
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print("enumerate function.......................")
for i, element in enumerate(seasons,2):
    print(i, element)

'''
10、input() 函数接受一个标准输入数据，返回为 string 类型
'''
# a = input("请输入: ")
# print(a,type(a))

'''
11、int() 函数用于将一个字符串或数字转换为整型   int(x, base=10)
    bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False
    ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串)的配对函数 它以一个字符串(Unicode 字符）作为参数，返回对应的 ASCII 数值
    float() 函数用于将整数和字符串转换成浮点数
    chr() 用一个整数作参数，返回一个对应的字符

'''
print(int('13',16))

'''
12、str() 函数将对象转化为适于人阅读的形式
'''

'''
13、isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
    isinstance() 与 type() 区别：
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    isinstance() 会认为子类是一种父类类型，考虑继承关系。 
'''
a = 2
print(isinstance(a,int))
print(isinstance(a,str))
print(isinstance (a,(str,int,list)))

#type 和 isinstance的状态
class A:
    pass

class B(A):
    pass

print(isinstance(A(),A))
print(type(A())  == A)
print(isinstance(B(),A))
print(type(B()) == A)


'''
14、filter(func,iterator)  对序列进行过滤 func 返回True 或者 False 返回一个迭代器对象
    map(function,iterable....)  类似 java map
'''
def is_odd(n):
    return n % 2 == 1
#返回的是可迭代的对象
tmpIterator = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])
# newlist = list(tmpIterator)
print(tmpIterator,type(tmpIterator))
for i in tmpIterator:
    print(i)

def square(x):
    return x ** 2
tmpMap = map(square,[1,2,3,4,5])
tmpMap1 = map(lambda x:x**2,[1,2,3,4,5,9])
for i in tmpMap:
    print(i)  

for i in tmpMap1:
    print(i)  

'''
15、tuple() 函数将可迭代系列（如列表）转换为元组
    list() 方法用于将元组或字符串转换为列表
    set() 函数创建一个无序不重复元素集 
'''
print(tuple("ssssssssssss"))
# print(list("kkkkkkkkkkkkkkk"))
print(set("sasasasasa"))
'''
16、callable() 函数用于检查一个对象是否是可调用的。如果返回 True object 仍然可能调用失败；但如果返回 False 调用对象 object 绝对不会成功。
    对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True
'''
def add(a,b):
    return a +b

print(callable(add))
#类定义了call方法
class C:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
print(callable(C))
print(callable(8))

'''
17、format语法 str.format()  具体数字格式化参考教程
    ①:不指定位置
    ②:指定位置
    ③:指定参数
'''
s1 = "{} {}" .format("hello","world")    #不指定位置
print(s1)

s2 = "{1},{0},{1}".format("hello","world")  #指定位置
print(s2)

print("网站名:{name},地址 {url}".format(name = "菜鸟教程",url = "www.runoob.com")) #指定参数
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

#数字格式化
print("{:.4f}".format(3.1415926))

'''
18、Python len() 方法返回对象（字符、列表、元组等）长度或项目个数
'''

'''
19、property() 函数 用法参考 https://zhuanlan.zhihu.com/p/210036690
    property属性的两种方式:1、装饰器 2、在类中定义值为property对象的类属性
'''

#property属性定义,在方法基础上加上@property 、仅有一个self参数、调用时候无需括号
class Foo:
    def func(self):
        pass

    @property
    def prop(self):
       return 100

foo_obj = Foo()
foo_obj.func()
print(foo_obj.prop)

#新式类，具有三种@property装饰器
class Goods:
    def __init__(self) -> None:
        self.__origin_price = 100
        self.__discount = 0.8
    @property
    def price(self):
        print("@property")
        newprice = self.__origin_price *  self.__discount
        return newprice

    @price.setter
    def price(self,value):
        print("@price.setter")

    @price.deleter
    def price(self):
        print("@price.deleter")

obj = Goods()
print(obj.price)
obj.price = 123
del obj.price

#2、类属性方式
# property方法中有个四个参数
# 第一个参数是方法名，调用 对象.属性 时自动触发执行方法。
# 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法。
# 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法。
# 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息。

class Car(object):
    def get_bar(self):
        print("getter...")
        return "opc"
    def set_bar(self,value):
        print("setter...")
        return 'set value' + value
    def del_bar(self):
        print("delter.....")
        return "laozyz"
    
    BAR = property(get_bar,set_bar,del_bar,"这个是一个描述汽车的类")

obj1 = Car()
obj1.BAR
obj1.BAR = "alex"

desc = Car.BAR.__doc__
print(desc)
del obj1.BAR

'''
20、frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

'''
list1 = [1,2,4,5]
b = frozenset(list) # 是b不可删除或者添加 list1 无关影响
list1.remove(1)
print(list1)

'''
21、range() 函数返回的是一个可迭代的对象，而不是列表类型
    range(stop)、range(start,stop,[,step])  step 默认是 1  注意是左闭右开的模式
'''

for num in range(1,6,2):
    print(num)
print("....................................")
for number in range(6,1,-1):
    print(number)

'''
22、reversed 函数返回一个反转的迭代器 可以是 tuple, string, list 或 range。
'''

'''
23、__import__() 函数用于动态加载类和函数 
    如果一个模块经常变化就可以使用 __import__() 来动态载入

    reload() 用于重新载入之前载入的模块
'''

'''
24、max()、min() 返回最大、最小值
    sum() 对序列进行求和计算  sum(iterable[, start])  start - 是指定相加的参数,没有就是默认为0
'''

print(sum([0,1,2]))
print(sum((2,3,4),1))


'''
25、round() 方法返回浮点数 x 的四舍五入值，准确的说保留值将保留到离上一位更近的一端（四舍六入） 精度要求高的，不建议使用该函数
'''
print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2))

'''
26、hash() 用于获取取一个对象（字符串或者数值等）的哈希值
'''

'''
27、memoryview() 函数返回给定参数的内存查看对象(memory view)。
    所谓内存查看对象 是指对支持缓冲区协议的数据进行包装 在不需要复制对象基础上允许Python代码访问。
'''

'''
28、zip函数 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
            如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
            语法zip([iterable,...])
'''
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b) #输出[(1,4),(2,5),(3,6)]

#与zip相反,*zipped可理解为解压,返回二维矩阵式
zip1 = zip(*zipped) #输出[(1,2,3),(4,5,6)]
print(zip1)

for item1 in zip1:
    print(item1)

#itertools.zip_longest函数的行为有所不同：使用可选的fillvalue（默认值为None）填充缺失的值，因此可以继续产出，直到最长的可迭代对象耗尽
from itertools import zip_longest
for item2 in zip_longest(range(3),'ABC',[0.0,1.1,2.2,3.3],fillvalue=-1):
    print(item2)