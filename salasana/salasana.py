from time import sleep
def main():
    #seuraavaksi teen yrityslaskurin
        salainensalasana = open("salainensalasana.txt")
        salasana = input("Syötä salasana: ")
        if salasana == salainensalasana.read():
            print("Pääsy hyväksytty!")
            sleep(1)
            print("Tiedoston sisältö on seuraavanlainen:")
            sleep(1)
            f = open("salainentiedosto.txt", "r")
            sisältö = f.read()
            print(sisältö)
        else:
            print("Pääsy hylätty!")
            main()
main()