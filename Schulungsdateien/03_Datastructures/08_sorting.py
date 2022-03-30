numbers = [9,16,3,5,6,4,3,2,45,6,1,3,2,532]
print(numbers)
print()
print()
# 1.Variante ( In- Place)
#***************************
numbers.sort() # aufteigend
print(numbers)

print()
print()

numbers.sort(reverse=True) # abteigend
print(numbers)

print()
print()

# 2. Variante (creaes a new list)
#****Not in place*************
unsorted_numbers = [9,16,3,5,6,4,3,2,45,6,1,3,2,532]
sorted_numbers = sorted(unsorted_numbers)
print(unsorted_numbers)
print(sorted_numbers)