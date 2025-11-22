import re
from collections.abc import Iterable
from collections import OrderedDict

def get_length(item):
    if isinstance(item, Iterable):
        return len(item)
    else:
        return "nem iterálható"


def is_ok():
    return False


def my_decorator(func):
    def wrapper():
        print("ez van a függvényhívás előtt")
        if is_ok():
            func()
        else:
            print("nem")
        print("ez van a függvényhívás után")
    return wrapper


@my_decorator
def say_hello():
    print("hello")


# say_hello()

"""
nev@aldomain.domain-teszt.gov.hu
[a-zA-Z0-9._%+-]
@
[a-zA-Z0-9.-]
.
[a-zA-Z]{2,}
"""
email_minta = r"[a-zA-Z09._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_szoveg = "az email cím: nemvalid@.email.h pelda.elek@mail-server-example.com user@domain.com info@test.org."
talalatok = re.findall(email_minta, email_szoveg)
print(talalatok)


od = OrderedDict()

od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)

od.move_to_end('a')
print(od)

od.popitem(last=False)
od.popitem(last=True)
print(od)


square = lambda x: x**2
print(square(5))


my_list = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))
print(odd_numbers)


gyumi = [("apple", 50), ("banana", 10), ("cherry", 30)]

sorted_list = sorted(gyumi, key=lambda x: x[1])
print(sorted_list)


teszt_list = list(map(lambda x: x**2, my_list))
print(teszt_list)

