
def main():
    salainensalasana = open("salainensalasana.txt")
    salasana = input("Syötä salasana: ")
    if salasana == salainensalasana.read():
        print("Pääsy hyväksytty!")
    else:
        print("Pääsy hylätty!")
        main()
main()
    