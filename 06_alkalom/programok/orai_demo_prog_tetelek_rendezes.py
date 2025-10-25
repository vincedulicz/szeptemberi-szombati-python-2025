def buborek_rendezes(t):
    """
    Buborékos rendezés:
    Egymás melletti elemeket hasonlít össze, és ha rossz sorrendben vannak, felcseréli őket.
    Minden körben a legnagyobb elem "felúszik" a végére.

    Hogyan működik:
    - Képzeljük el úgy, mint a vízben úszó buborékokat: a legnagyobb mindig a tetejére kerül.
    - Az algoritmus egymás melletti elemeket vizsgál (t[j] és t[j+1]).
    - Ha a bal oldali nagyobb, mint a jobb oldali, akkor cseréljük őket.
    - Minden körben a legnagyobb elem a lista végére kerül, ezért a következő körben már nem kell vele foglalkozni.
    - Addig ismételjük, amíg az egész lista sorba nem kerül.

    Példa:
    [5, 2, 9, 1] → összehasonlítja 5 és 2 → csere → [2, 5, 9, 1]
    majd 5 és 9 → marad, 9 és 1 → csere → [2, 5, 1, 9]
    A 9 most már a helyén van.
    """
    n = len(t)

    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if t[j] > t[j + 1]:
                tmp = t[j + 1]
                t[j + 1] = t[j]
                t[j] = tmp

    print(t)


def rendezes_cserevel(t):
    """
    Rendezés cserékkel:
    Minden elemhez (i) végignézi a nála későbbi elemeket (j),
    és ha talál kisebbet, akkor cserél.
    Egyszerű, de nem hatékony megoldás.

    Hogyan működik:
    - A lista első elemétől indulunk, és minden egyes elemhez (i) végignézzük a nála jobbra lévő elemeket (j).
    - Ha találunk olyat, ami kisebb, akkor azonnal cseréljük őket.
    - Így a legkisebb elemek fokozatosan a lista elejére kerülnek.
    - A végére a lista rendezett lesz, de sok felesleges csere történik.

    Példa:
    [5, 2, 9, 1]
    i=0 → 5 összehasonlítva 2-vel → csere → [2, 5, 9, 1]
           5 és 9 → nem csere, 5 és 1 → csere → [2, 1, 9, 5]
    i=1 → 1 és 9 → ok, 1 és 5 → ok → [1, 2, 5, 9]
    """
    n = len(t)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if t[i] > t[j]:
                tmp = t[i]
                t[i] = t[j]
                t[j] = tmp

    print(t)


def max_kivalasztas_rendezes(t):
    """
    Maximum kiválasztásos rendezés:
    A lista végéről indulva minden körben megkeresi a maximumot
    a rendezetlen részben, majd kicseréli az aktuális pozícióval.

    Hogyan működik:
    - A lista végére mindig a legnagyobb elemet tesszük.
    - Először megkeressük a legnagyobb elemet a teljes listában.
    - Aztán kicseréljük az utolsó elemmel.
    - Ezután már nem kell foglalkoznunk az utolsóval, mert az biztosan a helyén van.
    - A folyamatot addig ismételjük, amíg minden elem a helyére nem kerül.

    Példa:
    [5, 2, 9, 1]
    legnagyobb = 9 → csere az utolsóval → [5, 2, 1, 9]
    legnagyobb a maradékból (5, 2, 1) → 5 → csere az előtte lévővel → [1, 2, 5, 9]
    """
    n = len(t)

    for i in range(n - 1, -1, -1):
        max_index = i
        for j in range(0, i):
            if t[j] > t[max_index]:
                max_index = j
        tmp = t[i]
        t[i] = t[max_index]
        t[max_index] = tmp

    print(t)


def min_kivalasztas_rendezes(t):
    """
    Minimum kiválasztásos rendezés:
    Balról jobbra haladva minden lépésben megkeresi a legkisebb elemet
    a rendezetlen részből, majd kicseréli az aktuális pozícióval.

    Hogyan működik:
    - Az első helyre mindig a legkisebb elemet tesszük.
    - Végigmegyünk a listán, és megkeressük a legkisebb elemet a hátralévő részből.
    - Ezt kicseréljük az aktuális (i-edik) elemmel.
    - Utána a következő elemre lépünk, és ugyanezt megismételjük.
    - A lista fokozatosan balról jobbra rendeződik.

    Példa:
    [5, 2, 9, 1]
    legkisebb = 1 → csere az elsővel → [1, 2, 9, 5]
    legkisebb a maradékból (2, 9, 5) → 2 → marad → [1, 2, 9, 5]
    """
    n = len(t)

    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if t[j] < t[min_index]:
                min_index = j
        if min_index != i:
            tmp = t[i]
            t[i] = t[min_index]
            t[min_index] = tmp

    print(t)


