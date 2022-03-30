teilnehmer_tupel = ('lina','agata','sven','dennis','ana','philipp','arthur','olaf')
"""print (teilnehmer_tupel,type(teilnehmer_tupel))

print (teilnehmer_tupel[3])
print (teilnehmer_tupel[3:6])

# Loop over a tupel
for teilnehmer in teilnehmer_tupel:
    print (teilnehmer)
print()
print()

# Search for an element
if 'lina' in teilnehmer_tupel:
    print ('Lina ist da')
"""

#############################################
#Indirekt way to change the tupel
###--------------------------------
# 1. Convert th tuple in a temporäre list
tmp_list = list(teilnehmer_tupel)

# 2. Adjust the tmp List
tmp_list.append('justin')
print (tmp_list)

# 3. Reassign the tiple to the tmp list
teilnehmer_tupel = tuple(tmp_list)
print (teilnehmer_tupel)

