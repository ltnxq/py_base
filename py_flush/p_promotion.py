'''
利用装饰器注册对应的策略函数
'''
promos = []
#一般都是原封不动返回这个函数
def promotion_registry(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion_registry
def fidelity_promo(order):
    """ 为积分达到1000或以上的顾客提供5%的优惠"""
    return order.total() * .05 if order.customer.fidelity >=1000 else 0

@promotion_registry
def bulk_item_promo(order):
    """单个商品为20个或者以上时提供0.1折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion_registry
def largeOrder_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promotion(order):
    return max(promo(order) for promo in promos)