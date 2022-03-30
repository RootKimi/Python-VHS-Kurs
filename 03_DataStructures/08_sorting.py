"""numbers = [1,4,22,33,2,6,8,4,6,66,9,0,2,4,1,7,9,8,5]
print (numbers)

# 1. Variante (In- Place)
numbers.sort()                  # Aufsteigend
print (numbers)

numbers.sort(reverse=True)      # Absteigend
print (numbers)"""

# 2. Variante (creases a new list)
unsorted_numbers = [1,4,12,22,33,2,6,8,4,6,66,9,0,2,4,1,7,9,8,5]
sorted_numbers = sorted(unsorted_numbers)
print (unsorted_numbers)
print (sorted_numbers)