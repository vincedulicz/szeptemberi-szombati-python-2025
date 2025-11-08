class Motor:
    def __init__(self, teljesitmeny):
        self.__teljesitmeny = teljesitmeny # PRIVÁT !!!!!!!!!!!

    def __str__(self):
        return f'ez egy motor objektum'

    def motor_info(self):
        return f'motor tej.: {self.__teljesitmeny}'

    # !!!
    @property
    def teljesitmeny(self):
        print("getter")
        return self.__teljesitmeny

    @teljesitmeny.setter
    def teljesitmeny(self, value):
        print("setter")
        self.__teljesitmeny = value


motor = Motor(120)
print(motor)
print(motor.teljesitmeny)
motor.teljesitmeny = 121
print(motor.teljesitmeny)


class Auto:
    def __init__(self, marka, motor: Motor):
        self.marka = marka
        self.motor = motor

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.marka == other.marka
        return False

    def auto_info(self):
        return f'márka: {self.marka}, {self.motor.motor_info()}'


auto = Auto("toyota", motor)

motor2 = Motor(1200)
auto2 = Auto("toyota", motor2)

print(auto == auto2)
