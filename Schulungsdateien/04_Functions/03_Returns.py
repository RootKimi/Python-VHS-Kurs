
# No Return
def addieren1(x,y):
    result = x + y
    print('Result:', result)


# single Return
def addieren2(x,y):
    result = x + y
    return result

# Multi Return
def calculator(num1, num2):
    addieren = num1 + num2
    subtraction = num1 - num2
    multiplikation = num1 * num2
    return addieren,subtraction,multiplikation,'Die Ergebnisse sind:'


# caller

# No Retun
addieren1(4,5)

# Single Return
total = addieren2(5,6)
print('Ergebnis:',total)


# Multi Return
plus, minus,multi,message = calculator(5,2)
print(message)
print(f'5+3 = {plus}')
print(f'5-3 = {minus}')
print(f'5-3 = {multi}')