"""

Írj egy gyenge_jelszavak nevű függvényt,
amely egy jelszavakat tartalmazó listát kap paraméterül!

A függvény adja vissza ezek közül a gyenge jelszavakat egy listában!
Egy jelszót gyengének tekintünk, ha az alábbi feltételek közül legalább 1 érvényes rá:

•	A jelszó rövidebb, mint 5 karakter
•	A jelszó nem tartalmaz számjegy karaktert
•	A jelszó tartalmazza a jelszo vagy 123 szövegek valamelyikét bármilyen formában
    (a kis- és nagybetűket nem megkülönböztetve).

Írd ki az erős jelszavakat egy txt fájlba, valamint a gyenge jelszavakat is.



Írj eros_jelszavak nevű függvényt, melynek paramétere a jelszó hossza (alapból 8)
illetve a másik paraméter, hogy hány jelszót állítson elő (alapból 1),
amely egy jelszavakat tartalmazó listával tér vissza.

A jelszót a 0..9-ig valamint az angol abc a..z
és általad választott speciális karakterek kombinációja alkossa.

"""

import string
import random

def gyenge_jelszavak(jelszavak):
    """ gyenge jelszavak szűrése listába """

    gyenge_jelszavak = []

    for jelszo in jelszavak:
        van_szam = is_digit_in_password(jelszo)

        jelszo_kisbetu = jelszo.lower()
        if len(jelszo) < 5 or not van_szam or "jelszo" in jelszo_kisbetu or "123" in jelszo_kisbetu:
            gyenge_jelszavak.append(jelszo)

    return gyenge_jelszavak

def is_digit_in_password(jelszo):
    """ megnézi van-e szám a jelszóban """

    # alma2
    for karakter in jelszo:
        # 1: a 2: l 3: m 4: a 5: '2'
        if karakter.isdigit():
            return True

    return False

def is_digit_in_password_alter(jelszo):
    """ alter """

    # regex, map, any, next, stb......

    # jelszo = "abc123"

    print("halmaz teszre: ", set(jelszo) == {'a', 'b', 'c', '1', '2', '3'})

    print("halmaz értékei: ", set(jelszo).intersection(string.digits))

    print("van e szám: ", bool(set(jelszo).intersection(string.digits)))

    return bool(set(jelszo).intersection(string.digits))

def eros_jelszavak(pw_hossz=8, mennyiseg=1):
    """ erős jelszó generáló függvény """

    eros_jelszavak = []

    karakterek = string.ascii_letters + string.digits + string.punctuation

    for _ in range(mennyiseg):
        jelszo = ""

        for _ in range(pw_hossz):
            jelszo += random.choice(karakterek)

        eros_jelszavak.append(jelszo)

    return eros_jelszavak

def jelszavak_fajlba_irasa(file_name, jelszavak):
    """ jelszavak fájlba írása """

    try:
        with open(file_name, "w", encoding='UTF-8') as file:
            for jelszo in jelszavak:
                file.write(jelszo + "\n")
    except (IOError, Exception) as e:
        print(f'error: {e}')


def main():
    jelszavak = ["root", "KwkWWW2025", "H0sszoJelsz0GoesBrrrrrr", "admin123", "asdqwe"]

    gyenge_jelszavak_list = gyenge_jelszavak(jelszavak)

    eros_jelszavak_list = eros_jelszavak(12, 7)

    jelszavak_fajlba_irasa('gyenge_jelszavak.txt', gyenge_jelszavak_list)
    jelszavak_fajlba_irasa('eros_jelszavak.txt', eros_jelszavak_list)

    print(f"Program vége lefutott ennyi... {jelszavak} :)")


main()





