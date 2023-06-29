#list和字符串的用法相似，都有反向索引的功能
#嵌套列表
a = ['2','3','4']
b = [5,6,7]
x = [a,b]
print(x)
print(x[0])
print(x[1])

#列表比较
import operator

a = [1,2]
b = [2,3]
c = [2,3]

print("operator.eq(a,b):",operator.eq(a,b))
print("operator.eq(a,b):",operator.eq(c,b))

#函数 len、max、min、list(seq)
#方法 append、count、index、insert、reverse、sort、clear、copy

a = [1,2,3]
b =  a
c = []
c = a
d = a


"""
可以看到a b c 三个是同一id值,当改变当中任一列表元素的值后，三者会同步改变。

但d的元素值不会变,改变d的元素值其它三个变量内的元素值也不会变。

从a b c d 的id值来看,a b c 地址全一样,唯有d分配了新地址。

所以一般情况下想复制得到一个新列表并改变新列表内元素而不影响原列表,可以采用d的赋值方式。

 d = a[:]

这只是针对这种比较单一的普通列表。
"""
import copy
a = [1,2,3,4]
b = a
#还有一个就是用list自带的copy()方法,把重新开辟内存空间存储新列表。
d = copy.copy(a)
b[0] = 'b'

print(a,b,d)
print(id(a),id(b),id(d))

#python 列表是链式存储结构非顺序存储结构
#1 2 3 4代表一个内存地址 list将其用链表连接在一起而已
a = [1,2,3,4]
for i in range(len(a)):
    print(id(a[i]))
a[1] = 100
print("------------------")
for i in range(len(a)):
    print(id(a[i]))

#相关API
a = [66.25,333,333,1,1234.5]
print(a.count(333),a.count(66.25),a.count('x'))
a.insert(2,-1)
a.append(33)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()
print(a)
a.sort()
print(a)   

#del 语句的使用