restaurant_menu = {"pizza_list" : [{"id": 1,
                                    "title": "Pizza Tun",
                                    "price": 7,
                                    "size": "28 cm"},

                                    {"id": 2,
                                    "title": "Pizza Fungi",
                                    "price": 8,
                                    "size": "28 cm"},


                                    {"id": 3,
                                    "title": "Pizza Margeritta",
                                    "price": 9,
                                    "size": "28 cm"}]
,

                    "auflauf_list" :   [{"id": 1,
                                    "title": "Auflauf Kartoffeln",
                                    "price": 7},

                                    {"id": 2,
                                    "title": "Auflauf Nudeln",
                                    "price": 8}
                                    ]

                }
 
 # Pizzas


print(restaurant_menu["pizza_list"])
print()
print()

print('*******************    Herzlich Willkomen in unserem Restaurant   **********************\n\n')

for dish in restaurant_menu["pizza_list"]: # [0,1,2]
    #print(restaurant_menu["pizza_list"][0]['size'])
    print(dish) # {'id': 1, 'title': 'Pizza Tun', 'price': 7, 'size': '28 cm'}
    #print(pizza)
    print('\t', dish["id"], ".", dish["title"], "--->", dish["price"] , dish["size"])

print()
print()

for dish in restaurant_menu["auflauf_list"]:
    #print(pizza)
    print('\t',dish["id"], ".", dish["title"], "--->", dish["price"])

print()
print()





