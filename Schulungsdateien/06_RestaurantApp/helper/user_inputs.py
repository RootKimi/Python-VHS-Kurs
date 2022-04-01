def get_user_input():
    mylist = []
    while True:
        user_input = int(input('Enter a numbr: '))
        if user_input== 0:
            break
        mylist.append(user_input)
    
    return mylist