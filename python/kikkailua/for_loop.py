from time import sleep


for x in ("husse"):
    print (x)

#sleep(1)

print("\n" * 10)

for x in ["yamaha", "husse", "beta"]:
    if x == "husse":
        continue
    print (x)
    #sleep(0.5)

print("\n" * 10)


for x in range(6):
    if x == 4:
        break
    print(x)


print("\n" * 10)


for x in range(2, 30, 3):
    print(x)

print("\n" * 10)


parhaat_mopomerkit=["yamaha", "husse", "beta"]
värit = ["sininen", "punainen", "keltainen"]
for y in parhaat_mopomerkit:
    for x in värit:
        print(x, y)


viesti = "Moi mitä kuuluu?"
viesti2 = viesti.split()

