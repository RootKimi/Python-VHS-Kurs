# Anwedungsdatei
# Import the module

import greetings

#################################
# Call a function from the module
#################################

greetings.greeting_esp()
greetings.greeting_eng()
greetings.greeting_de()

print(greetings.location)

#################################
#Alias
import greetings as grt
grt.greeting_esp
grt.greeting_de

#################################

# Import certain function
from greetings import greeting_esp, greeting_de

greeting_de()
greeting_esp()

#################################

# Import certain functions with alias
from greetings import greeting_de as de, greeting_esp as esp

de()
esp()

# import all functions and others locally
from greetings import*
greeting_de()
