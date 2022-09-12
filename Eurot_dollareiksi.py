from re import S
from this import d
peli = False


def valuutta_1_kysyntä():
    print("\n")
    peli = True
    while peli == True:
        eurot = input("\nHaluatko muuttaa: (A)EUR-USD, (B)EUR-GBD, (C)EUR-JPY?: ")
        if eurot == "A":
            eurokysyntä = int(input("Syötä Eurot: "))
            lopputulos = eurokysyntä * 1.01
            print ("\n%s euroa on %s dollaria." % (eurokysyntä, lopputulos))
        if eurot == "B":
            eurokysyntä = int(input("Syötä Eurot: "))
            lopputulos = eurokysyntä * 0.87
            print ("\n%s euroa on %s puntaa." % (eurokysyntä, lopputulos))
        if eurot == "C":
            eurokysyntä = int(input("Syötä Eurot: "))
            lopputulos = eurokysyntä * 144
            print ("\n%s euroa on %s japanin jeniä." % (eurokysyntä, lopputulos))


valuutta_1_kysyntä() 

