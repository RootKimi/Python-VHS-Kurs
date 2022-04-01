
user_number = ""
all_numbers = ""
pos_numbers = ""
neg_numbers = ""

while True:
    user_number = int(input("Enter your numbers: "))

    if user_number == 0:
        break 

    all_numbers += str(user_number) + " "

    if user_number > 0:
        pos_numbers  += str(user_number) + " "
    elif user_number < 0:
        neg_numbers  += str(user_number) + " "

print(f"All Numbers: {all_numbers}")
print(f"Pos. Numbers: {pos_numbers}")
print(f"Neg. Numbers: {neg_numbers}")

