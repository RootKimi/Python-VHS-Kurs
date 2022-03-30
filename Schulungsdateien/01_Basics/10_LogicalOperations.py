print(10 > 3 ) # True  1
print(10 >= 3 ) # True


print(10 < 3 ) # False  0
print(10 <= 3 ) # False

##############################################


x = 10
y = 20

print(x == y) # Frage :ist 10 gleich 20 -> False
print(x != y) # Frage :ist 10 nicht gleich 20 -> True

#################################################
# and or

x = 10
y = 20

print( x == 10 and y == 20) # 1 and 1 ->1  True
print( x != 30 and y != 50) #  True
print( x == 10 and y != 50) #  True

#####################
x = 10
y = 20
print( x != 10 and y == 20) # 0 and 1 ->0  False
print( x != 30 and y != 20) #  False
print( x != 10 and y != 50) #  False

###########
x = 10
y = 20

print( x == 30 or y != 50) # True
print( x == 10 or y == 50) # True
print( x == 10 or y == 20) # True
print( x == 100 or y == 209) # False

####################
# not
anwesend = True
print(not anwesend)

#########################
# in

course = 'Python Schulung'
print('Python' in course) # True --> P is capital
print('python' in course) # False --> p is small