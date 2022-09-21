Onnen_numerot = [3, 5, 6, 8, 15]
Kaverit = ["Joona", "Matias", "Eljas"]

#extend
Kaverit.extend(Onnen_numerot)
print(Kaverit)

#kahden listan yhdistäminen (lista.extend(lista2))
Mopomerkit = ["Yamaha1", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit = ["Harley Davidson", "BMW", "Kawasaki"]
Mopomerkit.extend(Moottoripyörämerkit)
print(Mopomerkit)

#listan loppuun lisääminen (lista.append"X")
Mopomerkit1 = ["Yamaha2", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit1 = ["Harley Davidson", "BMW", "Kawasaki"]
Mopomerkit1.append("Solifer\", \"CPI")
print(Mopomerkit1)

#keskelle listaa lisääminen (lista.insert(x, "nimi")
Mopomerkit2 = ["Yamaha3", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit2 = ["Harley Davidson", "BMW", "Kawasaki"]
Mopomerkit2.insert(1, "YZF-R")
print(Mopomerkit2)

#nimen poistaminen listasta (lista.remove(x))
Mopomerkit3 = ["Yamaha4", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit3 = ["Harley Davidson", "BMW", "Kawasaki"]
Mopomerkit3.remove("Yamaha4")
print(Mopomerkit3)

#koko listan poistaminen
Mopomerkit4 = ["Yamaha5", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit4 = ["Harley Davidson", "BMW", "Kawasaki"]
Mopomerkit4.clear
print(Mopomerkit4)

#viimeisen objektin poistaminen (lista.pop)
Mopomerkit5 = ["Yamaha6", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit5 = ["Harley Davidson", "BMW", "Kawasaki"]
Mopomerkit.pop
print(Mopomerkit5)

#etsii nimeä vastaavan indeksin (print(lista.index("nimi")))
Mopomerkit6 = ["Yamaha7", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit6 = ["Harley Davidson", "BMW", "Kawasaki"]
print(Mopomerkit6.index("Suzuki"))

#kuinka monta kertaa nimi toistuu (print(lista.count("nimi")))
Mopomerkit7 = ["Yamaha8", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit7 = ["Harley Davidson", "BMW", "Kawasaki"]
print(Mopomerkit7.count("Suzuki"))

#laittaaa listan aakkosjärjestykseen (lista.sort()) (lista.reverse)
Mopomerkit8 = ["Yamaha9", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit8 = ["Harley Davidson", "BMW", "Kawasaki"]
Mopomerkit8.reverse()
print(Mopomerkit8)

#kopioi listan
Mopomerkit9 = ["Yamaha10", "Suzuki", "Fantic", "Honda"]
Moottoripyörämerkit9 = ["Harley Davidson", "BMW", "Kawasaki"]
Mopomerkit10 = Mopomerkit9.copy()
print(Mopomerkit10)