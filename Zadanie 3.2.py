print("Zadanie 1:")
słownik = {
    "Piekarnia" : ["Drożdżówka", "Pączek" , "Bułki"],
    "Warzywniak" : ["Marchew", "Seler", "Cebula"]
}
łączna_liczba_produktów = 0
for i in słownik:
    produkty = słownik[i]
    print (f"Idę do {i} i kupuję tam: {produkty}")
    łączna_liczba_produktów = łączna_liczba_produktów + len(produkty)
print(f"W sumie kupuję {łączna_liczba_produktów} produktów.")
