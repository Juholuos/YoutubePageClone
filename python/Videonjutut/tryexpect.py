
from decimal import DivisionByZero
'''
#perus
try:
    numero = int(input("Syötä numero: "))
    print(numero)
except:
    print("Väärä syöte")
'''


#monimutkaisempi
try:
    arvo = 10/0
    numero = int(input("Syötä numero: "))
    print(numero)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Väärä syöte")