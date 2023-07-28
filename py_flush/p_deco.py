'''
装饰器的特性:
    1、能把被装饰的函数替换成其他函数
    2、装饰器函数的另一个特性是 函数装饰器在导入模块时立即执行,而被装饰的函数只在明确调用时运行
       如果在其他的py模块导入 p_deco模块的化  装饰器函数会立即运行  
    3、装饰器一般用法  
      ①  装饰器通常在一个模块中定义 然后应用到其他模块中的函数上。
      ②  大多数装饰器会在内部定义一个函数，然后将其返回
'''
import time

# 1 功能展示
def deco(func):
    def inner():
        print("running inner")
    return inner

@deco
def target():
    print("running targrt()")

target()
print(target)


# 2 功能展示 
registry = []

def register(func):
    print("running register(%s)"%func)
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")

@register
def f2():
    print("running f2()")

@register
def f3():
    print("running f3()")

def main():
    print("running main()...")
    print('registry->',registry)
    f1()
    f2()
    f3()

#3 功能展示
#这个装饰器有点代理切面的味道,函数功能不变只是在头尾加上时间的计时或者是一些记录的日志
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs]%s(%s)->%r'%(elapsed,name,arg_str,result))
        return result
    return clocked

#4 一个参数化的注册装饰器
registry= set()

def register1(active = True):
    def decorate(func):
        print('running register1(active=%s)->decorate(%s)'%(active,func))
        if active:
          registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register1(active=False)
def f1():
    print("running f1()")

@register1()
def f2():
    print("running f2()")

def f3():
    print("running f3()")

#5参数化clock装饰器 
'''
①clock_param 是参数化装饰器工厂函数
②decorate 是真正的装饰器
③clocked 包装被装饰的函数
'''
DEFAULT_FMT = '[{elapsed:08f}s] {name} ({args})->{result}'
def clock_param(fmt = DEFAULT_FMT):
   def decorate(func): 
        def clocked(*args):
            t0 = time.perf_counter()
            _result = func(*args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ','.join(repr(arg) for arg in args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
   return decorate
