x=5
y=6
z=x+y
print(z)

#knowing the type of a varriable
x=5
y="john"
print(type(x))
print(type(y))

#varriables name are case sensitive
a=4
A="danish"
print(a)
print(A)

#Python allows you to assign values to multiple variables in one line:
#Note: Make sure the number of variables matches the number of values, or else you will get an error
x , y , z = "orange", 5, 7
print(x)
print(y)
print(z)

#And you can assign the same value to multiple variables in one line:
x = y = z = 4
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
heroes = ["Shaktiman", "Juniorjee", "Spiderman"]
x , y, z = heroes
print(x)
print(y)
print(z)

#In the print() function, you output multiple variables, separated by a comma:
x = "Danish "
y = "Hey "
z = "Whatsup "
print(x, y, z)
print(x +  y  +  z)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
'''
x = 5
y = "john"
print(x + y)
'''


'''Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.'''
def myFunc():
    global x
    x = "Danish"

myFunc()

print(" Hustle  " + x)

'''To change the value of a global variable inside a function, refer to the variable by using the global keyword:'''
x = "awesome"
def myFunc():
    global x
    x = "fantastic"
    
myFunc()
print("python is " + x)



