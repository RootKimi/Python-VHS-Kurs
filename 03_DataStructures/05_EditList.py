teilnehmer_list = ['lina','agata','sven','dennis','ana','philipp','arthur','olaf']
print(teilnehmer_list)

#Add am Ende einer Liste
teilnehmer_list.append('Asmae')
print(teilnehmer_list)

#Insert an zweite Position in der Liste
teilnehmer_list.insert(2,'Asmae')
print(teilnehmer_list)

#Edit Value
teilnehmer_list[2] = 'AnastasiaNeu'
print(teilnehmer_list)

#Delete the last Item () und mit Index
teilnehmer_list.pop(2)
print(teilnehmer_list)

#Delete the first match
teilnehmer_list.remove('ana')
print(teilnehmer_list)

#Alternative zum löschen
del teilnehmer_list[3]
print (teilnehmer_list)

#Delete Range Index
del teilnehmer_list[3:4]
print (teilnehmer_list)


