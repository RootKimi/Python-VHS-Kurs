teilnehmer_list = ['lina','sven','dennis','ana','philipp','arthur','olaf']
counter = 1
for teilnehmer in teilnehmer_list:
    
    print(f'{counter}.{teilnehmer}')
    counter +=1

print ()

#Enumerate with list unpacking
for teilnehmer in enumerate(teilnehmer_list,1): # enumerate -> Tuple (Index, Value)
    print (teilnehmer)

print ()

#Tupel unpacking

for teilnehmer in enumerate(teilnehmer_list,1): # enumerate -> Tuple (Index, Value, Startindex)
    print (teilnehmer[0],teilnehmer[1]) #(1,'lina')

print ()

for idx,val in enumerate(teilnehmer_list): #enumerate -> tuepel (index,value, start index)
    print (idx,val) 

print ()