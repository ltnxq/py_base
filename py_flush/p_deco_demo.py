from p_deco import clock
import time
import functools

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

#lru last recently used 这个装饰器在优化递归的方法中有很大的作用
'''
因为lru_cache使用字典存储结果 而且键根据调用时传入的定位参数和关键字参数创建 所以被lru_cache装饰的函数,它的所有参数都必须是可散列的。
有两个参数 maxsize = 128 ,指定缓存大小,如果缓存满了旧的结果会被扔掉
          typed = True  不同参数类型得到的结果分开保存 比如-1和1.0就是不同的参数
'''
@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


'''
内置装饰器 singleleddispatch 的使用
不同的参数类型 对应不同的函数  有java的函数重载的味道
'''
from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}<pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n','<br>\n')
    return '<p>{0}<p>'.format(content)

#numbers.Integral 是 int的虚拟超类
@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner+'</li>\n</ul>'


if __name__ == '__main__':
    # print('*' *40,'Calling snooze(.123)')
    # snooze(.123)
    # print('*'*40,'Calling factorial(6)')
    # print('6!=',factorial(6))
    print(fibonacci(6))

