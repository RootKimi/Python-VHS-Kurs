


def calculator(num1,num2):
    addieren = num1 + num2
    subtraction = num1 - num2
    multi = num1 * num2

    return addieren, subtraction, multi, "Die Ergebnisse sind:"

    # caller

    plus, minus, multi, message = calculator (5, 2)

    print (message)
    print(f"5+3 = {plus}")
    print(f"5-3 = {minus}")
    print(f"5*3 = {multi}")