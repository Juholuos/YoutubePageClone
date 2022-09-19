from time import sleep

def main():
    salainensalasana = open("salainensalasana.txt")
    salasana = input("Syötä salasana: ")
    if salasana == salainensalasana.read():
        print("Pääsy hyväksytty!")
        sleep(2)
        
    else:
        print("Pääsy hylätty!")
        main()
main()
    