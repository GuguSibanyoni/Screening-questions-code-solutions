# More on lists

# What is the difference between append and extend?

d = ['Thenj','Gugu','Lwandle','Tushi']
d.append(['Khonzi', 'Landi'])
print(d)


a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
c = ['Thenji', 'Gugu', 'Khonzi', 'Thushi', 'Landi']

a.append(b)
print(a)

# When we use the append() method, we add an element at the end of a list 

a.extend(c)
print(a)
#.extend() extends linear data structures 


#sorting a list without sort function

#sort in ascending order 
Numbers = [2, 3, 5, 10, 7, 1, 8, 9, 4, 6]

for i in range(len(Numbers)):
    for j in range(i + 1, len(Numbers)):

        if Numbers[i] > Numbers[j]:
            Numbers[i], Numbers[j] = Numbers[j], Numbers[i]

print(Numbers)

#Sort a list of integers in descending order without reverse
Numbers = [2, 3, 5, 10, 7, 1, 8, 9, 4, 6]

for i in range(len(Numbers)):
    for j in range(i + 1, len(Numbers)):

        if Numbers[i] < Numbers[j]:
            Numbers[i], Numbers[j] = Numbers[j], Numbers[i]

print(Numbers)

'''have pointers i and j iterating through the list simultaineously
(with j being one index ahead of i) so that you can use the logical operators'''


# Get the first element from each nested list in a list

Numbers = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

for i in Numbers:
    print(i[0])
    

#Adding all the elements without using .sum() function
a = [1, 2, 3, 4, 5]

def _sum(a):

    sum = 0

    for i in a:
        sum = sum + i
    return sum

print(_sum(a))


# Combine elements in a list into a single string 

Girls = ['Thenji', 'Thushi','Khanyi','Khonzi','Landi']

Ladies = "".join([str(element) for element in Girls])

print(Ladies)


# finding the minimum of a list

def minimum(list):
    current_min = list[0]
    for num in list:
        if num < current_min:
            current_min = num
    return current_min


print(minimum([1, 2, 3, -1]))


#To check if a list is empty

list = []

if len(list) == 0:
    print('list is empty')

if not any in list:
    print('list is empty')

#Squaring elements in a list

Numbers = [1, 2, 3, 4, 5]


myList = []
for i in Numbers:
    myList.append(i*i)
print(myList)

#   or

myList = [i*i for i in Numbers]
print(myList)


#merging two lists in a dictionaries

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

myDict = {}
for name, hero in zip(names, heros):
    myDict[name] = hero
print(myDict)

#you can also exclude an element 
myDict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(myDict)



 
