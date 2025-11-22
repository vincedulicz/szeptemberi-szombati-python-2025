class Iskola:
    def __init__(self, nev):
        self.nev = nev
        self.osztalyok = []

    def add_osztaly(self, osztaly):
        for existing_osztaly in self.osztalyok:
            if existing_osztaly.nev == osztaly.nev:
                print(f'hiba: már létezik a(z) {osztaly.nev} ...')
                return

        self.osztalyok.append(osztaly)
        print(f'{osztaly.nev} osztály sikeres hozzáadás')

    def iskola_info(self):
        print(f'iskola: {self.nev}')
        for osztaly in self.osztalyok:
            osztaly.osztaly_info()
            print("...")