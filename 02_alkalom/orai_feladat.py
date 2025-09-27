def szorzat(a, b): # függvény definiálása
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Mindkét paraméternek számnak kell lennie")
    return a * b

szorzat(3, 7) # függvény meghívása


def kisebb_duplaja(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Mindkét paraméternek számnak kell lennie")
    kisebb = a if a < b else b
    return kisebb * 2

kisebb_duplaja(3, 4)

def paros_paratlan(szam):
    if not isinstance(szam, int):
        raise TypeError("Egész számot adj meg!")
    if szam % 2 == 0:
        print(f'ez a szám {szam} páros')
    else:
        print(f"ez a szám {szam} páratlan")


def nagyobbTripla(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Mindkét paraméternek számnak kell lennie")
    nagyobb = a if a > b else b
    return nagyobb * 3


def szokoz_nelkul(szoveg):
    if not isinstance(szoveg, str):
        raise TypeError("A bemenetnek sztringnek kell lennie")
    return szoveg.replace(" ", "")


# print(szokoz_nelkul("ez egy teszter eszrter")) # függvény visszatérési értéke printelve

# response = szokoz_nelkul("ez eg d dg dfg")
# print(response)


def primkereso():
    from math import sqrt

    felso = int(input("Felső határ: "))

    for szam in range(2, felso + 1):
        is_prim = True
        n = 2
        while n <= sqrt(szam):
            if szam % n == 0:
                is_prim = False
                break
            n += 1

        if is_prim:
            print(szam, end=" ")


primkereso()