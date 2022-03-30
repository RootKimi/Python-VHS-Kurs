# Welcome message
print("BMI Rechner")
print("~"*30)


# User Input
weight = float(input('Enter the weight [kg]: '))
height = float(input('Enter the height [m]'))


# Calculation

bmi = (weight) / (height **2)

# Output

print('Your BMI ist: ', bmi)

