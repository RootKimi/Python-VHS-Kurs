liste =[]
num = 1
while num != 0:
    num = int(input("Eingabe der Benutzerzahl: "))
    liste.append(num)

print (liste)

for num in liste:
    if num < 0:
        print ("Negativ:",num)
        
    else:
        print ("Positiv:",num)


