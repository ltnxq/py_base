'''
使用抽象基类来实现策略模式
'''

from abc import ABC,abstractclassmethod
from collections import namedtuple
Customer = namedtuple('Customer','name fidelity')
class LineItem:
    def __init__(self,product,quantity,price) -> None:
       self.product = product
       self.quantity = quantity
       self.price = price
    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self,customer,cart,promotion=None) -> None:
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    def total(self):
        if not hasattr(self,'__total'):
            self.__total = sum(item.total() for item in self.cart)
            return self.__total
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    def __repr__(self) -> str:
        fmt = '<Order total:{:.2f} due: {:.2f}>'
        return fmt.format(self.total(),self.due())

'''
1、使用ABC 把Promotion 定义为一个抽象基类
'''    
class Promotion(ABC): #策略  抽象基类
    @abstractclassmethod
    def discount(self,order):
        pass
class FideLityPromo(Promotion): #第一个具体策略
    def discount(self,order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    def discount(self,order):
        discount = 0
        for item  in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion):
    def discount(self,order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
joe = Customer('John Doe', 0) 
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5), LineItem('apple', 10, 1.5),LineItem('watermellon', 5, 5.0)]

print(Order(joe, cart, FideLityPromo()))
print(Order(ann, cart, FideLityPromo()))

banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, BulkItemPromo()) )

long_order = [LineItem(str(item_code), 1, 1.0)for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()) )
print(Order(joe, cart, LargeOrderPromo()))
