słownik = {
    "Piekarnia" : ["Chleb", "Pączek" , "Bułki"],
    "Warzywniak" : ["Marchew", "Seler", "Rukola"]
}

print(słownik)
for i in słownik:
    produkty = słownik[i]
    print (f"Idę do {i} i kupuję tam: {produkty}")