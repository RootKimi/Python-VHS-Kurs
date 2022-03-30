UPPER_LIMIT = 20
sum_g = 0
sum_ug = 0


for num in range(0,UPPER_LIMIT+1):
    print (num)
    if num%2==1:
        print(num,"ungerade")
        sum_ug=sum_ug+num
    if num%2==0:
        print(num,"gerade")
        sum_g=sum_g+num

print (sum_ug)
print (sum_g)