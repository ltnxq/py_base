'''
函数相关知识
'''
print("1"+"-"*60)

'''
* 参数的用法
'''
def avg(first,*rest):
    print(type(rest))  #rest的类型是元组
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1,2))
print(avg(1,2,3,4))

'''
** 参数的用法
关键字参数就是 参数名称=参数值 的形式的入参
'''
print("2"+"-"*60)

def print_info(**kwargs):
    print(type(kwargs))  #kwargs的类型是dict
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_info(name = 'Alice',age = 30,city = 'New York')


'''
函数特定位置只接受关键字参数的形式
'''
print("3"+"-"*60)
#也就是*之后的参数只能按照关键字参数的形式给出
def recv(maxsize,*,block):
    pass
try:
 recv(1024,block=True)
except Exception as e:
   print(e) 

'''
接受变参+关键字参数的函数入参形式
'''
print("4"+"-"*60)
def mininum(*values,clip = None):
   m = min(values)
   if clip is not None:
      m = clip if clip > m  else m
   return m
print(mininum(1,5,2,-5,10))
print(mininum(1,5,2,-5,10,clip=0))

'''
2、将元数据信息附加到函数上
'''
print("5"+"-"*60)
def add(x:int,y:int) -> int:
   return x + y
print(help(add))
print(add.__annotations__)


'''
3、从函数中返回多个值
'''
print("6"+"-"*60)
def myfun():
   #返回的是元组的形式的返回值
   return 1,2,3
a,b,c = myfun()
print(a,b,c)

a = (1,2)
#通过逗号可以创建一个元组对象
b = 1,2
print(a)
print(b)
print(type(a))
print(type(b))

'''
定义带有默认参数的函数
'''
print("7"+"-"*60)
def spam(a,b=42):
   print(a,b)
spam(1)
spam(1,2)

'''
默认参数是可变容器的话 
为啥使用b = None 而不是使用可变参数 [] ?
'''
def spam1(a,b = None):
  if b is None:
     b = []
  pass

'''
第一点注意
默认参数在函数定义的时候被绑定为一个对象
'''
print("8"+"-"*60)

x = 43
def spam2(a,b = x):
   print(a,b)
spam2(1)
x = 23  # 23不会改变默认参数
spam2(1)

'''
第二点注意
默认参数的绑定必须是不变对象 int 字符串 None True等 而不是 [] list这些可变对象
'''
print("9"+"-"*60)

def spam3(a,b=[]):
   print(b)
   return b
x = spam3(1)
x.append(1)
x.append('hello')

#再次调用spam3的时候发现默认参数已经改变了
spam3(1)

#将b的默认参数用None来代替
print("10"+"-"*60)
def spam4(a,b=None):
   if b is None:
      b = []
   print(b)
   return b

x = spam4(1)
x.append(1)
x.append('hello')
spam4(1)

'''
最佳的做法是用一个默认值去代替None 例如no_value
'''
_no_val = object()
def spam5(a,b=_no_val):
   if b is _no_val:
      b = []
   print(b)
   return b

'''
4、定义匿名函数或者内联函数
'''
print("11"+"-"*60)
add = lambda x,y : x+y
a =  add(2,3)
b= add('hello',"word")
print(a)
print(b)

'''
lambda 匿名函数是在运行的时候绑定变量的值
       如果想要在定义的时候进行绑定的话,那么可以使用默认参数
'''
print("12"+"-"*60)
x = 10
a = lambda y : x + y
x = 20 
b = lambda y : x + y

print(a(10))  #30  运行的时候 x 绑定为20
print(b(10))

#下面通过默认参数的形式进行绑定
print("13"+"-"*60)
x = 10
a = lambda y,x=x:x+y
x = 20
b = lambda y,x=x:x+y
print(a(10))
print(b(10))

'''
5、改变原始函数的参数个数,类似于c++ bind的功能
   partial 返回了一个新的可调用对象
'''
print("14"+"-"*60)
from functools import partial
#接受4个参数
def spam6(a,b,c,d):
   print(a,b,c,d)
spam6(1,2,3,d=9)

#a 默认是1 现在s1是三个参数的函数
s1 = partial(spam6,1)
s1(2,3,4)
s1(4,5,6)
#s2 三个参数的函数 d 为42
s2 = partial(spam6,d = 42)
s2(1,2,3)

#s3为接受一个参数的函数
s3 = partial(spam6,1,2,d=43)
s3(87)

