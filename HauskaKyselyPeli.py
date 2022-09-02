from time import sleep
from pygame import mixer
mixer.init()
mixer.music.load("musiikki.mp3")
mixer.music.play()

kuollut = False
sleep(1)
print("Kävelet illalla yksin tiellä..\n")
sleep(2)
print("Yhtäkkiä kuulet juoksuaskelia takaasi, ja ennenkuin kerkeät edes kääntymään..\n")
sleep(3)
print("Näkösi pimenee, ja seuraavana heräät pimeästä varastosta, kädet sidottuina.\n")
sleep(3)
print("Sinun tehtävänäsi on nyt päättää, mitä teet!\n")
print("----------------------------------------------\n")
sleep(1)
def main():
        print("Huomaat, että maassa on puukko. \n")
        kysymys1 = input("(A) Yritä kerätä se jaloilla / (B) Jatka huoneen tutkimista: ")
        print("\n")
        print("----------------------------------------------\n")
        print("\n")
        if kysymys1 == ("A"):
                print("Et saa nostettua puukkoa jaloilla, ja siitä tuleva kolina herättää toisessa huoneessa olevan nappaajasi huomion.\n")
                sleep(1)
                print("Nappaaja tulee ja viiltää sinulta kurkun auki.")
                kuollut = True
                def kuollut():
                        kuollut = True
                        if kuollut == True:
                                print("Peli päättyi!")
                                uudelleen = input("Haluatko yrittää uudelleen? (K/E): ")
                                if uudelleen == "K":
                                        print("Heräät varastosta.")
                                        main()
                                else:
                                        print("Heippa")
                                        quit()
        elif kysymys1 ==("B"):
                        print("Tutkiessasi huonetta huomaat, että nappaaja ei tyhjentänyt taskujasi ja löydät linkkuveitsen, jolla saat leikattua kätesi vapaiksi.\n")  
                        sleep(1)
                        print("----------------------------------------------\n")
                        sleep(1)
        else:
                print("Väärä vastaus, yritä uudelleen")
                sleep(1)
                main()
main()
###########################################################################################################################################################################################
def toinen():
        print("Vapauduttuasi liikut varovasti oven luokse kuuntelemaan onko sieppaaja lähellä.\n")
        sleep(1)
        print("Oven takaa kuuluu ääniä.\n")
        sleep(1)
        kysymys2 = input("(A) Odota hetki oven takana jos sieppaaja lähtisi muualle / (B) Ota viereinen metallitanko aseeksi ja houkuttele sieppaaja luoksesi: ")
        if kysymys2 == "A": 
                print("Sieppaaja lähtee ovesta ulos ja kuulet auton käynnistyvän")
                sleep(1)
                print("Hiivit toiseen huoneeseen ja saat selville, että sieppaaja on poliisin etsimä murhaaja.")
                sleep(1)
        
        elif kysymys2 == "B":
                print("Sieppaaja tulee huoneeseen, mutta et saa yllätettyä häntä, ja hän ampuu sinut.")
                sleep(1)
        
              
        else: 
                print("Väärä vastaus, yritä uudelleen")
                toinen()


toinen()