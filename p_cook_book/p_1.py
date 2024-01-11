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
'''

if __name__ == "__main__":
    print("main------------------------------------------")
    #print("平均值是{}".format(drop_first_last([1,2,3,4,5])))
    #search_in_file()
    