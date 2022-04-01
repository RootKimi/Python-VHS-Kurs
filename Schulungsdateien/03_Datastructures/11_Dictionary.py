# define a dictionary
user = {'id':50, 'name':'lina', 'PLZ':'24356'} # key -> 'id'   value --> 50
print(user, type(user))

print()
print()

# user =[50,'lina',29,'24356']

# Alternative to define a dictionary
user = dict(id = 50, name ='lina', PLZ = '24356')
print(user, type(user))
print()
print()

# Edit a value of akey
user['name'] = 'Ana'
print(user)

print()
print()

# Add a new key value pair
user['stadt'] = 'Hamburg'
print(user)

print()
print()

# look for an existing Key 
print(user['stadt'])  # Hamburg
print(user.get('stadt')) # Hamburg
print()
print()

# look for an non-existing Key -> error
#print(user['location'])


# look for an non-existing Key -> whithout error
print(user.get('location'))  # None
print(user.get('location','there is no Key location'))  # customised message
print()
print()
#  delete a key from a dictionary
# {'id': 50, 'name': 'Ana', 'PLZ': '24356', 'stadt': 'Hamburg'}


user.pop('stadt') # {'id': 50, 'name': 'Ana', 'PLZ': '24356'}
print(user)
print()
print()

#  delete a key from a dictionary and pack it into a variable
name = user.pop('name')

print(user)
print(name)


# Check if a key exists
if 'id' in user:
    print('Id key exists')



# Loop over keys

#user = {'id':50,'PLZ':'24356'}  2Keys (id,plz) - 2 values(50,24356)

for key in user.keys():
    print(key)

print()
print()
# Loop over values

#user = {'id':50,'PLZ':'24356'}  2Keys (id,plz) - 2 values(50,24356)

for val in user.values(): # 50 24356
    print(val)

print()
print()
# loop over items
for item in user.items(): # item1: ('id', 50)   item2:('PLZ', '24356')
    print(item)
    print(item[0], item[1])
    print()

print()
print()
# Unpacking
for key,val in user.items():
    print(key,val)

