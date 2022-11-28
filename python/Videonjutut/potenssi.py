#potenssi
print(2**3)

#potenssi funktion avulla

def potenssiin(eksponentti, potenssi):
    tulos = 1
    for index in range(potenssi):
        tulos = tulos * eksponentti
    return tulos
print(potenssiin(3, 2))