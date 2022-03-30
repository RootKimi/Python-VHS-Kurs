numbers = [1,2,31,4,5,63,7,84,9,0,2]
teilnehmer_list = ['lina','agata','sven','dennis','ana','philipp','arthur','olaf','phillipp']
"""print (teilnehmer_list)

#len() der Liste
print ('The Lenghth of the list:', len(numbers))
print ('The Lenghth of the list:', len(teilnehmer_list))

# Summe der Liste
print ('The Lenghth of the list:', sum(numbers))

# Minimum inder Liste
print ('The Lenghth of the list:', min(numbers))

# Maximum inder Liste
print ('The Lenghth of the list:', max(numbers))

#Count of the numbers
print ('The Lenghth of the list:', numbers.count(2))

#Count of the Strings am Beispiel Dennis
print ('The Lenghth of the list:', teilnehmer_list.count('dennis'))"""

import re
pattern=re.compile(r'phi')
string_match = [x for x in teilnehmer_list if re.search('phi', x)]

print (string_match)