# Anwendungsdatei
# impot the Module

import greetings

##############################
# call function from the module
###################################

greetings.greeting_de()
greetings.greeting_fr()
greetings.greeting_sp()

print(greetings.location)

####################################
# Alias
import greetings as grt
grt.greeting_sp()
grt.greeting_de()

##################################
# import certain functions 
from greetings import greeting_sp, greeting_fr

greeting_fr()
greeting_sp()


# import certain functions with alias
from greetings import greeting_sp as sp, greeting_fr as fr, location

fr()
sp()
print(location)

################################
# import all functions and others locally
from greetings import*
greeting_de()