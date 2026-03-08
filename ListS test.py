# =============================
# PYTHON LIST TEST 2
# =============================

# Task 1 — Indexing
# data = ['red', 'green', 'blue', 'yellow']
#
# Print:
# 1. the last element
# 2. the first element



# Task 2 — Slicing
# numbers = [5,10,15,20,25,30]
#
# Create a new list containing:
# 10,15,20,25
# using slicing.



# Task 3 — Append vs Extend
# a = [1,2,3]
# b = [4,5]
#
# 1. Append b to a
# 2. Print a
#
# Reset a to [1,2,3]
#
# 3. Extend a with b
# 4. Print a



# Task 4 — Remove vs Pop
# items = ['car','bike','plane','boat']
#
# 1. Remove 'bike'
# 2. Pop the first element
# 3. Print the list



# Task 5 — Count and Index
# letters = ['a','b','c','a','a','d']
#
# Print:
# 1. how many times 'a' appears
# 2. the index of 'c'



# Task 6 — Sort
# numbers = [9,1,5,3,7]
#
# Sort the list in descending order
# and print it.



# Task 7 — Nested List
# letters = ['x','y','z']
# numbers = [1,2,3]
#
# Create a nested list that contains both lists.
# Print it.



# Task 8 — Zip
# letters = ['a','b','c']
# numbers = [10,20,30]
#
# Create a zipped list and print it.



# Task 9 — Comprehension
# numbers = [1,2,3,4,5,6,7,8]
#
# Create a list containing only
# odd numbers.



# Task 10 — Comprehension
# numbers = [1,2,3,4,5]
#
# Create a list of squares.



# Task 11 — String Cleaning
# words = ['HELLO','WORLD','PYTHON']
#
# Using a comprehension:
# convert everything to lowercase.



# Task 12 — Domain Cleaning
# domains = [
# 'WWW.APPLE.COM',
# 'google.com',
# 'localhost',
# 'WWW.OPENAI.COM'
# ]
#
# Using a comprehension:
# 1. lowercase everything
# 2. remove 'www.'
# 3. keep only domains containing '.'
#
# Print the result.



# Task 13 — Copy vs Deepcopy
# import copy
#
# matrix = [[1,2],[3,4]]
#
# 1. create shallow copy
# 2. create deep copy
# 3. modify an inner value in both copies
# 4. print matrix, shallow, deep



words = ['HELLO', 'WORLD', 'PYTHON']
print(words[-1])
print(words[0])


numbers = [5,10,15,20,25,30]
print(numbers[1:-1])


a = [1,2,3]
b = [4,5]

a.append(b)
print(a)
a.remove(b)
print(a)
a.extend(b)
print(a)

items = ['car','bike','plane','boat']

items.remove('bike')
items.pop(0)
print(items)

letters = ['a','b','c','a','a','d']
b = letters.count('a')
c = letters.index('c')
print(letters)
print(b)
print(c)

numbers = [9,1,5,3,7]

numbers.sort(reverse=True)
print(numbers)



letters = ['x','y','z']
numbers = [1,2,3]

nested_list = [letters,numbers]
print(nested_list)

letters = ['a','b','c']
numbers = [10,20,30]

zipped_list = list(zip(letters,numbers))
print(zipped_list)

numbers = [1,2,3,4,5,6,7,8]
odd_numbers = [
    n
    for n in numbers
    if n % 2 == 1
]
print(odd_numbers)

numbers = [1, 2, 3, 4, 5]
squared = [
    n * n
    for n in numbers

]
print(squared)

words = ['HELLO','WORLD','PYTHON']
compre = [
    str(w).lower()
    for w in words
]
print(compre)

domains = [
'WWW.APPLE.COM',
'google.com',
'localhost',
'WWW.OPENAI.COM'
]

low = [
    str(d).lower().replace('www.','')
    for d in domains
    if '.' in d
]
print(low)


import copy
matrix = [[1,2],[3,4]]


shallow_copy = matrix.copy()
deepcopy = copy.deepcopy(matrix)


shallow_copy[1][-1] = 7
deepcopy[0][-1] = 9

print(matrix)
print(shallow_copy)
print(deepcopy)