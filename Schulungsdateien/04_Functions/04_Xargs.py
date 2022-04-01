def add(num1,num2,num3):
    print(num1 + num2 + num3)


add(5,6,0)
add(5,6,7)


def add2(container):
    print(container)


# add2(5,6) # TypeError: add2() takes 1 positional argument but 2 were given

# Tuple: *container-> belibige Anzahl von -argumenten vom Caller zu empfangen
def add3(*container):
    print(container)
    for num in container:
        print(num)

add3(2,3,4)