import keyword
import math

print(keyword.kwlist)

teszt = 0

bejovo_szam = 1

print(type(bejovo_szam))

teszt = "string"

print(type(teszt))

valtozo = None

valtozo = "dede "
text = "ez egy text"

print(valtozo + text)


a_int = 1
b_float = 1.5
c_complex = 3.14j

print(type(c_complex))


print(5 / 2)  # osztás -> float
print(5 // 2) # egészosztás -> int
print(7 % 2 ) # maradékosztás
print(2 ** 3) # hatványozás
print(2 * 3)  # szorzás
# + -



text = "szöveg" # string
betu = 'a'      # string egyetlen egy karakter

tomb = ["string", 1, None, ["..."]] # lista pythonossan

print("len(tomb): ", len(tomb))

print("tomb az 1. elem: ", tomb[0])

print("lista 2. elem: ", tomb[1])

# print("index error: ", tomb[4])

print("...")



print(text[0])      # első karakter
print(text[0:2])    # első két karakter
print(text[2:])     # 3. karaktertől a végéig
print(text[-3:])    # utolsó 3 karakter

print(text[0:-1:2]) # elejétől az utolsó előttig, kettes lépésközzel
print(text[::2])    # elejétől végéig kettes lépésköz

print(text[::1])    # teljes string
print(text[::-1])   # string visszafelé
print(text[-1])     # utolsó karakter
print(text[-2])     # utolsó előtti karakter


lista = [1, 2, 3, 4, 5]

i = 0
while i <= 4:
    print(f"i értéke: {i}")
    print(f"érték: {lista[i]}, típus: {type(lista[i])}")
    i += 1
    print(f"i értéke: {i}")



# name = input("hogy hínak? ")
# print(f"szia {name}")


# first_num = int(input("első szám: "))        # string
# second_num = int(input("második szám: "))    # str(2) + str(2) = 22
# print(first_num + second_num)


print("mennyi a kör sugara: ")
# sugar = float(input())

# print("kerület = ", 2 * sugar * math.pi)
# print("terulet = ", sugar ** 2 * math.pi)


# páros v páratlan

def paros_e_method(szam):
    if szam % 2 == 0:
        print("páros")
    else:
        print("páratlan")


# függvény | boolean t / f  -  1 / 0
def paros_e_fuggveny(szam):
    return szam % 2 == 0

if paros_e_fuggveny(5):
    print("varázslat páratlan")
else:
    print("mér nem párospáratlan???")


if not False: # not False -> True
    print("true")
else:
    print("false")



a = 4
b = False # 0
c = True  # 1


if a > b:
    print("a > b")
elif b > a:
    print("B nagyobb")
elif b == a:
    print("b = a")
else:
    print("más.........")


lista = ["str2", 2,2,2,2,2,2, 2j, 3.14, "str2"]
print(lista)
print(lista.append(5)) # None a return érték
print(lista)

print(lista.count("str2"))