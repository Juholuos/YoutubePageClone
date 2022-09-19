salasana = True
while salasana == True:
    salainensalasana = open("salainensalasana.txt")
    salasana = input("Syötä salasana: ")
    if(salasana in salainensalasana.read()):
        print("Pääsy hyväksytty!")
    else:
        print("Pääsy hylätty!")
    