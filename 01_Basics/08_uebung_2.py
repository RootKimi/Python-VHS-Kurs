plastikpfand = 0.25
glaspfand = 0.08

plastik = int(input("Anzahl von Plastikflaschen: "))
glas = int(input("Anzahl von Glasflaschen: "))
guthaben = plastikpfand * plastik + glaspfand * glas
print()
print ("Anzahl von Plastikflaschen: ", plastik)
print ("Anzahl von Glasflaschen: ", glas)
print ("---------------------------")
print()
print (f"Ihr Guthaben beträgt: {guthaben} Euro")
