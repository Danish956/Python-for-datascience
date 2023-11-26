#Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello Danish"
print(b[2:5])

#By leaving out the start index, the range will start at the first character:
#Get the characters from the start to position 5 (not included):
b = "Hello Danish"
print(b[:5])

#By leaving out the end index, the range will go to the end:
#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

b = "Hello World"
print(b[-5:-2])