def obvod(a):
    vysledek = 4*a
    return vysledek

def obsah(a):
    vysledek = a**2
    return vysledek

def objem(a):
    vysledek = a**3
    return vysledek

promena1 = int(input("Zadejte proměnnou 1: "))
print("Pro výpočet obvodu, zadejte 1")
print("Pro výpočet obsahu, zadejte 2")
print("Pro výpočet objemu, zadejte 3")
volba = input("Zadejte Vaši volbu: ")

if volba == "1":
    vysledek = obvod(promena1)
    print("Výsledek je: ", vysledek)
elif volba == "2":
    vysledek = obsah(promena1)
    print("Výsledek je: ", vysledek)
elif volba == "3":
    vysledek = objem(promena1)
    print("Výsledek je: ", vysledek)
else:
    print("Něco jsi zadal špatně :(")