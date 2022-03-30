LL = 5
UL = 20
sum_g = 0
sum_ug = 0


for num in range(LL,UL+1):
    print(num)
    if num%2==1:
        print(num,"ungerade")
        sum_ug=sum_ug+num
        print (sum_ug)
