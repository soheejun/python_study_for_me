# sequence in python standard library 
# : 1-1. container sequence: list, tuple, collections, deque --> several dtypes
# : 1-2. flat sequence: str, bytes, bytearray, memoryview, array.array --> only one dtypes 
# : 2-1. mutable sequence: list, bytearray, array.array, collections, deque, memoryview 
# : 2-2. immutable sequence: tuple, str, bytes 


# list comprehension 
symbols = '$%^&*'
codes = [ord(symbol) for symbol in symbols]
print(codes)


# list comprehension is faster than map() + filter() + lambda 
# list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)


# zip() can not return combination
tshirts  = list(zip(colors, sizes))
print(tshirts)


# generator expression 
# : same grammar with list comprehension / use ( ) instead of [ ]
# : not create list just create one item at time
# memory usage: list comprehension > generator expression 
a = tuple(ord(symbol) for symbol in symbols)
print(a)
import array 
a = array.array('I', (ord(symbol) for symbol in symbols))  # array.array(dtypes, data) 
print(a)

for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes):
    print(tshirt)


# tuple 
# can use tuple as record --> size, order is matter 
# tuple unpacking 
lax_coordinates = (33.9425, -118.409056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '3119849'), ('BRA', 'CEjhfgs'), ('ESP', 'slkrjfgals')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)  # unpacking: % format process each tuple's item as field 

for country, _ in traveler_ids:  # unpacking
    print(country) 

latitude, longtitude = lax_coordinates  # unpacking: parallel assignment 
print(latitude, longtitude)

import os 
_, filename = os.path.split('/home/sweet/home.py')  # get return value through unpacking 
print(filename)

# unpacking with star(*)
t = (20, 8) 
quotient, remainder = divmod(*t) # unpacking: with * 
print(quotient, remainder)

# star takes remain returns (only one star in one line for parallel assignment)
a, b, *rest = range(5)
print(a, b, rest)

a, *body, c, d = range(5) 
*head, b, c, d = range(5)
print(body, head)


# collections.namedtuple(class name, field name)
# same memory usage with tuple (efficient)
# tuple is not enough for record 
import collections 
City = collections.namedtuple('City', 'name country population coordinate')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)  # can access using field name 
print(tokyo[1]) # can access using position 

# other attributes in namedtuple 
# _fields, _make(), asdict()
print(City._fields) 

LatLong = collections.namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', "IN", 21.935, LatLong(28.61, 77.20))
delhi = City._make(delhi_data)  # = City(*delhi_data) 
print(delhi)
print(delhi._asdict()) # return collections.OrderedDcit 


# list (mutable) vs tuple (immutable)
# tuple offer every list's method except add, delete, reversed (reversed(tuple) does not use __reversed__())





