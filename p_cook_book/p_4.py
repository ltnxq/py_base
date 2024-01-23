'''
迭代器和生成器相关知识
'''

'''
1、迭代器的基础知识和原理
'''
print("1"+"-"*60)
a = [1,2,3]
#获取迭代器
iterm_a = iter(a)
try:
    while True:
        f = next(iterm_a)
except StopIteration:
    print("catch StopIteration")
    pass

'''
当迭代到最后一个元素的时候,迭代器的默认行为是抛出StopIteration
可以让其返回NODE
'''
print("2"+"-"*60)
iterm_b = iter(a)
while True:
    f = next(iterm_b,None)
    if f is None:
        print("iter over.......")
        break
    print(f)

'''
2、委托迭代
   实现迭代协议的__iter__方法 委托给列表的迭代行为
'''
class Node:
    def __init__(self,value) -> None:
        self._value = value
        self._children = []
    
    def __repr__(self) -> str:
        return 'Node({!r})'.format(self._value)
    
    def add_child(self,node):
        self._children.append(node)
    
    def __iter__(self):
        return iter(self._children)

print("3"+"-"*60)
root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for child in root:
    print(child)


'''
3、生成器的实现
'''
print("4"+"-"*60)
def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x
        x += increment
for  i in frange(0,4,0.5):
    print(i)

# list、sum都是可以接受生成器作为参数
a = list(frange(1,8,0.5))
b = sum(frange(1,10,0.5))
print(a)
print(b)

'''
4、实现迭代协议
   使用生成器来实现一个迭代协议
   yield from 从另一个方法产生值
'''
class Node_1:
    def __init__(self,value) -> None:
        self._value = value
        self._children = []
    
    def __repr__(self) -> str:
        return 'Node({!r})'.format(self._value)
    
    def add_child(self,node):
        self._children.append(node)
    
    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

print("5"+"-"*60)
root = Node_1(0)
child1 = Node_1(1)
child2 = Node_1(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node_1(3))
child1.add_child(Node_1(4))
child2.add_child(Node_1(5))

for ch in root.depth_first():
    print(ch)

'''
5、反向迭代器
   内建函数reversed 可以创建反向迭代器
'''
print("6"+"-"*60)
a = [1,23,89,67,"hello"]
for i in reversed(a):
    print(i)

'''
带有额外状态的生成器函数
利用class封装一些额外的属性
'''
from collections import deque

print("7"+"-"*60)
class linehistory:
    def __init__(self,lines,histlen = 3) -> None:
        self.lines = lines
        self.history = deque(maxlen=histlen)
    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append((lineno,line))
            yield line
    def clear(self):
        self.history.clear()

with open('foo.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno,hline in lines.history:
                print('{}:{}'.format(lineno,hline),end='')

'''
对迭代器或者生成器做切片操作
itertools.isslice()函数可以解决
'''
print("8"+"-"*60)

import itertools
def count(n):
    while True:
        yield n
        n += 1

c = count(0)
for x in itertools.islice(c,10,20):
    print(x)

'''
跳过可迭代对象的前一部分区域
itertools  dropwhile的使用
'''
print("9"+"-"*60)
with open('foo.txt') as f:
    for line in f:
        print(line,end="")
print()
#忽略注释行
print("10"+"-"*60)
from itertools import dropwhile
#只会舍弃第一个注释的#符号的行,其他行不需要进行筛选直接返回
with open('foo.txt') as f:
    for line in dropwhile(lambda line : line.startswith('#'),f):
        print(line,end="")

'''
跳过已知的行数
'''
items = ['a','b','c',1,4,10,15]
#最后一个参数None表示 除了前三个元素 都需要
for x in itertools.islice(items,2,None):
    print(x)

'''
忽略所有的注释
'''
print("11"+"-"*60)
with  open('foo.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line,end='')

'''
6、以索引值对的形式迭代序列
   enumerate的使用 默认start = 0
'''
print("12"+"-"*60)
my_list = ['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)
print("---------------------------")
for idx,val in enumerate(my_list,start=2):
    print(idx,val)

print("-----------summary words-----")
from collections import defaultdict
word_summary = defaultdict(list)
with open('foo.txt','r') as f:
    lines = f.readlines()
for idx,line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
print(word_summary)

'''
7、同时迭代多个序列
   zip是按照长度序列最短的作为迭代结束的条件,zip返回的只是一个迭代器 
   如果最短这种不是需要的场景,可以使用itertools.ziplong()来代替
'''
print("13"+"-"*60)
xpts = [1,5,4,2,10,7,8]
ypts = [101,78,37,15,62,99]
zpts = [1011,6722,1209,6772,2881]

for x,y,z in zip(xpts,ypts,zpts):
    print(x,y,z)

print("14"+"-"*60)
from itertools import zip_longest
#fillvalue这个参数可以用来作为默认值 而不是None
for i in zip_longest(xpts,ypts,fillvalue = 0):
    print(i)

'''
8、在不同的容器中迭代
   itertools chain方法  chain最常见的用途是想迭代的元素分布在不同的集合中
   chain()相对于 + 更加节省内存,并且+号需要两个数据类型是相同的
'''
print("15"+"-"*60)
from itertools import chain
a = [1,2,3,4]
b = ['x','y','z']
for x in chain(a,b):
    print(x)

print("16"+"-"*60)
'''
chain()相对于 + 更加节省内存,并且+号需要两个数据类型是相同的
'''
for y in a + b :
    print(y)


'''
9、利用生成器处理一个文件夹下多个文件数据
   比如日志目录下多个日志文件
   yield 和 yield from 的区别?
   yield后面跟上一个值 在迭代的时候返回
   而yield from 后面跟着也必须是生成器
'''
print("17"+"-"*60)
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepath,top):
    '''
    Find all filename in a directory tree that match a shell wildcard pattern
    '''
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepath):
            yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    open a sequence of filenames one at a time producing a file object
    The file is closed immediately when processing to next iteration
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename,'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename,'rt')
        else:
            f = open(filename,'rt')
        yield f
        #在下一个迭代的周期中被关闭
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern,lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

#获取目录下所有的日志文件
filepath = r'D:\zyz\project_my\c++\webServer\webServer\logs'
lognames = gen_find('rorat*',filepath)

#打开对应的文件 返回的也是生成器
files = gen_opener(lognames)

#返回对应的行数据
lines = gen_concatenate(files)

word_pattern = r".*14:18:00.177.*"
pylines = gen_grep(word_pattern, lines) 

#生成器被串联起来,for循环的每个迭代都会驱动生成器生成一份数据
# for pline in pylines:
#      print(pline)

'''
10、扁平化处理嵌套的序列
'''
print("18"+"-"*60)
from collections import Iterable

def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        #判断是否是可迭代对象除了字符串和字节数组
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1,2,(3,4),['hello','word']]
for h in flatten(items):
    print(h)

'''
11、两个有序队列合并后 再次进行有序输出
    heapq.merge的原理是相反,它只是简单地检查每个输入序列中的第一个元素，将最小的那个发送出去
    并不会把两个有序的队列先进行合并再进行输出
'''
print("19"+"-"*60)
import heapq
a = [1,4,7,10]
b = [2,5,6,11]
c = heapq.merge(a,b)

for x in c:
    print(x)

'''
12、iter读取文件数据
    iter()接受一个无参的可调用对象 一个哨兵作为结束的标记
'''
print("20"+"-"*60)
import sys
with open('foo.txt') as f:
    for chunk in iter(lambda:f.read(10),''):
        sys.stdout.write(chunk)
