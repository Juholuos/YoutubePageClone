from tkinter import E, N
import math

print("Tervetuloa pelaamaan arvauspeliä!")

pelaaminen = input("Haluatko pelata? (Kyllä/ei): ")
if pelaaminen.lower() != "kyllä":
        print("Väärä vastaus")

print("\n")

print("Selvä, aloitetaan ensimmäisellä kysymyksellä.")
pisteet = 0
print("\n" *2)
nimenkysyntä = input("Mikä on sinun nimesi? ")
print("Hieno nimi, " + nimenkysyntä + "!")
print()
print("Mennään seuraavaan kysymykseen.")
print()
print("\n" *2)
vastaus = input("Kuinka monta silmää ihmisellä normaalisti on?: ")
if vastaus == "2":
        print("Oikein")
        pisteet += 1
else:
        print("Väärin, ihmisellä on 2 silmää.")

print("\n")

vastaus = input("Onko Coca Cola hyvää?: ")
if vastaus.lower() == "kyllä" or "joo" or "on":
        print("Oikein")
        pisteet += 1
else:
        print("Väärin, kokis on hyvää")

print("\n")

vastaus = input("Kannattaako A2-pyörää hankkia?: ")
if vastaus.lower() == "kyllä" or "joo" or "kannattaa":
        print("Oikein")
        pisteet += 1
else:
        print("Väärin, aina kannattaa")

print("\n")

vastaus = input("Onko Yamaha hyvä?: ")
if vastaus.lower() == "kyllä" or "joo" or "on":
        print("Oikein")
        pisteet += 1
else:
        print("Väärin!")

print("\n")

if pisteet == 4:
    print("Täydellistä, vastasit "+str(pisteet)+" kysymykseen oikein")
if pisteet == 3:
    print("Melkein täydellistä, vastasit "+str(pisteet)+" kysymykseen oikein")
if pisteet == 2:
    print("Ihan hyvä, vastasit "+str(pisteet)+" kysymykseen oikein")
if pisteet < 2:
    print("Ensi kerralla paremmin, vastasit "+str(pisteet)+" kysymykseen oikein")
print("Se on " +str(pisteet/0.04) + " prosenttia.")











