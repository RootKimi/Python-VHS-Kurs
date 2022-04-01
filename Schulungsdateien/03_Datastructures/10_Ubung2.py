foods = [ 
    [100, "Pizza Tunfisch", 5],
    [101, "Pizza Fungi", 6],
    [102, "Pizza Margeritta", 7],

    [200, "Auflauf Kartoffeln", 7],
    [201, "Auflauf Nudeln", 6],

    [300, "Salat", 3]

]

drinks = [ 
    [400, "Wasser", 2],
    [401, "Fanta", 3],
    [402, "Cola", 3]
    ]


# Welcome Message
print("Willkommen bei ACASA Restaurant")
print("=" * 30 , "\n")

# Show Menu 
print("Gerichte:\n" , "=" * 20,sep="=")

for item in foods:
    print(f" {item[0]}. {item[1]} ---> {item[2]} €")

# # Show Menu 
print("Getränke:\n" , "=" * 20, sep="=")

for item in drinks:
    print(f" {item[0]}. {item[1]} ---> {item[2]} €")

