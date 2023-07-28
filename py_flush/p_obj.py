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