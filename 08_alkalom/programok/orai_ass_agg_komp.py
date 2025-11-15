class DefaultStandard(object):
    def __init__(self):
        self.publikus_adattag = 0
        self._protected = 1
        self.__privat_adattag = False

ds = DefaultStandard()


class MasikStandard(DefaultStandard):
    pass

ms = MasikStandard()


""" asszociáció """
class Lada:
    def __init__(self, kapacitas):
        self.kapacitas = kapacitas

    def kihasznaltsag_vizsgalo(self, dobozok):
        tomeg = sum([doboz.tomeg for doboz in dobozok])
        return tomeg / self.kapacitas * 100


class Doboz:
    def __init__(self, tomeg):
        self.tomeg = tomeg


lada = Lada(40)
megrendeles = [Doboz(10), Doboz(50)]

print(f'{lada.kihasznaltsag_vizsgalo(megrendeles):.0f}%-os kihasználtság')


""" aggregáció """
class Szerelo:
    def __init__(self, nev):
        self.nev = nev

    def __str__(self):
        return self.nev

    def szerel(self):
        print(f'{self.nev} brutál mód szerel')


class Kulcs:
    def __init__(self, sorozatszam):
        self.sorozatszam = sorozatszam
        self._data = True

    @property
    def data(self):
        print("getter")
        return self._data


class Gepjarmu:
    def __init__(self, alvazszam, kulcs_serial, szerelo_obj=None):
        self.alvazszam = alvazszam
        self.szerelo_obj = szerelo_obj          # aggregáció
        self.kulcs_obj = Kulcs(kulcs_serial)    # kompozició

    def __str__(self):
        if self.szerelo_obj:
            return f'gépjármű alv {self.alvazszam}' \
                   f' szerelő név: {self.szerelo_obj.nev}' # property :)
        else:
            return f'gép'

    def szereles_nagyon_szerelek(self):
        if self.szerelo_obj:
            self.szerelo_obj.szerel()
        else:
            print("nincs mit javítani vagy nincs kivel...")

    def analyze_data(self):
        # analyze....... -> []
        return self.kulcs_obj.data


szerelo = Szerelo("Szerelo Peter")
szerelo_rossz = Szerelo("Rossz Reszel")

print(szerelo, szerelo_rossz)

gepjarmu = Gepjarmu("ALV0123", "KLCS0123", szerelo)

gepjarmu.szereles_nagyon_szerelek()

print(gepjarmu.analyze_data())
