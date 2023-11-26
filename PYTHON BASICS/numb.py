#Type Conversion:-converting from one data type to another data types.
x = 1
y = 2.8
z = 1j #Note: You cannot convert complex numbers into another number type.

# converting from int to float
a = float(x)
#cinverting from float to int
b = int(y)
#converting from complex number to float
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

'''Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:'''
import random
print(random.randrange(1, 10))