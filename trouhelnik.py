def obvod(a, b, c):
    vysledek = a+b+c
    return vysledek

def obsah(a, b):
    vysledek = (a*b)/2
    return vysledek

print("Pro výpočet obvodu, zadejte 1")
print("Pro výpočet obsahu, zadejte 2")
volba = input("Zadejte Vaši volbu: ")

if volba == "1":
    promena1 = int(input("Zadejte stranu 1: "))
    promena2 = int(input("Zadejte stranu 2: "))
    promena3 = int(input("Zadejte stranu 3: "))
    vysledek = obvod(promena1, promena2, promena3)
    print("Výsledek je: ", vysledek)
elif volba == "2":
    promena1 = int(input("Zadejte proměnnou 1 (strana): "))
    promena2 = int(input("Zadejte proměnnou 2 (výška): "))
    vysledek = obsah(promena1, promena2)
    print("Výsledek je: ", vysledek)
else:
    print("Neumíš číst :/")