import csv
import json
import math


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f'elindult a {self.brand} autó')

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}'

    def save_to_file(self, filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(str(self) + "\n")

    @classmethod
    def from_file(cls, filename):
        cars = []

        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(" ")
                if len(parts) >= 3:
                    year = parts[0]
                    brand = parts[1]
                    model = " ".join(parts[2:])
                    cars.append(cls(brand, model, year))

        return cars


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def start(self):
        print("hangtalunl elindul me elektromos")

    def charge(self):
        print("töltés...")

    def estimate_charging_time(self, charger_kw):
        if charger_kw <= 0:
            raise ValueError("nem lehet negatív")
        hours = round(self.battery_capacity / charger_kw, 2)
        return hours

    @staticmethod
    def save_to_json(electric_cars, filename):
        data = [
            {
                "brand": c.brand,
                "model": c.model,
                "year": c.year,
                "battery_capacity": c.battery_capacity,
            }
            for c in electric_cars
        ]
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("érvénytelen befizetés")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("érvénytelen levétel")
            return
        if amount > self.__balance:
            print("nincs elég egyenleg")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def save_to_csv(self, filename):
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([self.account_number, self.get_balance()])

    @classmethod
    def load_from_csv(cls, filename):
        accounts = {}

        with open(filename, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    acc_num, balance = row
                    acc = cls(acc_num)
                    acc._BankAccount__balance = float(balance)
                    accounts[acc_num] = acc
        return list(accounts.values())


class Shape:
    def __init__(self, name=None):
        self.name = name

    def area(self):
        raise NotImplementedError("A terület az alosztályban történik")


class Rectangle(Shape):
    def __init__(self, width, height, name="téglalap"):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius, name="kör"):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Square(Rectangle):
    def __init__(self, side, name="négyzet"):
        super().__init__(side, side, name)
        self.side = side # nem feltétlen kell...


def shapes_to_json(shapes, filename):
    data = []
    for s in shapes:
        entry = {"type": s.__class__.__name__, "name": s.name, "area": s.area()}
        if isinstance(s, Rectangle):
            entry.update({"width": s.width, "height": s.height})
        elif isinstance(s, Circle):
            entry.update({"radius": s.radius})
        elif isinstance(s, Square):
            entry.update({"side": s.side})
        data.append(entry)

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def shapes_from_json(filename):
    shapes = []

    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            t = item["type"]
            if t == "Circle":
                shapes.append(Circle(item["radius"], item["name"]))
            # ... rectangle square

    return shapes


def main():
    print("Car")
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Ford", "Focus", 2018)
    car1.start()
    car2.start()
    car1.save_to_file("adatok/cars.txt")
    car2.save_to_file("adatok/cars.txt")
    for c in Car.from_file("adatok/cars.txt"):
        print(c)

    print("\nElectricCar teszt")
    ecar = ElectricCar("Tesla", "Model 3", 2022, 75)
    normal = Car("VW", "Golf", 2019)
    ecar.start()
    ecar.charge()
    print("Töltési idő:", ecar.estimate_charging_time(11), "óra")
    ElectricCar.save_to_json([ecar], "electric_cars.json")

    print("\nBankAccount")
    acc1 = BankAccount("HU123")
    acc2 = BankAccount("HU456")
    acc1.deposit(5000)
    acc1.withdraw(1000)
    acc2.deposit(12000)
    acc1.save_to_csv("adatok/accounts.csv")
    acc2.save_to_csv("adatok/accounts.csv")
    for a in BankAccount.load_from_csv("adatok/accounts.csv"):
        print(a.account_number, a.get_balance())

    print("\nShape")
    shapes = [
        Rectangle(3, 4, "Tégla1"),
        Rectangle(5, 6, "Tégla2"),
        Square(5, "Négyzet1"),
        Circle(3, "Kör1"),
    ]
    for s in shapes:
        print(f"A(z) {s.name} területe: {round(s.area(), 2)}")
    shapes_to_json(shapes, "adatok/shapes.json")
    print("Fájlból visszaolvasva:")
    for s in shapes_from_json("adatok/shapes.json"):
        print(f"{s.name} ({s.__class__.__name__}) - terület: {round(s.area(), 2)}")


main()
