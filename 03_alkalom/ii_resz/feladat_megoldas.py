import random

def lista_letrehozasa():
    return [
        (i * 0.9 if i % 3 == 0 else i * 1.2 if i % 2 != 0 else i)    # értékadás
        for i in range(1, 36)                                       # ciklus
        if i % 7 != 0                                               # statement
    ]

def lista_kiirasa(lista, uzenet="Lista: "):
    print(f"{uzenet} - {lista}")

def uj_arak_beszurasa(lista):
    szam = int(input("Adj meg egy számot"))
    lista.insert(2, szam)
    lista_kiirasa(lista, uzenet="uj ar beszurasa")

def ar_torlese(lista):
    torlendo = float(input("melyik ár legyen törölve? "))
    if torlendo in lista:
        lista.remove(torlendo)
        print("törölve lett")
    else:
        print("nem található")

def lista_rendezes(lista, reversed=False):
    lista.sort(reversed=reversed)
    lista_kiirasa(lista, "meg lett fordítva")
    # reverse()



DOLGOZOK = [
    {"nev": "Kovács Lili", "eletkor": 21, "pozicio": "barista"},
    {"nev": "Szabó Gergely", "eletkor": 25, "pozicio": "pultos"},
    {"nev": "Tóth Zsófia", "eletkor": 19, "pozicio": "takarító"},
    {"nev": "Varga László", "eletkor": 28, "pozicio": "manager"},
]

POZICIOK = ["barista", "pultos", "takarító", "manager", "szakács"]

def get_dolgozo_by_nev(nev):
    return next((d for d in DOLGOZOK if d["nev"] == nev))

    # for d in DOLGOZOK:
    #     if d["nev"] == nev:
    #         return d
    # return {}

def dolgozok_kiirasa():
    print("\ndolgozók: \n}")
    [print(f'{d["nev"]} '
           f'- {d["eletkor"]} éves'
           f'- {d["pozicio"]}')
     for i, d in enumerate(DOLGOZOK)]

def uj_dolgozo():
    nev = input("add meg neved")
    eletkor = int(input("életkor: "))
    pozicio = random.choice(POZICIOK)
    DOLGOZOK.append({"nev": nev, "eletkor": eletkor, "pozicio": pozicio})
    # TODO: print

def dolgozo_torlese():
    nev = input("név:")
    dolgozo = get_dolgozo_by_nev(nev)
    if dolgozo:
        megerosites = input("tuti? (i/n)").lower()
        if megerosites == "i":
            DOLGOZOK.remove(dolgozo)
            # todo: print
        else:
            pass
            # todo: print
    else:
        pass
            # todo: print


def dolgozo_modositasa():
    nev = input("nev: ")
    dolgozo = get_dolgozo_by_nev(nev)
    if dolgozo:
        kulcs = input("melyik adat modify: ")
        if kulcs in dolgozo:
            uj_ertek = input("mi az")
            if kulcs == "eletkor":
                uj_ertek = int(uj_ertek)
            dolgozo[kulcs] = uj_dolgozo
            # todo: print
        else:
            pass
            # todo: print érvénytelen a key
    else:
        pass
        # todo: print

def dolgozok_program():
    while True:
        print(
            # todo: print
            "\nElérhető parancsok amiket lehet használni: "
            "\nnew"
            "\ndelete"
            "\nmodify"
            "\nquit"
        )

        dolgozok_kiirasa()

        parancs = input("\nMi a parancs? ").strip().lower()

        if parancs == "quit":
            break
        elif parancs == "new":
            uj_dolgozo()
        elif parancs == "delete":
            dolgozo_torlese()
        elif parancs == "modify":
            dolgozo_modositasa()
        else:
            pass
            # todo: print érvénytelen parancs

def main():
    dolgozok_program()


main()


print(f'{DOLGOZOK} - {DOLGOZOK[0]} - {main()} - {dolgozok_program()} - {dolgozo_torlese()} - {dolgozok_program()}')