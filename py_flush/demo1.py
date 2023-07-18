import collections
from random import choice
Card = collections.namedtuple("Card",['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards =[Card(rank,suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,position):
        return self._cards[position]
    
deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])

print(choice(deck))
print(choice(deck))
print(choice(deck))

print("slice operator")
print(deck[:3])
print(deck[12:13])

#正向迭代
print("----------------------------------------")
for  card in deck:
    print(card)
#反向迭代
print("----------------------------------------")
for card in reversed(deck):
    print(card)

print("anthor___________________________________________________")
from math import hypot
class Vector:
    def __init__(self,x=0,y=0) -> None:
            self.x = x
            self.y = y
    def __repr__(self) -> str:
         return "Vector(%r,%r)"%(self.x,self.y)
    def __abs__(self):
         return hypot(self.x,self.y)
    def __bool__(self):
         return bool(abs(self))
    def __add__(self,other):
         x = self.x + other.x
         y = self.y + other.y
         return Vector(x,y)
    def __mul__(self,scalar):
         return Vector(self.x*scalar,self.y*scalar)