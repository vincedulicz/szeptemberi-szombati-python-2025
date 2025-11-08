from abc import ABC, abstractmethod


class Jarmu(ABC):
    def __init__(self, sebesseg):
        self.sebesseg = sebesseg

    def alap_info(self):
        return f'Sebesség: {self.sebesseg}'

    @abstractmethod
    def halad(self):
        pass

    @abstractmethod
    def fogyasztas(self):
        pass


class Auto(Jarmu):
    def __init__(self, sebesseg, utasok, tipus):
        super().__init__(sebesseg)
        self.utasok = utasok
        self.tipus = tipus

    def halad(self):
        return f'{self.sebesseg} km/h halad az autó'

    def fogyasztas(self):
        return 'nincs fogyasztás'

    def tipus_info(self):
        return f'{self.tipus} ez a típus'

    def utasok_adat(self):
        return f'{self.utasok} db ember'

    def alap_info(self):
        return f'{self.tipus} + {self.utasok}'


class ElektromosAuto(Auto):
    def __init__(self, sebesseg, utasok, tipus, akku_kapacitas):
        super().__init__(sebesseg, utasok, tipus)
        self.akku_kapacitas = akku_kapacitas

    def halad(self):
        return f'elektromos autó {self.sebesseg} km/h halad'

    def akku_info(self):
        return f'kapacitás: {self.akku_kapacitas}'


e_auto = ElektromosAuto(120, 5, "tezsla", 12)
print(e_auto.tipus_info())
print(e_auto.halad())

a = Auto(200, 4, "ford")
print(a.alap_info())
print(a.utasok_adat())

masik = Auto(2000, 40, "ford2")
print(masik.alap_info())
print(masik.utasok_adat())
