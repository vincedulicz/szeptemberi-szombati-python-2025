class Number:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("getter")
        return self._value

    @value.setter
    def value(self, new_value):
        print("setter")
        if new_value != 0:
            self._value = new_value
        print("nem lehet 0")

    def __eq__(self, other):
        """ obj1 == obj2 """
        return self.value == other.value

    def __ne__(self, other):
        """ obj1 != obj2 """
        return self.value != other.value

    def __add__(self, other):
        """ obj1 + obj2 """
        return Number(self.value + other.value)

    def __sub__(self, other):
        """ obj1 - obj2 """
        return Number(self.value - other.value)

    def __iadd__(self, other):
        """ obj1 += obj2"""
        print("iadd")
        if other.value == 10:
            print("10-et nem lehet hozzáadni")
            return
        self.value += other.value
        return self

    def __lt__(self, other):
        """ ojb1 < obj2 """
        return self.value < other.value

    def __gt__(self, other):
        """ obj1 > obj2 """
        return self.value > other.value

    def __le__(self, other):
        """ obj1 <= obj2 """
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __str__(self):
        return f'number object: {self.value}'


szam = Number(3)
masik_szam = Number(11)

print(szam)

print(szam < masik_szam)

szam += masik_szam
print(szam)