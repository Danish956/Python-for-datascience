'''
Access Items
List items are indexed and you can access them by referring to the index number:
'''
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

'''
Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
'''
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

'''
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
'''
#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#By leaving out the end value, the range will go on to the end of the list:
#Example
#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

'''
Check if Item Exists
To determine if a specified item is present in a list use the in keyword:
Example
Check if "apple" is present in the list:
'''

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


