peli = True
while peli == True:
    salasanatiedosto = open("salainensalasana.txt")
    salainensalasana = salasanatiedosto.read()
    kirjoitettusalasana=input("Syötä salasanasi: ")
    if (kirjoitettusalasana in salasanatiedosto()):
        print("Pääsy hyväksytty!")
        peli = False
    else:
        print("Pääsy hylätty!")