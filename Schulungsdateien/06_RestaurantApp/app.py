from helper.user_inputs import get_user_input
from helper.minimum import calc_min
#from .outputs import print_result  # relative Pfaden in Modulen
from helper.maximum import calc_max
from helper.outputs import*

# Begrüßungsphase
print('Welcome Python')


# Get User Inputs
mylist = get_user_input()

print(mylist)

# Caluculate Min
min_number = calc_min(mylist)

#Calculate Max
max_number = calc_max(mylist)

# print results
print_results(mylist, min_number, max_number)