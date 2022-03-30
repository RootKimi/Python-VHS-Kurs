###################################
# Slicing

course_name = "Einführung in Python"

print (course_name)

print (course_name[0])
print (course_name[1])
print (course_name[0:9])
print (course_name[0:10])
print (course_name[14:19])
print (course_name[14:20])
print (course_name[14:2000])
print (course_name[-21:-10])
print (course_name[-6:0])

#Lösung
print (course_name[-6:]) #bis Ende
print (course_name[:10]) #Von Beginn
print (course_name[:]) #Complete

print (course_name[0:10:2]) #Step 2
print ()

#########
#String Methods
print (course_name.upper())
print (course_name.lower())
print (course_name.title()) #Python Programmierung
print (course_name.capitalize()) #
print (course_name.strip()) #delete white space (begin,end) of the string
course_name = "hgfhdhfjdfdkjfdfjdkjfdkfjdkjfdk"
print (course_name.find("fdfjdk")) # Index where pro starts
print (course_name.replace("py", "jy"))

#Method Chain
###########

course_name = course_name.upper()
print (course_name)

course_name = course_name.strip()
print (course_name)
#Better
print(course_name.upper().strip())
print(course_name.strip().upper())

###String Formatting

first_name = "Thomas"
last_name = "Meier"

full_name = first_name + last_name
print(full_name)
full_name = first_name + " " + last_name #String concatenation 
print(full_name)

#String Formatting
print("first_name:{} last_name:{}".format(first_name, last_name)) # old way
print(f"First Name:{first_name} Last Name:{last_name}") #newway

#Escaping, Ignoring "",'', 

print("Dennis sagte \"Guten Morgen\" heute")
print ("Python\nJava")
print ("Python\tJava")

