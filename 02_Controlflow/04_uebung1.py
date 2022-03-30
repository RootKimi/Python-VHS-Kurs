age = 16
anzahlImWarenkorb = 1
zahlmethode = False

if age < 18:
    print ("Sie sind zu jung")

if anzahlImWarenkorb < 1:
    print ("Sie müssen Produkte auswählen.")

if zahlmethode == False:
    print ("BZ Methode nicht vorhanden")

if age >= 18 and anzahlImWarenkorb > 0 and zahlmethode == True:
    print ("Bitte gehen Sie zur Kasse.")
    

