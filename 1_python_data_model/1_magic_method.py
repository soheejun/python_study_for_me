# magic_method
# : ex) __getite__(), __len__() --> called 'dunder-len'
# : usally magic method is for interpreter not user 
# : sometimes interpreter call C things to get length ... for speed 
# : len() just read C things size field not call __len__() because it is faster 

import collections
# collections.namedtuple(type_name, field_names, *, rename=False)
# : factory function for tuples with named fields 
# : similar with database record and dictionary
# : can access by key and index  
# same function different definition 
Card = collections.namedtuple('Card', ['rank', 'suit'])
Card = collections.namedtuple('Card',  'rank suit')
Card = collections.namedtuple('Card', 'rank, suit')

class FrenchDeck: # implicitly inherit 'object' in python3
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# same function different input 
beer_card1 = Card('7', 'diamonds')
beer_card2 = Card(**{'rank':'7', 'suit':'diamonds'})
print(beer_card1)
print(beer_card2)
print()


# how special method works 
# special methods make FrenDeck operates like python sequence 
deck = FrenchDeck()
print(len(deck)) # __len__()
print(deck[0]) # __getitem__()
print(deck[-1]) # __getitem__(0 
print()


# can use indexing, slicing,  since FrenchDeck's __getitem__() is operated with indexing (slicing) []
# indexing with python standard library 
from random import choice 
print(choice(deck))
print(choice(deck))
print()

print(deck[:3])
print(deck[12::13])
print()


# can iterate with __getitem__() 
for card in deck: print(card)
print()

for card in reversed(deck): print(card)


# only iteratable can works with in 
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)


# sorting 
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0) # weight
def spades_high(card):
    # FrenchDeck.ranks --> ['2', '3', ....'K', 'A']
    # list.index(value) --> index of value in list 
    rank_value = FrenchDeck.ranks.index(card.rank) 
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high): # sorted(iterable, key: function take one argument)
    print(card)

# shuffle 
# from random import shuffle
# shuffle(deck) # does not work --> FrenchDeck is immutable 


# magic methods for numerical operation (+, -, *, /) 
from math import hypot # hypotenuse

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 
    
    def __repr__(self): 
        return 'Vector(%r, %r)' % (self.x, self.y) 
        # %r vs %s 
        # : %r: object representation / %s: string representation 
        # ex) 
        # import datetime
        # d = datetime.date.today()
        # str(d) --> '2023-01-02'
        # repr(d) --> 'datetime.date(2023, 1, 2)'

    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x 
        y = self.y + other.y 
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar) 


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v = Vector(3, 4)
print(abs(v))

print(v * 3)

# empty list == False
# : because when __bool__ is not implemented __bool__() call __len__()
# : so if len(x) == 0 , return False
print(bool([]))
print(bool([1,2]))


