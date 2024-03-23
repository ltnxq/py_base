import statistics
from  collections import deque

'''
1、变量分解
   只要变量是可迭代的，那么就可以进行变量的分解
'''
print("1"+"-"*60)
p = (4,5)
x,y = p
print(x)
print(y)
'''
如果数量不匹配将会出现错误
x,y,z = p
'''


#---------------------
print("2"+"-"*60)
data = ['ACME',50,91.1,(2012,12,21)]
name,shares,prices,(year,month,day) = data
print(name)
print(shares)
print(prices)
print(year)
print(month)
print(day)

print("3"+"-"*60)
a,b,c,d,e = "hello"
print(a)
print(e)

'''
如果想丢弃某个值,可以选一个用不到的变量名来进行占位
'''
print("4"+"-"*60)
data = ['ACME',50,91.1,(2012,12,21)]
_,shares,price,_ = data
print(shares)
print(price)


'''
2、从任意长度的可迭代对象中分解元素
   * 表达式的利用  *修饰的变量的类型是list
   statistics.mean()方法 求平均值
'''
def drop_first_last(grades):
    first,*middle,last = grades
    return statistics.mean(middle)

print("5"+"-"*60)
record = ('Dave',"dave@example.com",'773-555-1212','847-555-1212')
name,email,*phone_number = record
print(type(phone_number))
print(name)
print(email)
print(phone_number)

'''
*修饰的变量也可以位于列表的第一个位置
'''
print("6"+"-"*60)
sales_record = [1,2,3,4,5]
*trailing_qtrs,current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg)

'''
*表达式 迭代一个变长的元组对象
'''
print("7"+"-"*60)
records = [('foo',1,2),('bar','hello'),('foo',3,4)]
def do_foo(x,y):
    print('foo',x,y)
def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

'''
*表达式和字符串的split结合使用
'''
print("8"+"-"*60)
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(":")
print(uname)
print(homedir)
print(sh)

'''
保存最后N个元素
'''
def search(lines,pattern,history = 5):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

def search_in_file():
    with open('foo.txt',"r",encoding  = "utf-8") as f:
        for line ,prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline,end="")
            print(line,end='')
            print('-'*20)

'''
找到最大或者最小的N个元素
heapq 模块的使用  底层使用的堆的数据结构
nlargest、nsmallest接收key参数作为比较的准则,使用于n相对比较小的场景

'''
print("9"+"-"*60)
import heapq
nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

print("10"+"-"*60)
portdolio = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'AAPL','shares':100,'price':543.2},
    {'name':'FB','shares':200,'price':21.09},
    {'name':'HPQ','shares':35,'price':31.75},
    {'name':'YHOO','shares':45,'price':16.35},
    {'name':'ACME','shares':75,'price':115.65},
]
#先按照shares 进行 排序 如果相同再按照 price进行排序
cheap = heapq.nsmallest(2,portdolio,key = lambda s:(s['shares'],s['price']))
expensive = heapq.nlargest(2,portdolio,key = lambda s:(s['shares'],s['price']))
print(cheap)
print(expensive)

'''
列表转换为堆的形式
'''
print("11"+"-"*60)
nums = [1,6,2,23,7,-4,18,23,42,37,2]
heap = list(nums)  #从原数据构造一个新的list
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

'''
构建一个简单的优先级队列
'''
print("12"+"-"*60)
class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        #优先级 -priority 次优先是index 这样做好处就是防止由于优先级相同而无法进行比较
        heapq.heappush(self._queue,(priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
class Item:
    def __init__(self,name) -> None:
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
    
q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

'''
3、将字典的键映射到多个值上
   collections 模块的defaultdict的应用
'''
print("13"+"-"*60)
from collections import defaultdict
#构造参数可以是list 也可以是set set就是进行去重
d = defaultdict(list)
d['a'].append(1)
d['a'].append(1)
d['b'].append(4)
print(d)

d1 = defaultdict(set)
d1['a'].add(1)
d1['a'].add(1)
d1['b'].add(4)
print(d1)

'''
控制字典顺序 orderedDict的使用
维护着一个链表来实现插入的顺序 python自己的字典也是按照插入顺序来的
orderedDict的占用的内存空间是大于原生的dict这点要注意
'''
from collections import OrderedDict
print("14"+"-"*60)
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print(d)
for key in d:
    print(key,d[key])

'''
对字典求最大值、最小值和平均值等计算
zip的使用 返回一个可迭代的对象,zip返回的流只能使用一次而不能多次使用
'''
print("15"+"-"*60)
prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
    'FC': 10.75
}
# zip函数将字典的键值进行反转
min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))
print("min_price:{}".format(min_price))
print("max_price:{}".format(max_price))

#排序
price_order_dict = sorted(zip(prices.values(),prices.keys()))
print(price_order_dict)

'''
去重并保持元素顺序不变
'''
print("16"+"-"*60)
def dedupe(items):
    #?思考一下为啥用set进行集合去重? 当然list也可以 但是set因为底层是hashtable 判断元素是否存在 效率更高
    seen = set()
    for item in items:
        if item not in seen:
            yield item  #利用生成器 在遍历的时候 可以获取值
            seen.add(item)
