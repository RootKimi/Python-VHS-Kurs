# Ubung : Online Shop:
#~~~~~~~~~~~~~~~~~~~~~~~~~~

# Configurations
age = 25
payment_method = True
items = 3

# Code
if age>=18 and payment_method == True  and items >0:
    print("Zur Kasse Bitte ")
else:

    if age <18:
        print("Du bist zu jung")

        
    if payment_method == False:
        print("Bezahlmethode nicht vorhanden")

    if items < 1:
        print("Du muss Produke auswählen")