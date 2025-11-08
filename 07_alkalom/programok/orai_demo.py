

class LAMPA:
    piros = 1
    sarga = 2
    sargazold = 3
    zold = 4


print(LAMPA.piros)


class Menu:
    kilepes = 0
    stat = 1
    kiiras = 2
    beolvas = 3


def stat():
    print("stat goes brr")


def menu():
    while True:
        choice = input("választás 0-3")
        try:
            choice = int(choice)
        except ValueError:
            print("nem szám")
        if Menu.kilepes == choice:
            break
        elif Menu.beolvas == choice:
            print("......")
        elif Menu.stat == choice:
            stat()
        else:
            print("...")