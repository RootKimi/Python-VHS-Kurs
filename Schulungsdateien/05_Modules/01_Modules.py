#import greetings
from greetings import*
def app():
    print('Willkommen bei Restaurant xyz')
    print('Choose your languages:')
    print('[1] DE')
    print('[2] EN')
    print('[3] FR')
    print('[4] SP')


    user_language = int (input('>'))


    if user_language == 1:
        greeting_de()
    elif user_language == 2:
        greeting_en()
    elif user_language == 3:
        greeting_fr()
    elif user_language == 4:
        greeting_sp()


app()