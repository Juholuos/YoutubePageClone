peli = False

def kuolema():
    if peli == True:
        print("kuolit")
        uudelleen = input("Haluatko pelata uudelleen? K/E: ")
        if uudelleen == "K":
            kysymys()
kuolema()


def kysymys():
    kysymys = input("A vai B: ")
    if kysymys == "A":
        print("Valitsit väärin!")
        kuolema()
peli = True
kysymys()

