def add(num1, num2, num3):
    print(num1+num2+num3)

#Xarg: beliebiger Anzahl von Argumenten
# Tuple: "Container"

def add2(*container):
    print(container)
    for num in container:
        print(num)

add(5,6,0)
add(5,6,7)

add2(5)
add2(5,6)
add2(5,6,7)

