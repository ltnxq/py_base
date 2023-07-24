#创建一个从单词到其出现情况的映射
import sys
import re
import collections

#不太好的解决方式
def sumaary_char():
    WORD_RE = re.compile(r'\w+')
    index = {}
    with open("test.txt",encoding='utf-8') as fp:
      for line_no,line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no,column_no)
            
            #先进行get  没有就赋值一个空的[]
            occurrences = index.get(word,[])
            occurrences.append(location)
            index[word] = occurrences
    for word in sorted(index,key=str.upper):
        print(word,index[word])

#推荐的做法
def sumaary_char_better():
    WORD_RE = re.compile(r'\w+')
    index = {}
    with open("test.txt",encoding='utf-8') as fp:
      for line_no,line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no,column_no)
            
            #关键在于如果word已经有这个key,那么会返回这个key对应value
            index.setdefault(word,[]).append(location)
    for word in sorted(index,key=str.upper):
        print(word,index[word])

# collections.defaultdict(list) 当key不存在的时候直接调用list()函数
'''
defaultdict里的default_factory只会在__getitem__里被调用 
在其他的方法里完全不会发挥作用。比如 dd是个defaultdict k是个找不到的键 dd[k]这个表达式会调用default_factory创造某个默认值 而dd.get(k)则会返回None。
所有这一切背后的功臣其实是特殊方法__missing__。它会在defaultdict遇到找不到的键的时候调用default_factory 而实际上这个特性是所有映射类型都可以选择去支持的

__missing__方法只会被__getitem__调用 (比如在表达式d[k]中)。提供__missing__方法对get或者__contains__(in运算符会用到这个方法)这些方法的使用没有影响
'''
def sumary_char_defaultdict():
   WORD_RE = re.compile(r'\w+')
   index = collections.defaultdict(list)
   with open("test.txt",encoding='utf-8') as fp:
      for line_no,line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no,column_no)
            
            index[word].append(location)
        for word in sorted(index,key=str.upper):
            print(word,index[word])


'''
collections.OrderedDict这个类型在添加键的时候会保持顺序 因此键的迭代次序总是一致的。
OrderedDict的popitem方法默认删除并返回的是字典里的最后一个元素 但是如果像my_odict.popitem(last=False)这样调用它，那么它删除并返回第一个被添加进去的元素。

collections.ChainMap该类型可以容纳数个不同的映射对象 然后在进行键查找操作的时候 这些对象会被当作一个整体被逐个查找，直到键被找到为止

collections.Counter这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数器
还有像most_common([n])这类很有用的方法。most_common([n])会按照次序返回映射里最常见的n个键和它们的计数
'''


ct = collections.Counter("abcdefg")
print(ct)
ct.update("aaaccff")
print(ct)
print(ct.most_common(2))

'''
UserDict并不是dict的子类 但是UserDict有一个叫作data的属性 是dict的实例 这个属性实际上是UserDict最终存储数据的地方。
'''

class StrKeyDict(collections.UserDict):
   def __missing__(self,key):
      if isinstance(key,str):
         raise KeyError(key)
      return self[str[key]]
   # in的时候调用
   def __contains__(self, key: object) -> bool:
      return str(key) in self.data
   # set 时候调用
   def __setitem__(self, key, item):
        self.data[str(key)] = item

'''
MappingProxyType 如果给这个类一个映射,它会返回一个只读视图,当原映射做出修改,只读视图也会跟着改变
'''
from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d[1])

#'mappingproxy' object does not support item assignment
#d_proxy[2] = 'x'
d[2] = 'B'
print(d_proxy)