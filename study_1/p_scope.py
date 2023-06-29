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