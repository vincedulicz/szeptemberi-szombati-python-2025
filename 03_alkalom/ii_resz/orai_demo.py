

forrasfajl = open('autok_listaja.txt')
for sor in forrasfajl:
    print(sor)

    print(forrasfajl.readline())    # 1-es sorok

    print(forrasfajl.readlines())   # összes elem

    print(forrasfajl.read())        # teljes fájltartalom

# mindig el kell követni - with hiányában
# forrasfajl.close()


autok = []

with open('autok_listaja.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'típus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

print(f'{autok}')


with open('output.txt', 'w', encoding='utf-8') as celfajl:
    print('ez kerül bele a becses fájlba....', file=celfajl)


with open('output2.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write('anystr ez kerül kifele a fájlba')

    celfajl.writelines(['alma\n', 'körte\n', 'dió\n'])


# TODO: fájlelejére tedjed
import json

with open('diakok.json', 'r', encoding='utf-8') as diakok_adatok:
    adatok = json.load(diakok_adatok)

print(type(adatok))

for diak in adatok['diakok']:
    print(diak.get('név'))
    print(diak)

    if not diak.get('kollegista'):
        print("mér")
    else:
        print("az")
