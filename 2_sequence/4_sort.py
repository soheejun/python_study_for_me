# list.sort(reverse bool), key(func)) : inplace operation (does not make copy), return None 
# sorted(reverse(bool), key(func)): not inplace operation, return sorted object 

fruits = ['grape', 'raspberry', 'apple', 'banana'] 
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len)) 
print(fruits.sort(key=len))
print(fruits)


# bisect(haystack, needle) : return index where the element (needle) will be inserted in sorted list (haystack) 
# bisect.bisect(lo, hi): insert needle in lo~hi of haystack (lo=0, hi=len(haystack))
# bisect.bisect_left(lo, hi): if the needle is same with element in haystack, needle is inserted in front of existed element 
import bisect 
import sys

haystack = [1,4,5,6,8,12,15,20]
needles = [0,3,1,2,5,12,13]

row_fmt = '{0:2d} @ {1:2}  {2}{0:<2d}'

def demo(bisect_fn):
 for needle in needles:
     position = bisect_fn(haystack, needle)
     offset = position * '   |'
     print(row_fmt.format(needle, position, offset))

print('DEMO: ', bisect.bisect)
print('haystack ->', ' '.join('%2d'% n for n in haystack))
demo(bisect.bisect)


def grade(score, breakpoints=[60,70,80,90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 88 , 77, 65]])

# biserc.insort(seq, item, lo, hi) : insert item in seq (inplace)
import random 

size = 7
my_list = [] 
for i in range(size):
    new_item = random.randrange(size * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)


