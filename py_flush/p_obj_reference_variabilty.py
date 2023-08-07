'''
1、对象在右边创建或者获取,在此之后左边的变量才会绑定到对象上,像是为对象贴标注
   因为对象不过是标注,所以无法阻止为对象贴多个标注,贴多个标注就是别名
'''

class Gizmo:
    def __init__(self) -> None:
        print("Gizmo id:%d"%id(self))

x= Gizmo()
print(dir())

'''
2、== 比较两个对象的值  而 is 比较的是两个对象的标识  是调用 object的 __equal__方法 一般内置类型会进行重写  object的__equal__就是比较对象的id
'''

a = [1,2,3]
b = [1,2,3]

print("a==b",a == b)
print("a is b",a is b)

'''
3、构造方法或[:]做的是浅复制（即复制了最外层容器，副本中的元素是源容器中元素的引用）
   深复制-副本中的元素和源容器不是同一个引用 copy模块的 copy和deep copy可以实现 浅复制 和深复制
   注意:deepcopy能处理循环引用
        我们可以实现特殊方法__copy__()和__deepcopy__(),控制copy和deepcopy的行
'''

class Bus:
    def __init__(self,passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

import  copy
bus1 = Bus(['Alice','Bill',"XYX","ZYZ"])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(id(bus1),id(bus2),id(bus3))

bus1.drop("Bill")
print(bus2.passengers)

print(id(bus1.passengers),id(bus2.passengers),id(bus3.passengers))

print(bus3.passengers)

'''
4、默认参数不要用可变对象
   出现这个问题的根源是，默认值在定义函数时计算（通常在加载模块时），因此默认值变成了函数对象的属性
   可变默认值导致的这个问题说明了为什么通常使用None作为接收可变值的参数的默认值
'''
class HauntedBus:
    def __init__(self,passengers=[]):
        self.passengers = passengers
    def pick(self,name):
        self.passengers.append(name)
    def drop(self,name):
        self.passengers.remove(name)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

bus3 = HauntedBus()
print(bus3.passengers)

#默认的列表对象是同一个列表对象
print(id(bus2.passengers))
print(id(bus3.passengers))


'''
正确处理默认参数
'''
class  TWilightBus:
    def __init__(self,passenger=None):
        if passenger is None:
            self.passenger = []
        else:
            self.passenger = list(passenger)
    def pick(self,name):
        self.passenger.append(name)
    def drop(self,name):
        self.passenger.remove(name)


tStuents = [[1,2],"ab","a"]
tStuentsTw = TWilightBus(tStuents)
tStuentsTw.pick("abcd")
print(tStuents)
print(tStuentsTw.passenger)

#修改tStuents的某一个元素 观察另一个是否有变化  list构造是一种浅复制
tStuents[0].append(3)
print(tStuents)
print(tStuentsTw.passenger)

'''
5、弱引用,对象的回收(python通过引用计数实现垃圾回收)
   弱引用在缓存应用中很有用，因为我们不想仅因为被缓存引用着而始终保存缓存对象,类似于c++的weak_ptr Java其实也有弱引用
   不是每个Python对象都可以作为弱引用的目标(或称所指对象)。基本的list和dict实例不能作为所指对象,但是它们的子类可以轻松地解决这个问题
'''
import weakref
s1 = {1,2,3}
s2 = s1

def bye():
    print("Gone   with the wind...")

ender = weakref.finalize(s1,bye)
print(ender.alive)

del s1
print(ender.alive)

s2 = "spam"
print(ender.alive)

a_set = {0,1}
wref = weakref.ref(a_set)
print(wref)

print(wref())
a_set = {2,3,4}
print(wref() is None)

'''
6、weakref的集合 
   ① WeakValueDictionary类实现的是一种可变映射,里面的值是对象的弱引用。
     被引用的对象在程序中的其他地方被当作垃圾回收后,对应的键会自动从WeakValueDictionary中删除。
     因此,WeakValueDictionary经常用于缓存。
   ② WeakKeyDictionary的键是弱引用
   ③ WeakSet 元素没有强引用时 集合会把它删除。”如果一个类需要知道所有实例,一种好的方案是创建一个WeakSet类型的类属性,保存实例的引用
'''

class Cheese:
 def __init__(self, kind):
    self.kind = kind
 def __repr__(self):
    return 'Cheese(%r)'%self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
                 Cheese('Brie'), Cheese('Parmesan')]

'''
临时变量引用了对象，这可能会导致该变量的存在时间比预期长。
通常，这对局部变量来说不是问题，因为它们在函数返回时会被销毁。
但是在示例中for循环中的变量cheese是全局变量,除非显式删除,否则不会消失
'''
for cheese in catalog:
  stock[cheese.kind] = cheese  

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))