def rendezes_beszurasssal(t):
    """
    Beszúrásos rendezés:
    Balról jobbra haladva minden elemet a helyére szúr be
    az előzőleg már rendezett részbe.
    Hatékony kis listák esetén.

    Hogyan működik:
    - Képzeld el, hogy kártyákat rendezel a kezedben.
    - Balról jobbra haladsz, és minden új kártyát (elemet) a megfelelő helyre "beszúrsz".
    - Az első elem önmagában rendezett.
    - A második elemtől kezdve mindig visszafelé haladunk, amíg meg nem találjuk, hova illik az aktuális elem.
    - A többieket jobbra toljuk, hogy legyen helye.

    Példa:
    [5, 2, 9, 1]
    2-t betesszük 5 elé → [2, 5, 9, 1]
    9 marad, mert nagyobb → [2, 5, 9, 1]
    1-et betesszük legelőre → [1, 2, 5, 9]
    """
    n = len(t)

    for i in range(0, n):
        kulcs = t[i]
        j = i - 1
        while j >= 0 and t[j] > kulcs:
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = kulcs

    print(t)


def shell_rendezes(t):
    """
    Shell-rendezés:
    A beszúrásos rendezés általánosítása, amely kezdetben
    távolabbi elemeket hasonlít össze és mozgat, csökkentve az "ugrásokat".
    A lépések (gap) egyre kisebbek, végül beszúrásos rendezés lesz belőle.

    Hogyan működik:
    - A beszúrásos rendezés lassú, ha az elemek nagyon távol vannak.
    - A Shell-rendezés ezt úgy javítja, hogy először "ugrásokkal" (gap) dolgozik.
    - Először pl. minden 5. elemet hasonlít össze, majd 3-at, majd 1-et.
    - Így a nagyobb értékek gyorsan elmozdulhatnak a helyük közelébe.
    - Amikor a lépésköz 1 lesz, egy sima beszúrásos rendezés történik, de már sokkal kevesebb munka van hátra.

    Példa:
    [5, 2, 9, 1, 6, 3]
    gap=5 → összehasonlít 5 és 3 → csere → [3, 2, 9, 1, 6, 5]
    gap=3 → összehasonlít távoli elemeket, fokozatosan rendez
    gap=1 → végső finomítás beszúrásos rendezéssel
    """
    h = [5, 3, 1]
    n = len(t)

    for k in range(0, 3):
        lepes = h[k]
        for j in range(lepes, n):
            i = j - lepes
            kulcs = t[j]
            while i >= 0 and t[i] > kulcs:
                t[i + lepes] = t[i]
                i -= lepes
            t[i + lepes] = kulcs

    print(t)


def gyors_rendezes(t):
    """
    Gyorsrendezés (QuickSort):
    Egy kiválasztott pivot érték alapján a listát három részre bontja:
    kisebbek, egyenlők és nagyobbak. Ezeket rekurzívan rendezi.
    Nagyon hatékony, de nem stabil rendezés.

    Hogyan működik:
    - Választunk egy központi elemet (pivot).
    - Minden más elemet összehasonlítunk ezzel:
      - ami kisebb, az a "bal oldalra" kerül,
      - ami egyenlő, középre,
      - ami nagyobb, a "jobb oldalra".
    - A bal és jobb oldali részeket újra és újra ugyanígy rendezzük (rekurzívan).
    - Végül az összes részlista összeáll, és az egész sorba kerül.

    Példa:
    [5, 2, 9, 1, 5, 6]
    pivot = 6
    → kisebbek: [5, 2, 1, 5]
    → egyenlők: [6]
    → nagyobbak: [9]
    újrarendezi a részeket → [1, 2, 5, 5, 6, 9]
    """
    n = len(t)

    if n <= 1:
        return t

    kicsik = []
    egyenlo = []
    nagyok = []
    pivot = t[n-1]

    for num in t:
        if num < pivot:
            kicsik.append(num)
        if num == pivot:
            egyenlo.append(num)
        if num > pivot:
            nagyok.append(num)

    return gyors_rendezes(kicsik) + egyenlo + gyors_rendezes(nagyok)


def main():
    lista = [5, 2, 9, 1, 5, 6]

    buborek_rendezes(lista.copy())
    rendezes_cserevel(lista.copy())
    max_kivalasztas_rendezes(lista.copy())
    min_kivalasztas_rendezes(lista.copy())
    rendezes_beszurasssal(lista.copy())
    shell_rendezes(lista.copy())
    print(gyors_rendezes(lista.copy()))


main()
