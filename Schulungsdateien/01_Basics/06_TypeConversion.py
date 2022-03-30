""" 
int()
float()
str()
"""

x = "10" # string
print(x, type(x))

x = int(x) # int
print(x, type(x))

x = float(x)
print(x, type(x))

x = str(x)
print(x, type(x))  # "10.0"

#############################################
# Example:
num1 = input("Enter num1: ") # "5"
num2 = input("Enter num2: ") # "6"


num1 = int(num1)
num2 = int(num2)

print("Result:", num1 + num2) # 11

################################################
# Shortcut --> User Inputs + Conversion
num1 = int(input("Enter num3: ")) # 5
num2 = int(input("Enter num4: ")) # 6

print("Result:", num1 + num2) # 11