a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))

'''
4、对切片进行命名,如果某一个切片具有一些业务含义,尽量使用一个变量进行命名,防止代码中出现很多的硬编码
   .start .stop .step 分别对应切片的开始、结束、步长
'''
print("17"+"-"*60)
shares = slice(1,36,1)
items = [0,1,2,3,4,5,6]
a = slice(2,4,1)
print(items[2:4])
print(items[a])
#对2到3之间的元素重新赋值
items[a] = [10,11]
print(items)
print(a.start)
print(a.stop)
print(a.step)

'''
top n的求解 使用collection模块的Counter
    Counter底层的实现是字典,在元素和出现次数做了映射 所以元素必须是可hash的对象
    两个Counter对象之间可以进行一些数学运算 比如 + -等
'''
print("18"+"-"*60)
from collections import Counter
words = [ 
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 
 'my', 'eyes', "you're", 'under' 
] 
#构造一个Counter对象
words_counts = Counter(words)
top_three = words_counts.most_common(3)
print(words_counts.popitem())
print(top_three)
#底层是字典 继承了字典
print(words_counts['eyes'])
#增加一部分单词
morewords = ['why','are','you','not','looking','in','my','eyes']
words_counts.update(morewords)
print(words_counts['eyes'])

#利用Counter进行一些数学运算
words_counts_1 = Counter(words)
more_words_count = Counter(morewords)
print(words_counts_1)
print(more_words_count)
c = words_counts_1 + more_words_count
print(c)
c = words_counts_1 - more_words_count
print(c)

'''
5、通过公共键对列表进行排序
   使用operator 模块的 itemgetter
   sorted、min、max接受一个callable作为key来进行比较和排序,key作为callable返回一个特定的值
   一般itemgetter用于原生的字典的操作
   而attrgetter一般用于自定义的类的某一个属性进行操作 
   而lambda两种场景都是适合的
'''
'''
 operator.itemgetter  标准库 operator 模块中的一个函数，用于创建一个可调用对象，该对象用于从对象中获取指定索引或键对应的值
'''
print("itemgetter_test"+"-"*60)
from operator import itemgetter 

data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# 使用 itemgetter 获取 'name' 键对应的值
get_name = itemgetter('name')  #返回一个可调用的对象
print(callable(get_name))
# 使用 itemgetter 获取 'age' 键对应的值
get_age = itemgetter('age')
print(callable(get_age))
# 获取指定索引的值
for person in data:
    print(f"Name: {get_name(person)}, Age: {get_age(person)}")


print("19"+"-"*60)
rows = [ 
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, 
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} 
] 
from operator import  attrgetter

rows_sortBy_fname = sorted(rows,key=itemgetter('fname'))
rows_sortBy_uid = sorted(rows,key=itemgetter('uid'))
print(rows_sortBy_fname)
print(rows_sortBy_uid)
#可以组合多个键来排序 可以使用lambda来实现这种排序  但是 lambda的性能不如 这种方式 为啥?
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname')) 
rows_by_lfname_lambda = sorted(rows,key = lambda s:(s['uid'],s['fname']))
print(rows_by_lfname)
print(rows_by_lfname_lambda)
#所有用到key的地方都可以使用这个库
min_by_uid = min(rows,key=itemgetter('uid'))
max_by_uid = max(rows,key=itemgetter('uid'))
print(min_by_uid)
print(max_by_uid)

#使用lambda作为比较的key lambda的优势就是可以函数式编程
print("20"+"-"*60)
class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

u1 = User(6)
u2 = User(2)
u3 = User(9)
users = [u1,u2,u3]
user_sort_by_userId = sorted(users,key = lambda u : u.user_id)
print(user_sort_by_userId)
#可以使用attrgetter来代替  性能好于lambda
user_sort_by_userId = sorted(users,key = attrgetter("user_id"))
print(user_sort_by_userId)

'''
6、分组的解决方式
   itertools.groupby 分组之前必须进行排序,否则分组实现出错
'''
print("21"+"-"*60)
rows = [ 
 {'address': '5412 N CLARK', 'date': '07/01/2012'}, 
 {'address': '5148 N CLARK', 'date': '07/04/2012'}, 
 {'address': '5800 E 58TH', 'date': '07/02/2012'}, 
 {'address': '2122 N CLARK', 'date': '07/03/2012'}, 
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, 
 {'address': '1060 W ADDISON', 'date': '07/02/2012'}, 
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, 
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, 
] 
#对日期进行排序
from itertools import groupby
#分组之前进行排序
rows.sort(key = itemgetter("date"))
for date,items in groupby(rows,key = itemgetter("date")):
    print(date)
    for item in items:
        print(' ',item)

