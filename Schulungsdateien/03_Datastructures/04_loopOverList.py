teilnehmer_list = ['lina','agata','ana','phillip','sven','arthur','dennis','olaf']

counter = 1
for teilnehmer in teilnehmer_list:
    print(f'{counter}.{teilnehmer}')
    counter +=1

print()

for teilnehmer in enumerate(teilnehmer_list): # enumerate -> tuple (index, value)
    print(teilnehmer)
    
    
print()

for teilnehmer in enumerate(teilnehmer_list,1): # enumerate -> tuple (index, value, start_idx)
    print(teilnehmer)

    
print()

# Enumerate with List unpacking
# Tupel auspacken

for teilnehmer in enumerate(teilnehmer_list,1): # enumerate -> tuple (index, value, start_idx)
    print(teilnehmer[0],teilnehmer[1]) #(1,'lina')[0]->1  (1,'lina')[1]-> 'lina'

print()



for idx,val in enumerate(teilnehmer_list,1): # enumerate -> tuple (index, value, start_idx)
    print(idx,val) #(1,'lina')[0]->1  (1,'lina')[1]-> 'lina'

print()