# Ubung : Pfandrechner:
#~~~~~~~~~~~~~~~~~~~~~~~~~~

# Configurations
PLASTIC_PRICE = 0.25
GLASS_PRICE = 0.08


# 1. User Inputs
count_plastic = int(input("Count Platic: "))
count_glass = int(input("Count Glass: "))

# 2. Calculation
result = count_glass * GLASS_PRICE + count_plastic * PLASTIC_PRICE

result = round(result, 2)   # round of 2x decimal places 

# 3. Outputs
print(f"Ihr Guthaben beträgt: {result} €")
