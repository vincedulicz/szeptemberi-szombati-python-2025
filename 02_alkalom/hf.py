

def maganhangzo_szamlalo():
    szoveg = input("Adj meg egy szöveget: ")

    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    db = 0

    i = 0
    while i < len(szoveg):
        betu = szoveg[i]
        j = 0
        while j < len(maganhangzok):
            if betu == maganhangzok[j]:
                db += 1
            j += 1
        i += 1

    print(db, "maganhangzó található")

def maganhangzo_szamlalo_better():
    szoveg = input("Adj egy meg egy szöveget: ")
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"

    db = 0

    for betu in szoveg:
        if betu in maganhangzok:
            db += 1

    print(db, "magánhangzó található")


def szamjegyek_osszege():
    szam = input("Adj meg egy egész számot")

    osszeg = 0
    i = 0
    while i < len(szam):
        jegy = ord(szam[i]) - ord("0")
        osszeg += jegy
        i += 1

    print("A számjegek összege: ", osszeg)


def szamjegyek_osszege_better():
    szam = input("Adj meg egy egész számot: ")

    osszeg = 0
    for c in szam:
        if c.isdigit():
            osszeg += int(c)

    print("A számjegyek összege: ", osszeg)


def szavak_visszafele():
    mondat = input("Adj meg egy mondatot: ")

    szavak = []
    szo = ""

    i = 0
    while i < len(mondat):
        if mondat[i] == " ":
            szavak.append(szo)
            szo = ""
        else:
            szo += mondat[i]
        i += 1

    if szo != "":
        szavak.append(szo)

    i = len(szavak) - 1
    while i >= 0:
        print(szavak[i], end=" ")
        i -= 1


def szavak_visszafele_better():
    mondat = input("Adj meg egy mondatot: ")
    szavak = mondat.split()
    szavak.reverse()
    print(" ".join(szavak))


def leggyakoribb_szam():
    szamok = []
    print("Adj meg számokat!: (üres enter end) ")

    while True:
        adat = input()
        if adat == "":
            break
        szamok.append(int(adat))

    legtobb_db = 0
    legtobb_szam = None

    i = 0
    while i < len(szamok):
        aktualis = szamok[i]
        db = 0

        j = 0
        while j < len(szamok):
            if szamok[j] == aktualis:
                db += 1
            j += 1

        if db > legtobb_db:
            legtobb_db = db
            legtobb_szam = aktualis
        i += 1

    print("A leggyakoribb szám: ", legtobb_szam, ":", legtobb_db, "alkalommal")



def leggyakoribb_szam_better():
    from collections import Counter

    print("Adj meg számokat: ")

    szamok = []

    while (adat := input().strip()):
        szamok.append(int(adat))

    if not szamok:
        print("nem adott meg számot")
        return

    counter = Counter(szamok)
    legtobb_szam, legtobb_db = counter.most_common(1)[0]

    print("a leggyakoribb elem: ", legtobb_szam, ":", legtobb_db, "alkalommal")


def jelszo_ellenorzo():
    jelszo = input("Adj meg egy jelszót")

    van_kisbetu = False
    van_nagybetu = False
    van_szam = False

    i = 0
    while i < len(jelszo):
        c = jelszo[i]

        if "a" <= c <= "z":
            van_kisbetu = True
        if "A" <= c <= "Z":
            van_nagybetu = True
        if "0" <= c <= "9":
            van_szam = True

        i += 1

    if len(jelszo) >= 8 and van_kisbetu and van_nagybetu and van_szam:
        print("A jelszó az erős!")
    else:
        print("A jelszó gyenge!")


def jelszo_ellenorzo_better():
    jelszo = input("Adj meg egy jelszót!: ")

    van_kisbetu = False
    van_nagybetu = False
    van_szam = False

    for c in jelszo:
        if c.lower():
            van_kisbetu = True
        elif c.upper():
            van_nagybetu = True
        elif c.isdigit():
            van_szam = True

    if len(jelszo) >= 8 and van_kisbetu and van_nagybetu and van_szam:
        print("A jelszó az erős!")
    else:
        print("A jelszó gyenge!")