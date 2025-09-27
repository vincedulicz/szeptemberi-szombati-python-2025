
"""PI = 3.14
MAX_POOL_CONN = 42
AGE_LIMIT = 18

age = 5
print(f'global var: {age}')

def test_age(age):
    print(f"age: {age}")
    return age < AGE_LIMIT

response = test_age(17)

# print(response)

if response:
    load_verify_odal()
else:
    redirect -> google.com
"""




"""
Egy szám osztói

Alap működés:

Input: 15

Kiemenet:

15 osztói:
1; 3; 5; 15
"""

def szam_osztoi():
    szam = int(input("Írjá be egy egész számot: "))
    osztok = "1"

    n = 2
    while n <= szam // 2:
        print(n)
        if szam % n == 0:
            osztok += "; " + str(n)
        n += 1

    osztok += "; " + str(szam)

    print(str(szam) + " osztói: ")
    print(osztok)


# szam_osztoi()



"""
Tökéletes számok

-> tökéletes szám akkor érvényesül ha önmagánál kisebb osztói összege megegyezik a számmal.
Pl 6 -> 1,2,3 (+) = 6

Input: 6
Tökéletes szám!

Input: 12
Nem tökéletes szám!

input, típuskonverzió, osztók összege, ha osztója + ha nem -> semmit
if osztok osszege == input_szam -> szám:nemaz
"""

def tokeletes_szam():
    szam = int(input("Írj be egy egész számot: "))
    osztok_osszege = 1

    n = 2
    while n <= szam // 2:
        if szam % n == 0:
            osztok_osszege += n
        n += 1

    if osztok_osszege == szam:
        print("tökéletes szám")
    else:
        print("nem az")


# tokeletes_szam()

def tokeletes_szam_felso_hatar():
    felso_hatar = int(input("Tökéletes szám felső határa: "))

    elso_tokeletes_szam = 6
    while elso_tokeletes_szam <= felso_hatar:
        osztok_osszege = 1

        n = 2
        while n <= elso_tokeletes_szam // 2:
            if elso_tokeletes_szam % n == 0:
                osztok_osszege += n
            n += 1

        if osztok_osszege == elso_tokeletes_szam:
            print(f'k: {elso_tokeletes_szam}')

        elso_tokeletes_szam += 1

# tokeletes_szam_felso_hatar()


def string_muveletek():
    szoveg = "6teszter elek békön vacon vákum tomhass tomas hamvas béla 2.0"

    print(len(szoveg))
    print(f'0. index {szoveg[0]}') # [2] [-2] [::2] [::-1]

    print(szoveg.replace("e", "á"))

    if "hamvas" not in szoveg:
        print(":(")
    else:
        print("scientia saacra i.iii.ii")

    print(f'kezdő: {szoveg.startswith("teszter")} | végző: {szoveg.endswith("2.0")}')

    if szoveg.startswith("6"):
        print("számmal kezdődik")
    else:
        print("nem számmal")


def string_muveletek_ii():
    szoveg = "Hello"
    print(szoveg)

    lista = list(enumerate(szoveg))
    print(lista)

    elotag = "törp"
    utotagok_listaja = ["erős", "költő", "morgó", "oltó"]

    for utotag in utotagok_listaja:
        print(elotag + utotag)

    print(utotagok_listaja[2:4])

    szoveg = "szöveg"
    print(szoveg.find("öv"))

# string_muveletek_ii()


def var_swapping():
    a = 5
    b = 4

    print(f'a: {a} ; b: {b}')

    tmp = a
    a = b
    b = tmp

    print(f'a: {a} ; b: {b}')

    a, b = b, a
    # tmp -> memory

    print(f'a: {a} ; b: {b}')


# var_swapping()


# todo: felsőhatárig
def primkereso():
    from math import sqrt

    szam = int(input("Szám: "))

    if szam == 1:
        print("def szerint ez nem prím")
    else:
        is_prim = True

        n = 2
        while n <= sqrt(szam):
            if szam % n == 0:
                is_prim = False

            n += 1

        if is_prim:
            print("prím")
        else:
            print("nem prím")


# primkereso()

