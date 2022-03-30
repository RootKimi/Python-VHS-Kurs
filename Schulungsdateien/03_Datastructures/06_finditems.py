teilnehmer_list =['lina', 'agata', 'ana','asmae','phillip', 'sven', 'arthur', 'dennis', 'olaf']
print(teilnehmer_list)

print()
print()

if 'sven' in teilnehmer_list:
    print('sven ist da:')
    print(teilnehmer_list.index('sven'))

else:
    print('sven ist nicht da')


print()
print()

if 'sven' not in teilnehmer_list:
    print('sven ist nicht da')
    print(teilnehmer_list.index('sven'))

else:
    print('sven ist da')