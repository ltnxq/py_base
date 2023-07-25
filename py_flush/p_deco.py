'''
1、讲解装饰器的使用,能把被装饰的函数替换成其他函数
'''

def deco(func):
    def inner():
        print("running inner")
    return inner

@deco
def target():
    print("running targrt()")

target()
print(target)

'''
2、装饰器函数的另一个特性是 函数装饰器在导入模块时立即执行,而被装饰的函数只在明确调用时运行
   如果在其他的py模块导入 p_deco模块的化  装饰器函数会立即运行  
'''

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

'''
3、装饰器一般用法  
   ①  装饰器通常在一个模块中定义 然后应用到其他模块中的函数上。
   ②  大多数装饰器会在内部定义一个函数，然后将其返回
'''

if __name__ == "__main__":
    main()