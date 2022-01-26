# ways to add and removing an elment in a list

a = [1, 2, 3, 4, 5]

#how to add to a list
a.append(6)
print(a)

a.insert(6, 7)
print(a) #6 is the index at which element 7 should be inserted

a.extend([8])
print(a)


#how to remove from a list

a.pop(7)
print(a)
# For .pop() we need to know the index of the element we are trying to remove 

a.remove(7)
print(a)
# For  .remove() we need to know the element we want to remove we could specify the index

a.remove(a[5])
print(a)
# For  .remove() we need to know the element we want to remove we could specify the index

del a[4]
print(a)

#Return the length of a list

print(len(a))

# Remove elements in a list before or afte a specific index

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(Numbers[:4])        #To print elements between indices 0 and 3
print(Numbers[4:])        #To print elements between indices 3 till the end
print(Numbers[0:10:2])    #To print every 2nd element in this case odd numbers 
print(Numbers[1:10:2])    #To print every 2nd element in this case even numbers 


# what is the differance between list and a set

myList = ["Gugu", "Thenji", "Gugu", "Khonzi", 4]
 
mySet = {"Gugu", "Thenji", "Gugu", "Khonzi", 4}

mySet2 = {"Khonzi", "Gugu", "Thenji", "Gugu", "Thenji", "Khonzi", 4, 4, 4}

print(myList)
print(mySet)
print(mySet2)


"""

-Lists are indexed and sets are not
-Lists can have repetition and sets cant 
-Lists are mutable and tuples are not
-However both can homogeneous or hetrogeneous 

When you want an unordered collection of unique elements, use a set. 
(For example, when you want the set of all the words used in a document).

When you want to collect an immutable ordered list of elements, use a tuple. 
(For example, when you want a (name, phone_number) pair that you wish to use as an element in a set, 
you would need a tuple rather than a list since sets require elements be immutable).

When you want to collect a mutable ordered list of elements, use a list. 
(For example, when you want to append new phone numbers to a list: [number1, number2, ...]).


***
What is the time complexity of insert, find and delete for a list?

Insert is O(n). If an element is inserted at the beginning, all other elements must be shifted right.
Find by index is O(1). But find by value is O(n) because elements need to be iterated over until the value is found.
Delete is O(n). If an element is deleted at the beginning, all other elements must to be shifted left.
***


When you want a mapping from keys to values, use a dict. 
(For example, when you want a telephone book which maps names to phone numbers: {'John Smith' : '555-1212'}).
 Note the keys in a dict are unordered.(If you iterate through a dict (telephone book), the keys (names) may show up in any order).

"""