'''
7、从列表中过滤出符合要求的元素
   ①-列表推导式缺点就是如果输入的元素过多,那么输出的元素可能也会过的
   ②-生成器表达式迭代的方式产生结果
   ③-使用filter函数来处理一些复杂的逻辑过滤  filter返回的是迭代器  如果想变成list 使用list进行构造
   ④-itertool.compress()接受一个可迭代的对象和一个布尔选择器序列作为输入 两个共同决定是否需要这个元素
'''
print("22"+"-"*60)
my_list = [1,4,-5,10,-7,2,3,-1]
#列表推导式
a = [n for n in my_list if n > 0]
b = [n for n in my_list if n < 0]
print(a)
print(b)

#生成器表达式
c = (n for n in my_list if n > 0)
print(c)
#注:生成器转换为列表的时候,生成器只能迭代一次
k = list(c)
print("k:{}".format(k))
for i in c:
    print(i)
#filter函数处理一些复杂的逻辑
values = ['1', '2', '-3', '-', '4', 'N/A', '5'] 
def is_int(value):
   try:
       x = int(value)
       return True
   except ValueError:
       return False
    
d = list(filter(is_int,values))
print(d)

#列表推导式 可以进行元素的替换 如果小于等于0 的替换为100
#从下面两个看出来 第一个是对结果进行判断 第二个是对筛选的范围进行过滤
a = [n if n > 0 else 100 for n in my_list]
print(a)

import math
a = [math.sqrt(n) for n in my_list if n > 0]
print(a)

#使用compress进行过滤
addresses = [ 
 '5412 N CLARK', 
 '5148 N CLARK', 
 '5800 E 58TH', 
 '2122 N CLARK' ,
 '5645 N RAVENSWOOD', 
 '1060 W ADDISON', 
 '4801 N BROADWAY', 
 '1039 W GRANVILLE'
] 
counts = [0,3,10,4,1,7,6,1]
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
a = list(compress(addresses,more5))
print(a)

'''
8、从字典中提取一部分元素
   ①-字典推导式  性能相对较快 通常比一般的构造函数来得效率比较高
'''
print("23"+"-"*60)
prices = { 
 'ACME': 45.23, 
 'AAPL': 612.78, 
 'IBM': 205.55, 
 'HPQ': 37.20, 
 'FB': 10.75 
} 
#过滤价格大于200的
p1 = {key:value for key,value in prices.items() if value > 200}
print(p1)
tech_names = {'AAPL','IBM','HPQ','MSFT'}
#字典key在tech_names中的
p2 = {key:value for key,value in prices.items() if key in tech_names}
print(p2)

'''
9、将名称映射到序列元素上,使用具名得tuple
   一方面使代码更容易阅读,
   另一方面如果元组后期添加元素的话,使用索引的话导致不正确,例如从数据库中读取表的数据，如果表增加字段，那么索引的值得重新调整
'''
print("24"+"-"*60)
from collections import namedtuple
Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('jjj@qq.com','2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
#namedtuple和元组一样具备类似得功能
print(len(sub))
addr,joined = sub
print(addr)
print(joined)

'''
10、同时对数据做换算和运算
    利用生成器表达式来进行换算  节省内存的使用
'''
print("25"+"-"*60)
nums = [1,2,3,4,5]
s = sum(x*x for x in nums)
print(s)
#参考下面的做法,使用list作为临时的参数,增加了一个临时的list的开销,而且这个list只使用一次就作废了
s = sum([x*x for x in nums])
print(s)

import os
#获取对应文件目录下的子文件和子目录 不递归获取
files = os.listdir('./pychart')
print(files)
if any(name.endswith('.py') for name in files):
    print("There be python")
else:
    print("sorry no python")

portfolio = [ 
 {'name':'GOOG', 'shares': 50}, 
 {'name':'YHOO', 'shares': 75}, 
 {'name':'AOL', 'shares': 20}, 
 {'name':'SCOX', 'shares': 65} 
]
min_price = min(s['shares'] for s in portdolio) 
max_price = max(s['shares'] for s in portdolio) 
print(min_price)

'''
11、将多个映射合并为单个映射
    ChainMap 可以接受多个映射,但是在逻辑上表示为一个映射,但是这些多个映射并不会合并在一起
    只是重新定义了字典的一些操作
    如果有重复的键,只会取第一个映射的键
    修改映射的操作也总会出现第一个映射上
'''
print("26"+"-"*60)

a = {'x':1,'z':3}
b = {'y':2,'z':4}
from collections import ChainMap
c = ChainMap(a,b)
print(c)
print(type(c))
print(c['x'])
print(c['y'])
print(c['z'])

#具有字典的一些公共操作
print(len(c))
print(list(c.keys()))
print(list(c.values()))

c['z'] = 10
c['w'] = 40
print(c)

'''
为啥不使用字典的update()方法将多个字典合并到一起
'''
a = {'x':1,'z':3}
b = {'y':2,'z':4}

mergerd = dict(a)
mergerd.update(b)
print(mergerd)
print(a)
print(b)

#对原始a的修改并不会 反应到mergerd中
a['x'] = 100
print(a)
print(mergerd)


if __name__ == "__main__":
    print("main"+60*"-")
    #print("平均值是{}".format(drop_first_last([1,2,3,4,5])))
    #search_in_file()
    