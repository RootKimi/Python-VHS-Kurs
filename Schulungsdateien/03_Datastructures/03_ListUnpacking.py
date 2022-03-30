numbers = [1,2,3,4,5,6,7,8,9]

print(numbers)

first = numbers[0]  # 1
second = numbers[1]
third = numbers[2]

print(first, second, third)

# Alternative

numbers = [1,2,3]  # 3 Elementen
first, second, third = numbers  # wir brauchen 3 variablen
print(first, second, third)


'''
numbers = [1,2,3,4]  # 4 Elementen
first, second, third = numbers  # too many values to unpack (expected 3)  wir brauchen 4 variablen
print(first, second, third)
'''

numbers = [1,2,3,4,5,6,7,8,9]  
first, second, third, *others = numbers  
print(first, second, third, others) # 1 2 3 [4, 5, 6, 7, 8, 9]


numbers = [1,2,3,4,5,6,7,8,9]  
first,*others,last = numbers  
print(first,others,last) # 1 [2, 3, 4, 5, 6, 7, 8] 9