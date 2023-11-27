'''
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
'''
#* Note: Set items are unchangeable, but you can remove items and add new items.

#creating a set
thisset = {"apple", "Danish", "Heyyy" }
print(thisset)
#Sets are unordered, so you cannot be sure in which order the items will appear.
'''
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
'''

'''
Duplicates Not Allowed
Sets cannot have two items with the same value.

Example
Duplicate values will be ignored:
'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#o determine how many items a set has, use the len() function.
thisset={"danish", 5, "danish"}
print(len(thisset))

'''
A set can contain different data types:
Example
A set with strings, integers and boolean values:
'''

set1 = {"Danish", True, 40, "male"}
print(set1)
print(type(set1))

'''
Access Items
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
'''

#Loop through the set, and print the values:
thisset = {"apple", "Danish0," "Hey"}
for x in thisset:
    print(x)

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "Cherry"}
print("banana" in thisset)