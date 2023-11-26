#Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = 'danish'
print(a)

#You can assign a multiline string to a variable by using three quotes:
#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings in Python are arrays of bytes representing unicode characters.
a = "Hello World"
print(a[0])
print(a[6])


#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)


#The len() function returns the length of a string:
a = "Hey Danish "
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
#Check if "free" is present in the following text:
txt = "The best things in life are free"
print("free" in txt)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best thing in life are free"
print("expensive" not  in txt)