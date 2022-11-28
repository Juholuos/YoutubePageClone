from tkinter import E

print("Tervetuloa pelaamaan arvauspeliä!")

pelaaminen = input("Haluatko pelata? (Kyllä/ei): ")
if pelaaminen.lower() != "kyllä":
    quit()

print("Selvä, aloitetaan ensimmäisellä kysymyksellä.")
pisteet = 0

nimenkysyntä = input("Mikä on sinun nimesi? ")
print("Hieno nimi, " + nimenkysyntä + "!")
print()
print("Mennään seuraavaan kysymykseen.")
print()

vastaus = input("Kuinka monta silmää ihmisellä normaalisti on?: ")
if vastaus == "2":
        print("Oikein")
        pisteet += 1
else:
        print("Väärin, ihmisellä on 2 silmää.")

vastaus = input("Onko Coca Cola hyvää?: ")
if vastaus.lower() == "kyllä":
        print("Oikein")
        pisteet += 1
else:
        print("Väärin, kokis on hyvää")

vastaus = input("Kannattaako A2-pyörää hankkia?: ")
if vastaus.lower() == "kyllä":
        print("Oikein")
        pisteet += 1
else:
        print("Väärin, aina kannattaa")

vastaus = input("Onko Yamaha hyvä?: ")
if vastaus.lower() == "kyllä":
        print("Oikein")
        pisteet += 1
else:
        print("Väärin!")

if pisteet == 4:
    print("Täydellistä, vastasit "+str(pisteet)+" kysymykseen oikein")
if pisteet == 3:
    print("Melkein täydellistä, vastasit "+str(pisteet)+" kysymykseen oikein")
if pisteet == 2:
    print("Ihan hyvä, vastasit "+str(pisteet)+" kysymykseen oikein")
if pisteet < 2:
    print("Ensi kerralla paremmin, vastasit "+str(pisteet)+" kysymykseen oikein")
print("Se on " +str(round(pisteet/4) * 100) + " prosenttia.")









