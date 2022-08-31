from re import S
from this import s


def käännä(lause):
    käännös = ""
    for kirjain in lause:
        if kirjain in "AEIOUYÄÖaeiouäö":
            käännös = käännös + "g"
        else:
            käännös = käännös + kirjain
    return käännös

print(käännä(input("Syötä lause: ")))