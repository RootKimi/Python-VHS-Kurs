user_list = ['lina',    #0
            'agata',    #1
                ['A',   #2
                 'B',
                 True,
                
                    [1,
                        2,
                        3, 
                        ['E','F']
                    ]
                    
                ]
            
            ]


###########################################
print(user_list[0]) # lina
print(user_list[1]) # agata
print(user_list[2][2]) #True  # ['A', 'B', True, [1, 2, 3, ['E', 'F']]]
print(user_list[2][0])   # 'A'
print(user_list[2][1])   # 'B'
print(user_list[2][3][0])  # 1
print(user_list[2][3][3])   #['E', 'F']
print(user_list[2][3][3][1]) # 'F'

print() 
print()
###################################################

user = {'id':1,
        'name':'Thomas',
        'cars':['VW','Audi','Tesla'], 
        'kids':
                [
                    {'name':'Sara','age':20},
                    {'name': 'Liane','age':25,'friends':['Marcus','Lucas']}
                ]     
        
        }

print(user)
print()
print()

print(user['name'])# Thomas
print(user['id'])   # 1
print(user['cars'])  # ['VW','Audi','Tesla']
print(user['cars'][0])         # 'VW'
print(user['cars'][2])   # Tesla            
print(user['kids']) #[{'name': 'Sara', 'age': 20}, {'name': 'Liane', 'age': 25, 'friends': ['Marcus', 'Lucas']}]
                      
print(user['kids'][1]['friends'])                    # friends liste  ['Marcus', 'Lucas']
print(user['kids'][1]['friends'][1])                                        # lucas
print(user['kids'][0]['name'])                         #sara