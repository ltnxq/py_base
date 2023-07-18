#把list分片 成任意两个不重叠的部分
a = [10,20,30,40,50,60]
print(a[:2])
print(a[2:])

#s[a:b:c] 在s中的ab直接按照c为间隔来取
s = "abcdefgh"
print(s[::3])
print(s[::-1])  #hgfedcba
print(s[::-2])  #hfdb

#对切片进行赋值
x = list(range(10))
print(x)
#赋值右边的表达式必须是一个可迭代的对象
x[2:5] = [20,30]
print(x)
del x[5:7]
print(x)
