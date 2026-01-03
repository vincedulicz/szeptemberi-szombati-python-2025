
class Alap:
    OSZTALY_VAR = 1

    def __init__(self, param)
        self.__param = param

    def speak(self):
        print("beszélek")

    @staticmethod
    def foo():
        pass


class Alap2(Alap):
    def __init__(self, param):
        super().__init__(param)

    def speak(self):
        print("ír")

    @property
    def param(self):
        return self.param

    @property.setter
    def param(self, new_param):
        self.param = new_param




class Abs(ABC):
    @abstractmethod
    def foo(self):
        pass



class Engine:
    pass


class Bus:
    def __init__(self):
        self.engine = Engine()



SOLID - DRY - KISS - YAGNI - OOP