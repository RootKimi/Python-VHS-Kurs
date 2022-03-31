user_list = ['lina',
            'Agata',
                ['A',
                'B',
                True,
                    [1,
                    2,
                    3,
                    [  'E','F']
                ]
                ]
            ]

print (user_list[0]) #Lina
print (user_list[1]) #agata
print (user_list[2][2]) #True
print (user_list[2][0]) # A
print (user_list[2][1]) #B
print (user_list[2][3][0]) #1
print (user_list[2][3][3]) # ['E','F']
print (user_list[2][3][3][1]) #'F 


#################################

user = {'id':1,
        'name':'Thomas',
        'cars': ['VW','Audi','Tesla'],
        'kids':
                [
                    {'name':'Sara','age':20},
                    {'name': 'Liane', 'age': 25,'friends': ['Marcus','Lucas']}
                ]        
        }
print (user)
print(user['name'])  # Thomas
print(user['id'])    # 1
print(user['cars'])    # ['VW','Audi','Tesla']
print(user['kids'])    #[
                    #{'name':'Sara','age':20},
                    #{'name': 'Liane', 'age': 25,'friends': ['Marcus','Lucas']}
                    #]
print(user['cars'][0])    # VW
print(user['cars'][2])    # Tesla
print(user['kids'][1]['friends'])    # ['Marcus','Lucas']
print(user['kids'][1]['friends'][1])    # ['Lucas']
print(user['kids'][0]['name'])    # ['Sara']