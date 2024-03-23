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


print("2"+"-"*60)

'''
装饰器是随着程序的执行而加载的,不是调用函数也会自动加载
装饰器也是利用了函数闭包原理
'''
def makeBold(fn):
    print("BBBBB"*5)
    def wrapped():
        print("bbbbb"*5)
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeItalic(fn):
    print("IIIII"*5)
    def wrapped():
        print("iiiiii" * 5)
        return "<i>" + fn() + "</i>"
    return wrapped
 
#2.装饰器的使用，直接@加上函数名的形式，放到需要装饰的函数头上即可。
@makeBold  #效果等同于test_Bold=makeBold(test_Bold)，装饰器放在一个函数上，相当于将这个函数当成参数传递给装饰函数
def test_Bold():
    print("test_Bold"*5)
    return "this is the test_Bold"
 
@makeItalic #效果等同于test_Italic=makeItalic(test_Italic)，装饰器放在一个函数上，相当于将这个函数当成参数传递给装饰函数
def test_Italic():
    print("test_Itali" * 5)
    return "this is the test_Italic"

#-----------下面对函数进行调用-----------------
print(test_Bold)  # 函数是对象,现在指向的是<function makeBold.<locals>.wrapped at 0x000001FEC204FCA0>对象 


'''
多个装饰器修饰函数的时候,从内向外依次执行
'''
print("3"+"-"*60)

@makeBold   #注意2.其效果等同于test_B_I=makeBold( makeItalic(test_B_I) )
@makeItalic #注意1.其效果等同于test_B_I=makeItalic(test_B_I)
def test_B_I():   
    print("test_B_I"*5)
    return "this is the test_B_I"

test_B_I()



