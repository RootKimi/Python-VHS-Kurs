import csv

#with open("csvfile.csv", newline='') as csvfile:

with open('/Users/denniskimschmidt/GitHub/Python-VHS-Kurs/05_Modules/csvfile.csv', 'r') as csv_datei:
    spamreader = csv.reader(csv_datei, delimiter=';', quotechar='|')
    for row in spamreader:
            print(' '.join(row))

   
 
