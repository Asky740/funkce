def scitani(a, b):
    vysledek = a+b
    return vysledek


promena1 = input("Zadejte promennou 1: ")
promena2 = input("Zadejte promennou 2: ")

promena1 = int(promena1)
promena2 = int(promena2)

vysledek = scitani(promena1, promena2)

print("Výsledek je: ",str(vysledek))
