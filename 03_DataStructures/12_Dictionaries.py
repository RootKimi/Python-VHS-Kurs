# Define Dictionary
user = {'id': 50,'name':'lina','PLZ':'12345'}
print (user,type(user))
print()


# Alternative 
user = dict(id = 50, name = 'lina', PLZ = '12345')
print (user,type(user))
print()


#Edit a value of a key
user['name'] = 'Ana'
print (user)
print()


# Add a new key value pair
user['stadt'] = 'Hamburg'
print (user)
print()


#Bestimmten value ausgeben
print (user['stadt'])
print()

#Look for an non-existing key
"""print (user['location'])
Traceback (most recent call last):
  File "/Users/denniskimschmidt/GitHub/Python-VHS-Kurs/03_DataStructures/12_Dictionaries.py", line 30, in <module>
    print (user['location'])
KeyError: 'location'"""

# Look for an non-existing key without error
print (user.get('location')) # none
print (user.get('location','there is no key location')) # Custom Error

user.pop('stadt') # 

#delete a key vom dict and store it in a variable
name = user.pop('name')
print (user)
print (name)

# check if user exist
if 'id' in user:
    print('ID key exists')

#Loop over keys
for key in user.keys():
    print(key)

# Loop over values
for val in user.values(): 
    print(val)

#Loop over items
for item in user.items(): 
    print(item)
    print(item[0], item[1])

#Unpacking
for key,val in user.items():
    print (key,val)