#Direkt auspacken
numbers = [1,2,3,4,5,6]

first = numbers[0]
second = numbers[1]
third = numbers[2]
print (first, second, third)

#Alternative zum auspacken
numbers = [1,2,3,4,5,6]
first,second,third,*others = numbers
print (first,second,third,others)

