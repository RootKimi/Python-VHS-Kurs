# Define a Function
'''
Syntax:

def Funktion_name():
    was soll meine Funktion machen

'''

def greeting():
    print('Hallo Asmae')


def greeting2(first_name):
    print('Hallo',first_name)


def greeting3(first_name, last_name):
    print('Hallo',first_name,last_name)


def greeting4(first_name:str, last_name:str, plz:str):
    print('Hallo',first_name,last_name,plz)

# With return
def greeting5(first_name, last_name):
    return f'Hallo {first_name} {last_name}'





# Call a Function
'''
Syntax:

Funktion_name()

'''

greeting()
greeting2('Agata')
greeting3('sven','aaa')
greeting4('frank','Meier','12345')
message= greeting5('Asmae','bethi')
print(message)


# Argument oder can be changed via parameter name
greeting4(plz='0000',last_name='starke',first_name='sophie')

greeting4('0000','starke','sophie') # Hallo 0000 