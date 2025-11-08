

class Person:
    # osztályváltozók
    name = "John"
    age = 36
    country = "hu"

    def _protected(self):
        pass

    def __private(self):
        pass

    def public(self):
        pass


ertek = getattr(Person, 'age')
# print(ertek)

setattr(Person, 'age', 40)
ertek = getattr(Person, 'age')

# print(ertek)

# print(hasattr(Person, 'name2'))


class Cica(object):
    def __init__(self):
        self._nev = "cirmi" # protected
        self.__privat = "str" # privát

    def __str__(self):
        return f'cica: {self._nev}'

    def __eq__(self, other):
        if isinstance(other, Cica):
            return self._nev == other.nev

    @property
    def nev(self):
        print("getter")
        return self._nev

    @nev.setter
    def nev(self, value):
        print("setter")
        if value == "cirmi":
            print("nem lehet ilyen név")
            return

        self._nev = value

    @nev.deleter
    def nev(self):
        print("deleter")
        del self._nev


c = Cica()
print(c)

c.nev = "cirmi2"

print(c.nev)


c2 = Cica()
c2.nev = "cirmi2"

print(c2)

print(c == c2)