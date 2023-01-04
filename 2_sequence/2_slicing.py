# every sequence in python can be sliced 

l = [10, 20, 30, 40, 50, 60]
print(l[:2])
print(l[2:])

# seq[start:stop:step] call seq.__getitem__(slice(start, stop, step))
s = 'bicycle'
print(s[::3])
print(s[::-1]) # think as circle (back to begin)
print(s[::-2])

# slice()
three = slice(0, 3)
print(s[three]) # = s[:3]


# manipulate sequence 
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
l[2:5] = [100] # l[2:5] = 100 does not work --> if left is the slice, right should be iteratable object 
print(l)


