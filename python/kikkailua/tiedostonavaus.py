import os

f = open("testiteksti.txt", "a")
f.write("\nNo nyt tuli enemmän asiaa")
f.close

f = open ("testiteksti.txt", "r")
print(f.read())


if os.path.exists("testiteksti2.txt"):
    os.remove("testiteksti2.txt")
else:
    print("Tiedostoa ei löydy")
    f=open("testiteksti2.txt", "w")
    f.write("\nNo nyt tuli enemmän asiaatia")