user_number = ""
all_numbers = []
pos_numbers = []
neg_numbers = []
total = 0

while True:
    user_number = int(input("Enter your numbers: "))


    if user_number == 0:
        break 

    all_numbers.append(user_number)
    total += user_number

    if user_number > 0:
        pos_numbers.append(user_number)
    elif user_number < 0:
        neg_numbers.append(user_number)


# Sorting
all_numbers.sort()
pos_numbers.sort()
neg_numbers.sort()


print(f"All Numbers: {all_numbers}")
print(f"Pos. Numbers: {pos_numbers}")
print(f"Neg. Numbers: {neg_numbers}")

print(f"Min. Numbers: {all_numbers[0]}")
print(f"Max. Numbers: {all_numbers[-1]}")
print(f"Sum. Numbers: {total}")

