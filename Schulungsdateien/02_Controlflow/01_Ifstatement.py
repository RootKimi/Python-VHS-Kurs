temparatur = 40

if temparatur > 30:
    print("Es ist heiß!!!")

else:
    print("Es ist cool!!!")

######
temparatur = -25
if temparatur >= 30:    ## ja ich bin größer 30 -> heiß   oder Nein ich bin kleiner 30 -> gehe bitte zum nächtesten elif
    print('Es ist heiß!!')

elif temparatur < 30 and temparatur >=20:
    print('Es ist warm !')

elif temparatur < 20 and temparatur >=10:
     print('Es ist kalt !')

else:
    print('Es ist zu kalt!')


####

temparatur = -25
if temparatur >= 30:    ## ja ich bin größer 30 -> heiß   oder Nein ich bin kleiner 30 -> gehe bitte zum nächtesten elif
    print('Es ist heiß!!')

elif  20 <= temparatur < 30:
    print('Es ist warm !')

elif 10 <= temparatur < 20:
     print('Es ist kalt !')

else:
    print('Es ist zu kalt!')



######
temparatur = -25
if temparatur >= 30:
    print('Es ist heiß!!')

elif temparatur >=20:
    print('Es ist warm !')

elif temparatur >=10:
     print('Es ist kalt !')

else:
    print('Es ist zu kalt!')
