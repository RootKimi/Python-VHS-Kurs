# Liste von strings

import numbers


letters = ['a','b','c']

letters = ["a","b","c"]

print(letters,type(letters)) # ['a', 'b', 'c'] <class 'list'>

# Liste von Zahlen

numbers = [1,2,3,4,5,6] # [1, 2, 3, 4, 5, 6]
print(numbers)

# Matrix
matrix = [[1,2] , [3,4]]
print(matrix)

# Verctor of zeros
zeros = [0] * 30
print(zeros)

# Combine two lists together
combined = letters + numbers  # ['a', 'b', 'c', 1, 2, 3, 4, 5, 6]
print(combined)

# conversion function list()
numbers_range = list(range(20)) # []
print(numbers_range)