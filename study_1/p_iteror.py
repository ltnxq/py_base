#迭代器有两个基本的方法：iter() 和 next()。
#字符串，列表或元组对象都可用于创建迭代器：
list = [1,2,3,4]
#创建迭代器对象
it = iter(list)
# next(it)访问迭代器对象
# for x in it:
#     print(x,end = " ")

import sys

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         print("迭代结束")
#         sys.exit()
#一个类如果实现迭代器的功能 那么需要实现 __iter__() 和 __next__()方法
# python 通过 StopIteration 异常标识 迭代的完成

# class MyNumber:
#     def __init__(self) -> None:
#         pass
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# myClass = MyNumber()
# myiter = iter(myClass)

# for x in myiter:
#     print(x)

 #python 生成器的概念 yield 返回的函数只能用于迭代作用 每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次
 #执行next()方法时从当前位置继续运行

def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if(counter > n):
              return
        yield a
        a,b = b,a+b
        counter += 1
f = fibonacci(10)

print("run method fibonacci")

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
    