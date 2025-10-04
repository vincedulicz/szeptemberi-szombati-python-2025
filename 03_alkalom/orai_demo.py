
TANULOK = [
    {"nev": "Teszt Elek", "osztaly": "13I", "eletkor": 19},
    {"nev": "Kiss Béla", "osztaly": "12A", "eletkor": 18},
    {"nev": "Nagy Anna", "osztaly": "11B", "eletkor": 17},
    {"nev": "Szabó Gergő", "osztaly": "10C", "eletkor": 16},
    {"nev": "Varga László", "osztaly": "9D", "eletkor": 15},
    {"nev": "Tóth Zsófia", "osztaly": "12A", "eletkor": 18}
]


def frissit_tanulo(tanulok, nev, uj_kor=None, uj_osztaly=None):
    for tanulo in tanulok:
        if tanulo["nev"] == nev:
            if uj_kor is not None:
                tanulo["eletkor"] = uj_kor
            if uj_osztaly is not None:
                tanulo["osztaly"] = uj_osztaly
            break

frissit_tanulo(TANULOK, "Kiss Béla", uj_kor=19, uj_osztaly="13A")
# print(f"frisített lista {TANULOK}")

def torol_tanulo(tanulok, nev):
    for i, tanulo in enumerate(tanulok):
        if tanulo["nev"] == nev:
            del tanulok[i]
            return True
    return False

# torol_tanulo(TANULOK, "Teszt Elek")


suti = {"nev": "dobostorta", "szeletek": 12, "elfogyott": False}
print(suti["nev"])
print(suti.get("nevv"), "n/a")


# for kulcs, ertek in suti.items():
#    print(kulcs, "értéke: ", ertek)



gyumik = {
    1: "alma",
    2: "körte",
    3: "szilva",
    12: "alma",
    23: "körte",
    32: "szilva",
    41: "alma",
    42: "körte",
    34: "szilva"
}

# {'alma': [1, 12, 41] ....}


csoportok = {}
for kulcs, ertek in gyumik.items():
    csoportok[ertek] = csoportok.get(ertek, []) + [kulcs]

# print(csoportok)


# *tobbi = *args
def legkisebb(elso, *tobbi):
    acc = elso
    print(type(tobbi))

    for x in tobbi:
        if x < acc:
            acc = x
    return acc


# print(legkisebb(3,4,2,-5,65,54,-8,4))


def try_catch_minta():
    try:
        szam = int(input("adj meg egy számot: "))
        print(f'szám négyzete {szam ** 2}')
    except Exception as e:
        print(e)
        print("nem szám")


try:
    oszto = int(input("mennyivel osszam a 10-et? "))
    print(f'az eredmény: {10 / oszto}')
except ZeroDivisionError as e:
    print(f'hiba - {e} - nullával nem lehet osztani')
except ValueError as e:
    print("ez nem szám")
finally:
    print("ez mindig lefut")



try:
    oszto = int(input("mennyivel osszam a 10-et? "))
    print(f'az eredmény: {10 / oszto}')
except (ZeroDivisionError, ValueError) as e:
    print(f'hiba: {e}')
finally:
    print("ez még mindig mindig tényleg lefut")