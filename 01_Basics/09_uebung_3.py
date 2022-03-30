gewicht = input("Ihr Gewicht in kg: ")
groesse = input("Ihre Größe in m: ")

bmi = float(gewicht) / float(groesse)**2
print()
print ("----------------------------")
print()
print (f"Ihr BMI beträgt:, {round(bmi,2)}")