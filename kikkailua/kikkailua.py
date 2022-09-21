viesti = "Moi mitä kuuluu?"
viesti2 = viesti.split()
print(viesti2)

import datetime

x = datetime.datetime(2020, 5, 17)

def voitolle():
    global voitollejääneetrahat
    voitollejääneetrahat = 500 + 500
voitolle()
print(500 + (voitollejääneetrahat))

