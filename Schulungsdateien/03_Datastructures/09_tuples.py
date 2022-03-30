# Tupel is a READ ONLY LIST

teilnehmer_tupel =('lina', 'agata', 'ana','asmae','phillip','phillip', 'sven', 'arthur','phillip', 'dennis', 'olaf','phillip')
print(teilnehmer_tupel,type(teilnehmer_tupel))

print(teilnehmer_tupel[0])
print(teilnehmer_tupel[3])
print(teilnehmer_tupel[-1])

print(teilnehmer_tupel[0:5])

print()
print()

## Loop over a tupel
for teilnehmer in teilnehmer_tupel:
    print(teilnehmer)


print()
print()
# search for an element
if 'lina' in teilnehmer_tupel:
    print('Lina ist da')


##########################################
# Indirect way to change the tupel
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. Convert th tuple in a temp list
tmp_list = list(teilnehmer_tupel)
print(tmp_list)

#2. Adjust the tmp List
tmp_list.append('justin')
print(tmp_list)

#3. Reassign the tuple to the tmp list
teilnehmer_tupel = tuple(tmp_list)
print(teilnehmer_tupel)
