location = 'Hamburg'


def greeting1(name):
    print('Hallo', name,'von',location) # Global variable READ ONLY

def greeting2(name):

    location = 'Berlin' # Creates a new local variable within Scope of greeting 2
    print('Hallo', name,'von',location)


def greeting3(name):
    global location # Make the global variable writable/ editable
    location = 'Frankfurt'
    print('Hallo', name,'von',location)


greeting1('sven')
greeting2('sara')
greeting3('sara')

# Debugging
#******************
#1- break point setzten 
#2- 4 Icon von oben links clicken (Ausführen und debuggen) ->wird ein Json file erstellt (launch.json)
#3- link auf ausführen clicken 