class Nber:
    def __init__(self, nev):
        self.nev = nev
        self._kor = None

    @property
    def kor(self, uj_kor):
        self._kor = uj_kor

    @kor.getter
    def kor(self):
        return self._kor

    def foo(self):
        print(self.nev)

    def fura(self, *param):
        self.kor = param[0][0] # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! EZT NE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print("fura függvény lefutott")


n = Nber("kis pista")
n.foo()

try:
    print(n.kor)
except:
    pass

n.fura(["4", "5"])

print(n.kor)