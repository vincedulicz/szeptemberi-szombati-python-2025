
# 1.

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} ..."


# 2.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f'cím: {self.title} | szerzője: {self.author}')


b = Book("Föld És Lélek", "Carl G. Jung")
b.print_info()


# 3.

class Vehicle:
    pass


class Car(Vehicle):
    @staticmethod
    def start():
        print("elindult")


# 4.

class Animal:
    @staticmethod
    def speak():
        print("....")


class OtherDog(Animal):
    @staticmethod
    def speak():
        print("vau")


class Cat(Animal):
    @staticmethod
    def speak():
        print("nyünnyügni")


# 5.

def make_animal_speak(animal: Animal):
    animal.speak()


make_animal_speak(OtherDog())
make_animal_speak(Cat())


# 6.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserPrinter:
    @staticmethod
    def print_user(user: User):
        print(f"név: {user.name} | email: {user.email}")


# 7.

class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a


# 8.

class Bird:
    pass


class Duck(Bird):
    @staticmethod
    def fly():
        print("A kacsa repülget")


class Penguin(Bird):
    def swim(self):
        print("A pingvin úszni")


# 9.

class Printer:
    def print(self):
        raise NotImplementedError


class Scanner:
    def scan(self):
        raise NotImplementedError


class Fax:
    def fax(self):
        raise NotImplementedError


class AdvancedPrinter(Printer, Scanner, Fax):
    def print(self):
        print("nyomtatáts")

    def scan(self):
        print("szkennn")

    def fax(self):
        print("faax")


# 10.

class Logger:
    def log(self, msg):
        print(f'LOG: {msg}')


class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger

    def create_user(self, name):
        self.logger.log(f'user létrehozva: {name}')


# 11.


class Engine:
    def start(self):
        print("motor elindult")


class CarWithEngine:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("...autó indul")
        self.engine.start()


# 12.

class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("életkor nem lehet negatív")
        self._age = value