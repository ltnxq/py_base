
'''
定义一个属性可由用户修改的装饰器
'''
print("1"+"-"*60)

from functools import wraps,partial
import logging

def attach_wrapper(obj,func = None):
    print(obj)
    if func is None:
        #创建一个新的可调用对象  partial的作用  返回的新的函数  作为包装函数
        return partial(attach_wrapper,obj)
    setattr(obj,func.__name__,func)
    return func

def logged(level,name=None,message = None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            return func(*args,**kwargs)
        # set_message 和 set_level 以属性的形式附加到包装器的函数上
        # 每个函数都允许对nonlocal变量进行赋值操作

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
        
        return wrapper
        
    return decorate

@logged(logging.DEBUG)
def add(x,y):
    return x + y

@logged(logging.CRITICAL,'example')
def spam():
    print('Spam!')

print(add.set_message)
print(spam.set_level)    

logging.basicConfig(level=logging.DEBUG)
add(2,3)

add.set_message('Add called')
add(2,3)

add.set_level(logging.WARNING)
add(2,3)

