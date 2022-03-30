
# Define a string 
course_name = "Python Schulung"
course_name = 'Python Schulung'
print(course_name, type(course_name))

# Multi-Line String
message = """Hallo Thomas
wie geht es dir ?
schöne Grüße
Sven"""

print(message)

###################################################
# functions 
course_name = "Einfühung in Python"
#len() # length
print(len(course_name)) # 19
print()



###############################################
# Slicing
course_name = "Einfühurng in Python"
print(course_name[0])
print(course_name[1])
print(course_name[-1])
print(course_name[0:9]) # Einführun
print(course_name[0:10]) # Einführung
print(course_name[14:19]) # Pytho
print(course_name[14:20]) # Python
print(course_name[14:2000]) # Python
print(course_name[-21:-10]) # Einführung
print(course_name[-6:0]) # empty

# Lösung
print(course_name[-6:]) # bis Ende
print(course_name[:10]) # Vom Beginn
print(course_name[:]) # complete
print(course_name) # complete

print(course_name[0:10:2]) # step 2
print()

##################################################
# String Methods:   Methods = DOT FUNCTIONS
course_name = "     pyTHoN proGramMIeruNG     "
print(course_name)

print(course_name.upper())
print(course_name.lower())
print(course_name.title()) # Python Programmierung
print(course_name.capitalize()) # PPython programmierung
print(course_name.strip())   # delete white space (begin, end) of the string
print(course_name.find("pro"))   # index where pro starts: 12
print(course_name.replace("py", "jy"))   # replace the first match

print(course_name) # original version


# Method Chain
#~~~~~~~~~~~~~~~~~~

course_name = course_name.upper()
print(course_name)

course_name = course_name.strip()
print(course_name)

# Better
print(course_name.upper().strip())
print(course_name.strip().upper())
print()

# String Formatting
#~~~~~~~~~~~~~~~~~~~~~
first_name = "Thomas"
last_name = "Meier"

full_name = first_name + " " + last_name # string concatenation

print(first_name, last_name)
print(full_name)

# String Formatting
#~~~~~~~~~~~~~~~~~~~
print("First Name:{}  Last Name :{}".format(first_name, last_name)) # old way

print(f"First Name: {first_name}  Last Name:{last_name}") # new way



# Escaping, Ignoring "", '' ,  \"   \'  \\
# \n: New Line ,  \t: TAB
#~~~~~~~~~~~~~~~~~~~~~~~
# Mohamed sagte "Guten Morgen" heute
# Mohamed sagte 'Guten Morgen' heute
# Mohamed sagte \Guten Morgen\ heute

print("Mohamed sagte \"Guten Morgen\" heute")
print('Mohamed sagte \'Guten Morgen\' heute')
print('Mohamed sagte \\Guten Morgen\\ heute')

print("Python\nJava")
print("Python\tJava")
