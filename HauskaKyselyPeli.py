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
sleep(2)
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
                if kuollut == True:
                        print("Peli päättyi!")
                        uudelleen = input("Haluatko yrittää uudelleen? (K/E): ")
                        if uudelleen == "K":
                                sleep(1)
                                print("Heräät varastosta.\n")
                                mixer.music.rewind()
                                sleep(1)
                                main()
                        else:
                                print("Heippa")
                                quit()
        elif kysymys1 ==("B"):
                sleep(1)
                print("Tutkiessasi huonetta huomaat, että nappaaja ei tyhjentänyt taskujasi ja löydät linkkuveitsen, jolla saat leikattua kätesi vapaiksi.\n")  
                sleep(1)
        else:
                print("Väärä vastaus, yritä uudelleen")
                sleep(1)
                main()

main()
###########################################################################################################################################################################################
def toinen():
        print("----------------------------------------------\n")
        sleep(1)
        print("Vapauduttuasi liikut varovasti oven luokse kuuntelemaan onko sieppaaja lähellä.\n")
        sleep(1)
        print("Oven takaa kuuluu ääniä.\n")
        sleep(1)
        kysymys2 = input("(A) Odota hetki oven takana jos sieppaaja lähtisi muualle / (B) Ota viereinen metallitanko aseeksi ja houkuttele sieppaaja luoksesi: ")
        if kysymys2 == "A": 
                sleep(1)
                print("Sieppaaja lähtee ovesta ulos ja kuulet auton käynnistyvän")
                sleep(1)
                print("Hiivit toiseen huoneeseen ja saat selville, että sieppaaja on poliisin etsimä murhaaja.")
                sleep(1)
                print("Sinun pitää alkaa valmistautua puolustamaan itseäsi!")
        
        elif kysymys2 == "B":
                print("Sieppaaja tulee huoneeseen, mutta et saa yllätettyä häntä, ja hän ampuu sinut.")
                kuollut = True
                if kuollut == True:
                        print("Peli päättyi!")
                        uudelleen = input("Haluatko yrittää uudelleen? (K/E): ")
                        if uudelleen == "K":
                                sleep(1)
                                print("Heräät varastosta.")
                                main()
                        else:
                                print("Heippa")
                                quit()
                sleep(1)
        
              
        else: 
                print("Väärä vastaus, yritä uudelleen")
                toinen()


toinen()

def kolmas():
        print("Helpointa olisi lähteä ovesta ulos, mutta se on lukossa myös sisältäpäin. Näet myös että pihalla vartioi iso koira. \n")
        sleep(1)
        print("Ikkunoistakaan ei voi karata paksujen kaltereiden takia.")
        sleep(1)
        print("Mietit nyt, kuinka saisit voitettua hänet")
        kysymys3 = input("(A) Ota puukko ja odota että hän palaa. / (B) Ota puukko ja mene takaisin huoneeseesi ja esitä että olet edelleen sidottu: \n")
        if kysymys3 == "A":
                sleep(1)
                print("Hänen astuessaan ovesta saat lyötyä häntä, mutta nappaaja ampuu sinut \n")
                kuollut = True
                if kuollut == True:
                        print("Peli päättyi!")
                uudelleen = input("Haluatko yrittää uudelleen? (K/E): ")
                if uudelleen == "K":
                        sleep(1)
                        print("Heräät varastosta.")
                        main()
        elif kysymys3 == "B":
                print("Nappaaja palaa asuntoon ja tulee veitsen kanssa luoksesi. \n")
                sleep(1)
                print("Hän kuiskaa korvaasi tappavasi sinut")
                kysymys4 = input("Lyötkö häntä nyt? (A) Odota vielä / (B) Lyö: ")
                if kysymys4 == "A":
                        print("Yhtäkkiä hän iskee veitsellä sinua")
                        kuollut = True
                        if kuollut == True:
                                print("Peli päättyi!")
                        uudelleen = input("Haluatko yrittää uudelleen? (K/E): ")
                        if uudelleen == "K":
                                sleep(1)
                                print("Heräät varastosta.")
                                main()
                elif kysymys4 == "B":
                        sleep(1)
                        print("Isket selkäsi takaa veitsen hänen kaulaansa ja nappaaja kaatuu maahan.")
                        sleep(1)
                        print("Otat hänen taskuistaan avainnipun ja suuntaat ulos \n")
                        sleep(1)
                        print("Kesytät koiran antamalla sille herkkuja joita löysit eteisestä \n")
                        sleep(1)
                        print("Hyppäät autoon ja ajat poliisilaitokselle paljastamaan murhaajan \n")
                        sleep(2)
                        print("..")
                        sleep(2)
                print("Heräät hikisenä ja mietit olipas ahdistava uni.")
                sleep(1)
                print("Kunnes jalkasi koskettavat kylmää tiililattiaa...")
                sleep(3)
                mixer.music.fadeout()
                print("Kiitos pelaamisesta!")   
kolmas()

      
        
                