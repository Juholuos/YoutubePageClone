from re import S
from this import d
peli = False

def eurodollarilasku():
    eurokysyntä = int(input("Syötä Eurot: "))
    lopputulos = eurokysyntä * 1.01
    f"{lopputulos:,}"
    print ("\n%s euroa on %s dollaria." % (eurokysyntä, f"{lopputulos:,}"))

def europuntalasku():
    eurokysyntä = int(input("Syötä Eurot: "))
    lopputulos = eurokysyntä * 0.87
    f"{lopputulos:,}"
    print ("\n%s euroa on %s puntaa." % (eurokysyntä, f"{lopputulos:,}"))

def eurojenilasku():
    eurokysyntä = int(input("Syötä Eurot: "))
    lopputulos = eurokysyntä * 144
    print ("\n%s euroa on %s japanin jeniä." % (eurokysyntä, f"{lopputulos:,}"))
    f"{lopputulos:,}"

def valuutta_1_kysyntä():
    print("\n")
    peli = True
    while peli == True:
        eurot = input("\nHaluatko muuttaa: (A)EUR-USD, (B)EUR-GBD, (C)EUR-JPY?: ")
        if eurot == "A":
            eurodollarilasku()
            peli = False
        if eurot == "B":
            europuntalasku()
            peli = False
        if eurot == "C":
            eurojenilasku()
            peli = False

        kysymys = input("\nHaluatko pelata uudelleen? (K/E): ")
        if kysymys.lower() == ("k"):
            print("Selvä!")
            peli = True
        elif kysymys.lower() == ("e"):
            print("Selvä, heihei!")
        

valuutta_1_kysyntä() 

