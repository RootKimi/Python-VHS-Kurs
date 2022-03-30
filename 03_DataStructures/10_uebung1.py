
counter = 1
list = []
listger = []
listung = []
listpos = []
listneg = []
listsum= []

while counter < 12:
    inputzahl = int(input("Bitte geben Sie eine Integer Zahl ein: "))
    list.append(inputzahl)
    counter += 1 

print()   
print("*" * 30)
print()   
print ("1. Alle Zahlen:", list)
print()   
print("*" * 30)
print() 

### Positive und negative Zahlen ###

for num in list:
    if num >= 0:
        listpos.append(num)
    else:
        listneg.append(num)
print() 
print ("2. Alle positiven Zahlen:", listpos)
print()   
print("*" * 30)
print() 
print ("3. Alle negativen Zahlen:", listneg)
print()   
print("*" * 30)
print() 

### Summe aller Zahlen, positiv und negativ ###

listsum = listpos + listneg
newnum = 0
for num in listsum:
    newnum = int(num+newnum)
print ("4. Summe der pos. und neg. Zahlen:", newnum)
#print ("4. Summe der pos. und neg. Zahlen:", sum(listsum))

print()   
print("*" * 30)
print() 

### Min aller Zahlen, positiv und negativ ###

print ("5. Minimum der gesamten pos. und neg. Zahlen:", min(listsum))

print()   
print("*" * 30)
print() 

### Max aller Zahlen, positiv und negativ ###

print ("6. Maximum der gesamten pos. und neg. Zahlen:", max(listsum))

print()   
print("*" * 30)
print() 

#### Gerade und ungerade Zahlen ###

for num in list:
    if num%2==0:
        listger.append(num)
    else:
        listung.append(num)
print() 
print ("7. Alle geraden Zahlen:", listger)
print()   
print("*" * 30)
print() 
print ("8. Alle ungeraden Zahlen:", listung)
print()   
print("*" * 30)
print() 