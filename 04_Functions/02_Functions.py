def greeting():
    print ("Hallo Dennis!")

def greeting2(first_name):
    print ("Hallo", first_name)

def greeting3(first_name, last_name):
    print ("Hallo", first_name, last_name)

def greeting4(first_name:str, last_name:str, plz:str):
    print ("Hallo", first_name, last_name,plz)

# Call a function

greeting()
greeting2("Dennis")
greeting3("Dennis","Schmidt")
greeting4("Dennis","Schmidt","12345")

# Argument oder can be changed via parameter name
greeting4(plz="0000",last_name="starke",first_name="sophie")

greeting4("0000","starke","sophie") # Hallo 0000




