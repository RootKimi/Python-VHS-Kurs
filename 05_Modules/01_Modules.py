
# Import Greetings
from greetings import*

def app():
    print("Wilkommen im REstaurant xyz")
    print ("Choose your languange: ")
    print("[1] DE")
    print("[2] EN")
    print("[3] ESP")


    user_language = int (input(">"))

    if user_language == 1:
        greeting_de()
    elif user_language == 2:
        greeting_eng()
    elif user_language == 3:
        greeting_esp()

app()