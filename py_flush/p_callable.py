import random

#演示一个类定义call方法成为可调用的一个对象
class BingoCage:
    def __init__(self,items) -> None:
        self._items = list(items)
        #random.shuffle 将原列表进行打乱，但是不产生新的list对象
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")
    def __call__(self):
        return self.pick()
        
bingo = BingoCage(range(3))
print(bingo())
print(bingo.pick())

print(callable(bingo))