'''
patial 改变参数的个数 用作key的比较规则上 sort min max等
       key只接受一个参数作为入参
'''
print("15"+"-"*60)
import math
def distance(p1,p2):
   x1,y1 = p1
   x2,y2 = p2
   return math.hypot(x2-x1,y2-y1)

points = [(1,2),(3,4),(5,6),(7,8)]
#points 对 到 固定点的距离排序
pt = (3,4)

# partial将两个参数的函数 变成一个参数的可调用对象 那么满足key的比较规则
a = sorted(points,key=partial(distance,pt))
print(a)

'''
6、python中函数闭包的使用 类似于js的闭包 函数中嵌套函数 
   嵌套函数有外层的上下文环境
'''
print("16"+"-"*60)
def outer_func(x):
   def inner_func(y):
      return x + y
   return inner_func

#创建闭包
closure = outer_func(103)
result = closure(5)
print(result)

'''
7、在回调函数中携带额外的状态
   三种方式-类、闭包、partial带额外参数
'''
print("17"+"-"*60)
def apply_async(func,args,*,callback):
   result = func(*args)
   #callback 是个回调函数 可以是用户提供 
   #此种在事件监听 或者 其他异步回调中经常用到
   callback(result)

#print_result 只接受一个参数并没有和其他变量进行交互 无状态的函数
def print_result(result):
   print('Got:',result)
def add(x,y):
   return x + y

apply_async(add,(1,2),callback=print_result)
apply_async(add,('hello ','world'),callback=print_result)

'''
有状态的可调用对象 使用类的字段属性来达到要求
'''
class ResultHandler:
  def __init__(self) -> None:
     self.seq = 0
  def handler(self,result):
     self.seq += 1
     print('[{}] Got: {}'.format(self.seq,result))

r = ResultHandler()
apply_async(add,(3,5),callback=r.handler)
apply_async(add,('sss','aaa'),callback=r.handler)

'''
使用函数闭包也可以得到有状态的可调用对象
nonlocal 修饰的变量表示非局部的变量
'''
def make_handler():
   seq = 0
   def handler(result):
      nonlocal seq
      seq += 1
      print('[{}] Got: {}'.format(seq,result))
   return handler
handler = make_handler()
apply_async(add,(9,5),callback=handler)
apply_async(add,('fff','ssss'),callback=handler)

'''
通过额外的参数来达到效果也可以
然后使用partial来转换为符合要求的函数形式
'''
class SeqNo:
   def __init__(self) -> None:
      self.seq = 0

def handler(result,seq):
   seq.seq += 1
   print('[{}] Got: {}'.format(seq.seq,result))

seq = SeqNo()
apply_async(add,(10,29),callback=partial(handler,seq = seq))
apply_async(add,('hello ','world'),callback=partial(handler,seq = seq))

'''
装饰器的使用
'''
import time
print("18"+"-"*60)

def timeit(func):
   def wrapper(*args,**kwargs):
      start_time = time.time()
      result = func(*args,**kwargs)
      end_time = time.time()
      print("Function {} took {:.2f} seconds to execute".format(func.__name__, end_time - start_time))
      return result
   return wrapper

@timeit
def myfun():
   time.sleep(1)
   print('Function executed')

myfun()



'''
8、内联函数的使用
'''
from queue import Queue
from functools import wraps

print("19"+"-"*60)

class Async:
   def __init__(self,func,args) -> None:
      self.func = func
      self.args = args

def inlined_async(func):
   @wraps(func)
   def wrapper(*args):
      #返回一个生成器
      f = func(*args)
      result_queue = Queue()
      result_queue.put(None)
      while True:
         result = result_queue.get()
         try:
            # 第一次为None的时候开启了生成器的执行  
            a = f.send(result)
            apply_async(a.func,a.args,callback=result_queue.put)
         except StopIteration:
            break
   return wrapper

@inlined_async
def test():
   print("test begin........")
   r = yield Async(add,(2,3))
   print(r)
   r = yield Async(add,('hello','world'))
   print(r)
   for n in range(10):
      r = yield Async(add,(n,n))
      print(r)
   print('Goodbye')

test()

'''
9、访问定义在闭包内的变量
'''
def sample():
   n = 0

   #Closure function
   def func():
      print('n=',n)
   
   def get_n():
      return n
   def set_n(value):
      nonlocal n
      n = value
   
   #给闭包函数添加属性 函数当成是一个对象去处理
   func.get_n = get_n
   func.set_n = set_n
   return func

print("20"+"-"*60)
f = sample()
f()
f.set_n(10)
f()
print(f.get_n())