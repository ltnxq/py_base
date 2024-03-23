'''
利用装饰器来构造一个类型系统
效率更高 可以参考其他章节的学习
'''

class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
 
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

# Decorator for applying type checking
def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)
    super_set = cls.__set__
 
    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expected ' + str(expected_type))
        super_set(self, instance, value)
 
    cls.__set__ = __set__
    return cls
 
 
# Decorator for unsigned values
def Unsigned(cls):
    super_set = cls.__set__
 
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super_set(self, instance, value)
 
    cls.__set__ = __set__
    return cls
 
 
# Decorator for allowing sized values
def MaxSized(cls):
    super_init = cls.__init__
 
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)
 
    cls.__init__ = __init__
 
    super_set = cls.__set__
 
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super_set(self, instance, value)
 
    cls.__set__ = __set__
    return cls
 
 
# Specialized descriptors
@Typed(int)
class Integer(Descriptor):
    pass
 
 
@Unsigned
class UnsignedInteger(Integer):
    pass
 
 
@Typed(float)
class Float(Descriptor):
    pass
 
 
@Unsigned
class UnsignedFloat(Float):
    pass
 
 
@Typed(str)
class String(Descriptor):
    pass
 
 
@MaxSized
class SizedString(String):
    pass


def check_attributes(**kwargs):
    def decorate(cls):
        #在类上设置一些属性 对象访问属性的时候就是访问对应的类属性
        for key ,value in kwargs.items():
            if isinstance(value,Descriptor):
                value.name = key
                setattr(cls,key,value)
            else:
                t = value(key)
                setattr(cls,key,t)
        return cls
    return decorate

@check_attributes(name=SizedString(size=8),shares=UnsignedInteger,price=UnsignedFloat)
class Stock_v3:
    def __init__(self,name,shares,price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

print("1"+"-"*60)

s = Stock_v3('ACME',52,91.4)
# 类型报错
#s.price = -90


'''
实现非递归的访问者模式
'''

print("2"+"-"*60)

import types

class Node:
    pass

class Number(Node):
    def __init__(self,value) -> None:
       self.value = value

class NodeVisitor:
    def visit(self,node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last,types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last,Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result
    
    def _visit(self,node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self,methname,None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
    
    def generic_visit(self,node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
    

class UnaryOperator(Node):
    def __init__(self,operand) -> None:
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self,left,right) -> None:
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass
class Sub(BinaryOperator):
    pass
class Mul(BinaryOperator):
    pass
class Div(BinaryOperator):
    pass
class Negate(UnaryOperator):
    pass

'''
yield 版本
'''
class Evaluator(NodeVisitor):
    def visit_Number(self,node):
        return node.value
    def visit_Add(self,node):
        yield (yield node.left) + (yield node.right)    
    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)    

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)    

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)
 
    def visit_Negate(self, node):
        yield -(yield node.operand)
    
t1 = Add(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)

e = Evaluator()
print(e.visit(t1))


'''

'''
print("3"+"-"*60)

class Spam: 
 def __init__(self, name): 
  self.name = name 
# Caching support
import weakref
_spam_cache = weakref.WeakValueDictionary() 
def get_spam(name): 
 if name not in _spam_cache: 
    s = Spam(name) 
    _spam_cache[name] = s 
 else: 
    s = _spam_cache[name] 
    return s
 
a = get_spam('foo')
b = get_spam('foo')
print(a is b)