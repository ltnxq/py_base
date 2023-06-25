# python 一切皆为对象，函数传递的是不可变对象或者可变对象
#在python中，strings、tuples和numbers 是不可更改的对象，而list、dict是可修改的对象
#不可变类似于c++的值传递、可变类似于c++的引用传递

# 不可变对象的传递
def change(a):
    print(id(a))
    a = 10
    print(id(a))
#如果传递是1 那么函数调用后对象发生改变 ，如果传递的是10 那么就没有发生改变
a = 1
print(id(a))
change(a)

#可变对象的传递
def changme(mylist):
    mylist.append([1,2,3,4])
    print("函数内取值：",mylist)
    return
mylist = [10,20,30]
changme(mylist)
print("函数外取值：",mylist)

#函数参数的类型 1、必须参数 2、关键字参数 3、默认参数 4、不定长参数
#关键字参数，可以通过名称去指定对象参数的值
def printinfo(name,age):
    print("name: ",name)
    print("age: ",age)
    return

#调用和申明不一致
printinfo(age=50,name="runoob")

#支持默认参数
#不定长参数 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def printinfo1(arg1,*vartuple):
    print("输出")
    print(arg1)
    print(vartuple)
    print(type(vartuple))
printinfo1(70,60,50)


#加了两个星号 ** 的参数会以字典的形式导入
def printdict(arg1,**vardic):
    print("dict 的输出")
    print(arg1)
    print(vardic)
printdict(1,a=2,b=3)
#1、{'a': 2, 'b': 3}

# lambda
x = lambda a : a + 10
print(x(5))

sum = lambda arg1,arg2:arg1 + arg2
print("相加后的值为: ",sum(10,20))
print("相加后的值为: ",sum(30,20))

#根据不同的参数返回不同的lambda js 函数对象吗
def myFunc(n):
    return lambda a:a*n
mydoubler  = myFunc(2)
myTripler = myFunc(3)

print(mydoubler(11))
print(myTripler(11))