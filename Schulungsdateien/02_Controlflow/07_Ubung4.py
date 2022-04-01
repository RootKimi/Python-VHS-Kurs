
# Variables
all_numbers = ""
odd_numbers = ""
even_numbers = ""
sum_odd = 0
sum_even = 0


lower_limit = int(input("Enter lower limit: "))
upper_limit = int(input("Enter upper limit: "))

for num in range(lower_limit, upper_limit+1):
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