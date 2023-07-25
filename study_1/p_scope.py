'''
类似于js的语法作用域
Python 中只有模块 module,类class以及函数def、lambda才会引入新的作用域
其它的代码块（如 if/elif/else/、try/except、for/while等是不会引入新的作用域的,也就是说这些语句内定义的变量，外部也可以访问，如下代码：
'''
if True:
    msg = "i am a good man"

#外部可以访问 if内的变量
print(msg)

def inner():
    msg1 = "ssss"

#外部作用域不可访问函数内的变量
#内部作用域想要修改外部作用域的变量时候，需要使用gloab 关键字
num = 1
def changeNum():
    global num 
    print(num)
    num = 123
    print(num)
changeNum()
print(num)

#如果需要修改嵌套非全局作用域需要关键字nonlocal关键字
def outer():
    num = 10
    def inner():
        nonlocal num 
        num = 90
        print(num)
    inner()
    print(num)
outer()

num_a = 100
def outer_a():
    #如果定义相同的变量名称，那么就会在函数内创建局部的变量
    num_a = 190
    print(num_a)
outer_a()
print(num_a)



def f1(a):
    print(a)
    print(b)

'''
在编译字节码的时候 会把b当成局部变量,因为在函数体使用,在print(b)在函数局部发现b没有值 会报错
UnboundLocalError: local variable 'b' referenced before assignment
'''
b = 6
def f2(a):
    print(a)
    print(b)
    b = 9

#反汇编f1函数
from dis import dis
print(dis(f1))

#LOAD_GLOBAL b  f1中 把b当作成了全局变量去使用了

'''
48           0 LOAD_GLOBAL              0 (print)
              2 LOAD_FAST                0 (a)
              4 CALL_FUNCTION            1
              6 POP_TOP

 49           8 LOAD_GLOBAL              0 (print)
             10 LOAD_GLOBAL              1 (b)
             12 CALL_FUNCTION            1
             14 POP_TOP
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE

'''

#反汇编f2函数
#LOAD_FAST 把b当作了局部变量 即使f2函数中b是后赋值
print(dis(f2))

'''
57           0 LOAD_GLOBAL              0 (print)
              2 LOAD_FAST                0 (a)
              4 CALL_FUNCTION            1
              6 POP_TOP

 58           8 LOAD_GLOBAL              0 (print)
             10 LOAD_FAST                1 (b)
             12 CALL_FUNCTION            1
             14 POP_TOP

 59          16 LOAD_CONST               1 (9)
             18 STORE_FAST               1 (b)
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE

'''


print("--------------------------------闭包------------------------")
'''
函数闭包理解
闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定。
'''
#使用类存储临时数据
class Average():
    def __init__(self) -> None:
        self.series = []
    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

avg = Average()
print(avg(10))
print(avg(11))
print(avg(12))

#函数式实现
def make_average():
    #--- 闭包开始-----------
    series = []   #--自由变量
    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total /len(series)
    #----闭包结束-------------
    return average

'''
avg_func函数引用一直存在到调用结束,所以series的引用也会一直到avg_func销毁为止
'''
avg_func = make_average()  #返回一个函数
print(avg_func(10))
print(avg_func(11))
print(avg_func(12))

print(avg_func.__code__.co_varnames)  #局部变量
print(avg_func.__code__.co_freevars)  #自由变量  
print(avg_func.__closure__[0].cell_contents)

'''
nonlocal关键字 使用nonlocal 将变量绑定为自由变量
'''

def make_average_2():
    count = 0
    total = 0
    '''但是对数字、字符串、元组等不可变类型来说 只能读取,不能更新。
       如果尝试重新绑定,例如count=count+1,
       其实会隐式创建局部变量count。
       这样,count就不是自由变量了,因此不会保存在闭包中'''
    def average(new_value):
        nonlocal count,total
        count += 1
        total += new_value
        return total / count
    return average

print(make_average_2()(10))