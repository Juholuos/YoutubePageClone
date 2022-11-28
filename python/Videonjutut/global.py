#global avainsanan avulla voidaan saada funktion sisällä tehdyt muuttujat funktion ulkopuolelle!
def voitolle():
    global voitollejääneetrahat
    #määritetään voittorahat globaliksi
    voitollejääneetrahat = 500 + 500
voitolle()

print(500 + (voitollejääneetrahat))
#muuttujaa voidaan käyttää
