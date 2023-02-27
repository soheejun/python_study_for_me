# python array is light like as c array 
# each element in array is saved as typecode 
# array.array(typecode, initializer)
# array.tofile(), 
# array.fromfile() is much faster than write and read as text 
# (pickle.dump() is fast like array.tofile())
from array import array 
from random import random 

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp  = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)
print()

# class memoryview() --> share memory sequence 
# : generalization version of numpy array 
# : can handle array slice while not copying bytes (efficient for big data) 
import array 
numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

# cast type without moving bytes (memv object share same memory)
memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers) 

print(id(numbers))
print(id(memv))
print(id(memv_oct))
print()


# numpy library 
import numpy 
a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)

# add axis by assign shape 
a.shape = 3, 4
print(a)
print(a[2])
print(a[:, 1])
print(a.transpose)
