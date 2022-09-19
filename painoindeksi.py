<<<<<<< HEAD
import webbrowser
from time import sleep
PituudenKysyntä = float(input("Syötä pituus (cm): "))
PainonKysyntä = float(input("Syötä paino (kg): "))
print("\n")

painoindeksi = (PainonKysyntä / ((PituudenKysyntä / 100) * (PituudenKysyntä/100 )))

print("Sinun painoindeksisi on " +(str(round(painoindeksi, 2))))


if (painoindeksi) < 15:
    print("Olet sairaalloisen alipainoinen.")
elif 15 < (painoindeksi) < 17:
    print("Olet merkittävästi alipainoinen.")
elif 17 < (painoindeksi) < 18.5:
    print("Sinulla on normaalia alhaisempi paino.")
elif 18.5 < (painoindeksi) < 25:
    print("Sinulla on normaali paino.")
elif 25 < (painoindeksi) < 30:
    print("Sinulla on lievä ylipaino.")
elif 30 <(painoindeksi) < 35:
    print("Sinulla on merkittävä ylipaino.")
elif 35 < (painoindeksi) < 40:
    print("Sinulla on vaikea ylipaino.")
elif (painoindeksi) > 40:
    print("Sinulla on sairaalloinen ylipaino.")

sleep(1)
print("\n")
nettisivu=input("Haluatko mennä aiheeseen liittyvälle nettisivulle? (K/E) ")
if nettisivu == ("K"):
    print("Selvä!")
    sleep(1)
    webbrowser.open_new("https://thl.fi/fi/web/elintavat-ja-ravitsemus/lihavuus/painonhallinta")
else:
    print("Selvä.")
=======
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


>>>>>>> 4fd80855627032ae679b6955e306a6db03ffd39c
