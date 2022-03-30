for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num)

print()


for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num,end=',')

print()

for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num,end=' ')

print()

for teilnehmer in ['Arthur','Dennis','Lina']:
    print('Hallo', teilnehmer)
    print('Welches BKG?')
    print('Python Vorkenntnisse ?')

    print()


#########################
# Numver generator via range()
range(10) # 0->9
range(5,10) # 5->9
range(1,100,2) # #1,3,5,7,....,99
range(2,101,2) # #2,4,6,8,...,100

#########################
for num in range(5,10):   # for num in [5,6,7,8,9]:  
    print(num,end=' ')

print()

 # Progress Bar
for num in range(11):   # for num in [0,....,10]:  
    print(num * 10, '*' * num)


# Example: nummerierte Auflistung der Teilnehmenden
counter = 1
for teilnehmer in ['Arthur','Dennis','Lina']:
    print(f'{counter}.{teilnehmer}')
    #counter = counter + 1
    counter += 1

print()


# Nested Loop
for num in range(1,6): #[1,..,5]
    for teilnehmer in ['Arthur','Dennis','Lina']:
        print(num, teilnehmer)
    print()


# Break Loops
for num in range(10):
    
    if num == 5:
        break  # exit the loop
    
    print(num)


for num in range(10):
    
    if num == 5:
        print('Banana')
        continue # jump to the header of the loop
    
    print(num)