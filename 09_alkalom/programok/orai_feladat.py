
import json
import re
from abc import ABC, abstractmethod



"""
Magyarázat:

if adat["faj"] == "Emlős":
    allat = Emlos(...)
elif adat["faj"] == "Madár":
    allat = Madar(...)

Ez nem túl jó, mert:

ha új faj jön → át kell írni a kódot

tele van if-else szerkezettel...

nem skálázható

mindenhol ismétlődik a logika

A Factory azt mondja:
-ne te döntsd el, majd én megmondom, melyik osztályt példányosítjuk”


új faj? → csak bekerül a dict-be, kész

a kódod tiszta marad

JSON betöltéséhez tökéletes

Plug-and-play barát :)

nincs if-erdő

Fogalom:

A Factory tervezési minta célja, hogy a példányosítás logikáját elkülönítse a többi kódrészlettől.
Egy központi „gyár” objektum dönt arról, hogy egy adott bemeneti adat alapján melyik konkrét osztály példányosuljon.

"""


class Allat(ABC):
    FAJ = None

    def __init__(self, nev, kor, **extra):
        self.nev = nev
        self.kor = kor
        self.extra = extra

    @property
    def faj(self):
        return self.FAJ

    @abstractmethod
    def hangot_ad(self):
        pass

    def allat_adatok(self):
        return {
            "nev": self.nev,
            "faj": self.faj,
            "kor": self.kor,
            **self.extra
        }

    def __str__(self):
        return f'{self.faj}: {self.nev}'


class Emlos(Allat):
    FAJ = "Emlős"

    def hangot_ad(self):
        return f'{self.nev} ugat'


class Madar(Allat):
    FAJ = "Madár"

    def hangot_ad(self):
        return f'{self.nev} károg'


class Hullo(Allat):
    FAJ = "Hüllő"

    def hangot_ad(self):
        return f'{self.nev} sziszeg'


class AllatFactory:
    TIPUSOK = {
        "Emlős": Emlos,
        "Madár": Madar,
        "Hüllő": Hullo
    }

    @staticmethod
    def letrehoz(adat: dict):
        faj = adat.get("faj")
        cls = AllatFactory.TIPUSOK.get(faj)
        if not cls:
            raise ValueError(f"Ismeretlen állatfaj: {faj}")

        extra = {k: v for k, v in adat.items()
                 if k not in ("nev", "kor", "faj")}

        return cls(adat["nev"], adat["kor"], **extra)


class Allatkert:
    def __init__(self):
        self._allatok = []

    @property
    def allatok(self):
        return self._allatok

    def __iadd__(self, allat):
        """
        += művelet
        """
        if not isinstance(allat, Allat):
            raise TypeError("Csak Allat példány adható hozzá.")
        self._allatok.append(allat)
        return self

    def allat_eltavolitas(self, allat):
        try:
            self._allatok.remove(allat)
            return True
        except ValueError:
            return False

    def osszes_allat(self):
        return [a.allat_adatok() for a in self._allatok]

    def mentes_fajlba(self, fajlnev):
        try:
            with open(fajlnev, "w", encoding="utf-8") as f:
                json.dump(self.osszes_allat(), f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f'Hiba mentéskor: {e}')

    def betoltes_fajlbol(self, fajlnev):
        adatok = self.json_beolvasas(fajlnev)
        for a in adatok:
            try:
                self._allatok.append(AllatFactory.letrehoz(a))
            except Exception as e:
                print(f"Hibás adat: {e}")

    @staticmethod
    def json_beolvasas(fajlnev):
        try:
            with open(fajlnev, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

"""
any() → van-e egyáltalán ilyen?

next() → első találta vagy none
"""


class AllatAdatProcess:
    def __init__(self, allatkert: Allatkert):
        self.allatok = allatkert.allatok

    def kor_alapjan_szures(self, min_kor):
        return [a for a in self.allatok if a.kor >= min_kor]

    def van_e_fajta(self, faj):
        """
        for a in self.allatok:
            if a.faj == faj:
                return True
        return False

        van-e köztük legalább egy True

        ha igen → visszaadja, hogy van ilyen faj
        """
        return any(a.faj == faj for a in self.allatok)

    def nevek_keresese(self, regex):
        return [a.nev for a in self.allatok if re.search(regex, a.nev)]

    def faj_keresese(self, regex):
        return [a.faj for a in self.allatok if re.search(regex, a.faj)]

    def keres_attr_szerint(self, attr, regex):
        return [getattr(a, attr) for a in self.allatok if re.search(regex, getattr(a, attr))]

    def nevek_keresese_BETTER(self, regex):
        return self.keres_attr_szerint("nev", regex)

    def faj_keresese_BETTER(self, regex):
        return self.keres_attr_szerint("faj", regex)

    def osszesitett_kor(self):
        return sum(a.kor for a in self.allatok)

    def keres_nev_szerint(self, nev):
        """
        for a in self.allatok:
            if a.nev == nev:
                return a
        return None

        next(...) → fogja az első találatot

        ha nincs ilyen állat, akkor ne dobjon hibát → adjon vissza None-t
        """
        return next((a for a in self.allatok if a.nev == nev), None)

    def nevek_betuvel_kezdodnek(self, betu):
        return [a.nev for a in self.allatok if a.nev.startswith(betu)]

    def faj_szerinti_csoportositas(self):
        c = {}
        for a in self.allatok:
            c.setdefault(a.faj, []).append(a.nev)
        return c


def main():
    ak = Allatkert()

    ak += Emlos("cirmos", 2, szoros_fajta="rövidszőrű")
    ak += Madar("harkály", 7, repul_kepes=True)
    ak += Hullo("kígyó", 6, merges=True)
    ak += Emlos("Bodri", 5, szoros_fajta="hosszú")
    ak += Madar("pingvin", 3, repul_kepes=False)

    print(ak.allatok[0].extra["szoros_fajta"])

    fajl = "allatkert.json"
    ak.mentes_fajlba(fajl)
    ak.allatok.clear()
    ak.betoltes_fajlbol(fajl)

    aap = AllatAdatProcess(ak)

    print("Összes állat:")
    for a in ak.allatok:
        print(a)

    print("\n3 év felett:")
    for a in aap.kor_alapjan_szures(3):
        print(a)

    print("\nB betűs nevek:")
    print(aap.nevek_keresese(r"^B"))


main()
