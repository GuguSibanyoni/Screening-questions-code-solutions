# How do we get a count of the duplicate values

names = ['Thenji', 'Thenji', 'Kat', 'Sam', 'Sam']
Freq = {}

for i in names:
    if (i in Freq):
        Freq[i] += 1
    else:
        Freq[i] = 1

print(Freq)


# How Iterate over both the values in a list and their indices

a = ['Thenji', 'Gugu', 'Khonzi', 'Thushi', 'Landi']

for i, val in enumerate(a):
    print("%s : %s" % (i, val))

# How to concatenate two lists

Boys = ['Sbu', 'Nhlanhla', 'Sihle']
Girls = ['Thenji', 'Gugu', 'Khonzi']

print(Boys + Girls)

# How to manipulate every element in a list with list comprehension
Girls = ['Thenji', 'Gugu', 'Khonzi']

for i in Girls:
    print(i + ', smile please')

a = [1, 2, 3, 4, 5]

for i in a:
    print(i * 5)

# Creating a dict

Girls = ['Thenji', 'Thushi', 'Khanyi', 'Khonzi', 'Landi', 'Thenji',
         'Thushi', 'Khonzi', 'Landi', 'Thenji', 'Thushi', 'Khanyi', 'Khonzi', ]

Ladies = {i for i in Girls}

print(Ladies)


# How to check if an element is not in a list?

Girls = ['Thenji', 'Gugu', 'Khonzi']

if 'Thushi' in Girls:
    print('element found')
else:
    print('element not found')

# Count occurrences of each value in a list without counter function

Numbers = [7, 1, 6, 3, 4, 5, 6, 7, 8, 9, 10]


def countX(lst, x):
    count = 0
    for element in lst:
        if (element == x):
            count = count + 1
    return count


Number = 6

print('{} has occurred {} times'.format(Number, countX(Numbers, Number)))


# Count vowels in a different way using dictionary

def Check_vowels(string1, vowels):

    # casefold has been used to ignore cases
    string = string1.casefold()

    vowel_count = {}.fromkeys(vowels, 0)

    for character in string1:
        if character in vowel_count:
            vowel_count[character] += 1
    return vowel_count


vowels = 'aeiou'
string1 = "Gugu is not for sale"
print(Check_vowels(string1, vowels))
