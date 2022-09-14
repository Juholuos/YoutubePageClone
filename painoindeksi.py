from time import sleep

PituudenKysyntä = (int(input("Syötä pituus (cm): ")))
PainonKysyntä = (int(input("Syötä paino (kg): ")))



painoindeksi = (PainonKysyntä / ((PituudenKysyntä / 100) * (PituudenKysyntä/100 )))


print("\nPainoindeksisi on " +(str( painoindeksi)))

if (painoindeksi) < 15:
    print("Olet sairaalloisen alipainoinen")
elif 15 > (painoindeksi) > 17:
    print("Olet merkittävästi alipainoinen")
elif 17 > (painoindeksi) > 18.5:
    print("Sinulla on normaalia alhaisempi paino")
elif 18.5 > (painoindeksi) > 25:
    print("Sinulla on normaali paino")
elif 25 > (painoindeksi) > 30:
    print("Sinulla on lievä ylipaino")
elif 30 >(painoindeksi) > 35:
    print("Sinulla on merkittävä ylipaino")
elif 35 > (painoindeksi) > 40:
    print("Sinulla on vaikea ylipaino")
elif (painoindeksi) > 40:
    print("\nSinulla on sairaalloinen ylipaino")


