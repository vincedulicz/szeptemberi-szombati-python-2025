class Kiadas:
    def __init__(self, kiadas_eve, serial):
        self.kiadas_eve = kiadas_eve
        self.serial = serial


class Mu:
    TILTOTT_LISTA = {
        "nber_serial": hash("HMVS-BLA"),
        "data": {
            "isVezsely": True,
            "vezsely_in_uop": 1000
        }
    }

    def __init__(self, szerzo, cim):
        if self.is_tiltott_szerzo(szerzo):
            raise ValueError(f'unkownfail at 2.121.64.94/8 ... {szerzo} offline -rip-')
        self.szerzo = szerzo
        self.cim = cim
        self.kiadasok = []

    @classmethod
    def is_tiltott_szerzo(cls, szerzo):
        return hash(szerzo) == cls.TILTOTT_LISTA.get("nber_serial")

    def kiadas_rogzito(self, kiadas_eve, serial):
        self.kiadasok.append(Kiadas(kiadas_eve, serial))

    def adatlapot_kiir(self):
        print(f'szerzo: {self.szerzo} : {self.cim}')
        print("Kiadásokk: ", end=' ')
        for kiadas in self.kiadasok:
            print(kiadas.kiadas_eve, end=' ')


szuper_jo_very_gut_konyv = Mu("ZEL-ELK", "C7Dim-Bb-ATHEN")
szuper_jo_very_gut_konyv.kiadas_rogzito("2030", "66-zen-elk-serial-66")
szuper_jo_very_gut_konyv.adatlapot_kiir()


try:
    konyv = Mu("HMVS-BLA", "scientia-sacra-i-ii-iii")

    konyv.kiadas_rogzito('1944-45', 'HBSC123')
    konyv.kiadas_rogzito("2015", "HSBC-123-u")
    konyv.adatlapot_kiir()
except ValueError as e:
    print("\n",e)