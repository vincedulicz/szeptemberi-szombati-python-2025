
# OCP

from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

    @staticmethod
    def info():
        print("info-tag")


class ClubCardDiscount(Discount):
    def calculate(self, price):
        return price / 2


class NoDiscount(Discount):
    def calculate(self, price):
        return price


class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def calculate(self, price):
        return price * (1 - self.percent / 100)


### business logic

def apply_discount(discount: Discount, price: float):
    # ...
    discount.info()
    return discount.calculate(price)


no_discount = NoDiscount()
percent_discount = PercentageDiscount(10)

print(apply_discount(no_discount, 100))
print(apply_discount(percent_discount, 100))

# END # OCP




# LSP

# LSP ROSSZ !!!
class Bird:
    def fly(self):
        return "repül"


class Pingvin(Bird):
    def fly(self):
        raise NotImplementedError("nem tud repülni")
# LSP ROSSZ END !!!



class Bird:
    def move(self):
        return "sétál"


class FlyingBird(Bird):
    def fly(self):
        return "repül"


class NonFlyingBird(Bird):
    def walk(self):
        return "totyog"


pingvin = NonFlyingBird()
sparrow = FlyingBird()
bird = Bird()


print(sparrow.fly(), sparrow.move())
print(pingvin.move(), pingvin.walk())

bird.move()

# [...]
bird.move()
pingvin.move()


# END LSP




# ISP

class Printer(ABC):
    # XXX: beépítet függvény elnevezés kerülése print dict és társai
    @abstractmethod
    def print_document(self, content):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class SimplePrinter(Printer):
    def print_document(self, content):
        print(f"nyomtat: {content}")


class MultiFunctionDevice(Printer, Scanner):
    def print_document(self, content):
        print(f'nyomtat: {content}')

    def scan(self):
        return "scanning in progress 1%"


printer = SimplePrinter()
printer.print_document("hello")

mdf = MultiFunctionDevice()
print(mdf.scan())


# END ISP




# DIP



class NotificatinSender(ABC):
    @abstractmethod
    def send(self, msg):
        pass


class EmailSender(NotificatinSender):
    def send(self, msg):
        print(f'sending mail: {msg}')


class SmsSender(NotificatinSender):
    def send(self, msg):
        print(f'sending sms: {msg}')


class NotificationService:
    def __init__(self, sender: NotificatinSender):
        self.sender = sender

    def notify(self, msg):
        self.sender.send(msg)


email_service = NotificationService(EmailSender())
sms_service = NotificationService(SmsSender())

email_service.notify("úton van")
sms_service.notify("10p és ott van")

arr = [email_service, sms_service]
for obj in arr:
    obj.notify("üzenet")


# END DIP