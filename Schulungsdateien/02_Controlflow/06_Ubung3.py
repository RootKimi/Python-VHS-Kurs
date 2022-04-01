# Ubung : arbeiten mit Zahlen:
#~~~~~~~~~~~~~~~~~~~~~~~~~~

# Configurations
# Variables
all_numbers = ""  # alle Zahlen
odd_numbers = ""  # ungerade Zahlen
even_numbers = ""  # gerade Zahlen
sum_odd = 0          # Summe ungerade Zahlen
sum_even = 0         # Summe gerade Zahlen


upper_limit = int(input("Enter upper limit: "))

for num in range(1, upper_limit+1):
    all_numbers += str(num) + " "
    
    if num%2 == 0:
        even_numbers += str(num) + " "
        sum_even += num
    else:
        odd_numbers += str(num) + " "
        sum_odd += num


# Output phase
print(f"All Numbers: {all_numbers}")
print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")
print(f"Sum Odd: {sum_odd}")
print(f"Sum Even: {sum_even}")