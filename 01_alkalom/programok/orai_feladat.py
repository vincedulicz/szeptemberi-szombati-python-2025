

def alap_operatorok():
    a = 4
    b = 3

    eredmeny = "eredmény"
    eredmeny_ = "eredmény_"

    if eredmeny == eredmeny_:
        print("\o/ két str megegyezik")
    elif eredmeny != eredmeny_:
        print("nem egyeznek")
    else:
        print("valami más")

    if a > b:
        print("a > b")
    elif b > a:
        print("b > a")
    elif b == a:
        print("b == a")
    else:
        print("más...")


# alap_operatorok()


def print_olvashatosag():
    i = 0
    szo = "python"

    print("{}. elem {}. szo".format(i, szo))                    # olvasható(?)

    print("A szó " + str(i + 1) + ". betűje: " + szo[i] + ".")  # kevésbé olvasható

    print("A szó ", str(i), ". betűje", szo[i], ".", sep="")    # olvashatóbb


# print_olvashatosag()

def print_olvashatobb():
    i = 0
    szo = "python"

    formazott = f"A szó {i}. betűje: {szo[i]}"                  # legtisztább

    return formazott

p = print_olvashatobb()
# print(p)


def osszeadas():
    egyik = input("Írj bele szöveget: ")
    masik = input("Írj bele mégegyszöveget: ")

    print("egyik+masik->")
    print(egyik + masik)


# osszeadas()


def szamok_osszeadasa():
    egyik = int(input("szam1: "))
    masik = int(input("szam2: "))

    print(egyik + masik)


# szamok_osszeadasa()


def szakasz_hossz_koordinata():
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))

    import math

    hossz = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    print(hossz)


# szakasz_hossz_koordinata()


def is_operator():
    a = [1, 2, 3]
    b = list(a)

    print(f'a: {a} | b: {b}')

    print("a == b", a == b) # tartalomnak az összehasonlítása
    print("a is b", a is b) # objektumazonosság összehasonlítás

    b.append(4)
    b.remove(1)

    print(a)
    print(b)

# is_operator()


def is_operator_():
    x = [1, 2, 3]
    y = [1, 2, 3]

    x = y

    print("x == y", x == y)
    print("x is y", x is y)

    y.append(4)
    print(x)

    print(type(x))
    print(type(y))

    print(id(x))
    print(id(y))


# is_operator_()


def szokoz_nelkul():
    szoveg = "H e l l o , v i l á g !"
    spacenelkul = ""

    for i in szoveg:
        if i != ' ':
            spacenelkul += i

    print(spacenelkul)


# szokoz_nelkul() # identálás szerepe !


def palindrom():
    szoveg = "Indul a görög aludni."

    csakbetuk = ""
    for i in szoveg:
        if i.isalnum():
            csakbetuk += i.lower()

    print(csakbetuk)

    hibas = False
    index = 0
    hossz = len(csakbetuk)
    while index < hossz / 2:
        if csakbetuk[index] != csakbetuk[hossz - 1 - index]:
            hibas = True
            break
        index += 1

    if hibas:
        print("A megadott szó nem palindrom")
    else:
        print("A megadott szó palindrom")

    print(csakbetuk)

    if csakbetuk != csakbetuk[::-1]:
        print("XXX a megadott szó nem palindrom")
    else:
        print("XXX a megadott szó palindrom")


# palindrom()


def referencia_lista():
    def modify_list(lst):
        lst.append(4)
        print(f'belső lista: {lst}') # [1, 2, 3, 4]

    our_list = [1, 2, 3]
    modify_list(our_list) # referencia átadás
    print(f'külső lista: {our_list}')


# referencia_lista()


def feladatok_pontok():
    pontok = []
    be = input("Pont? ")

    while be != "": # üres string esetén kilépünk
        pontok.append(int(be))
        be = input("Pont? ")

    print(pontok)

    db_max = 0 # számláló, hogy hányszor futott a belső ciklus
    for keresett in range(0, 10 + 1): # 0-10 pontig melyikből mennyi van
        db = 0

        for pont in pontok:
            db_max += 1
            if pont == keresett:
                db += 1

        print(f'{keresett} p, {db}')

    print(db_max)

# feladatok_pontok()



def paros_e_rossz():
    szam = 3

    print("bool: ", szam % 2 == 0)

    if szam % 2 == 0: # bool
        print("páros")
    else:
        print("páratlan")

    val = 0

    if val == 0: # bool
        return True
    else:
        return False


# paros_e_rossz()


def paros_e_jo():
    szam = 3
    return szam % 2 == 0

def paros_e_teszt():
    if paros_e_jo():
        print("páros")
    else:
        print("páratlan")


paros_e_teszt()
