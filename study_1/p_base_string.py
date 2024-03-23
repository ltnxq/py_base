str = "RUNOOB"
# 超范围没有越界的异常 只是全部打印
# 0 . 。。。 -1 -2 -3
# print(str[0:10])
# -1 到 -3 就不可以 只能左到右？
print(str[-3:-1])

#字符串运算符
'''
+、*（重复输出）、[]、[:](左闭右开)、in 、 not in r/R(没有转义，原样输出)
'''

#字符格式化 %d、%s、%p(格式化变量地址)，包含一些辅助的指令左对齐等  %是占位符
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

#可以使用format格式输出 {} 占位符
print("我叫 {} 今年 {} 岁!".format('小强',20))

from collections import Counter
Var1 = "1116122137143151617181920849510"
Var2 = "1987262819009787718192084951"
print(Counter(Var1))
print(Counter(Var2))

# python字符串提供了大量的API供调用

str = '''
[
{
 "longitude":890.90,
 "latitude":989.90
}
]
'''

print(len(str))