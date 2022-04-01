# Ubung : Uhrzeit:
#~~~~~~~~~~~~~~~~~~~~~~~~~~

# Code

for hour in range(24):
    for minute in range(60):
        for sec in range(60):
            #print(f"{hour}:{minute}:{sec}")
            print(f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(sec).zfill(2)}")
