teilnehmer_list = ['lina','agata','ana','phillip','sven','arthur','dennis','olaf']
print(teilnehmer_list )

# Add append()

teilnehmer_list.append('asmae')
print(teilnehmer_list )

# Add at a certain position   insert()

teilnehmer_list.insert(2,'asmae')
print(teilnehmer_list )

# Edit Value
teilnehmer_list[2] = 'anastasia'
print(teilnehmer_list )

# Delete
teilnehmer_list =['lina', 'agata', 'asmae', 'ana','asmae','phillip', 'sven', 'arthur', 'dennis', 'olaf', 'asmae']

## Delete the last item
teilnehmer_list.pop()
print(teilnehmer_list )


## Delete at certain index
teilnehmer_list.pop(1)
print(teilnehmer_list)

## Delete the first match
teilnehmer_list =['lina', 'agata', 'asmae', 'ana','asmae','phillip', 'sven', 'arthur', 'dennis', 'olaf', 'asmae']
teilnehmer_list.remove('asmae')
print(teilnehmer_list)

# Alternative way to delete via meta command in python  del
del teilnehmer_list[0]
print(teilnehmer_list)

# delte a range of items
del teilnehmer_list[1:3]
print(teilnehmer_list)