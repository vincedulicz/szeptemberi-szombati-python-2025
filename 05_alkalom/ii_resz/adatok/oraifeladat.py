import random


def task_01():
    with open('01_feladat.txt', encoding='utf-8') as f:
        students = [line.strip().split(";") for line in f]

    students = [(name, int(score)) for name, score in students]

    total_score = sum(score for _, score in students)

    avarage_score = total_score / len(students)

    passed_students = [name for name, score in students if score >= 60]

    best_student_name, best_score = max(students, key=lambda x: x[1])

    worst_student_name, worst_score = min(students, key=lambda x: x[1])

    print(f'| {avarage_score} | {passed_students} '
          f'| {best_score} - {best_student_name} '
          f'| {worst_student_name} - {worst_score}')

    with open('01_eredmeny.txt', 'w', encoding='utf-8') as f:
        for name, score in students:
            passed = 'yes' if score >= 60 else 'no'
            f.write(f'{name};{score};{passed}\n')


# task_01()


def task_02():
    drawns_numbers = set(random.sample(range(1, 91), 5))
    print(f'drawns numbers {sorted(drawns_numbers)}')

    with open('02_feladat.txt', encoding='utf-8') as f:
        players = [line.strip().split(";") for line in f]

    results = []
    for name, numbers_str in players:
        numbers = set(map(int, numbers_str.split(',')))

        hits = len(drawns_numbers & numbers)

        results.append((name, hits))

    with open('02_eredmeny.txt', 'w', encoding='utf-8') as f:
        for name, hits in results:
            f.write(f'{name};{hits}\n')


# task_02()

def task_03():
    with open(f'03_feladat.txt', encoding='utf-8') as f:
        orders = [line.strip().split(";") for line in f]

    orders = [(product, int(quantity)) for product, quantity in orders]

    total_items = sum(quantity for _, quantity in orders)

    bakery_orders_count = sum(1 for product, _ in orders if product == "Pékárú")

    more_than_3 = [(product, quantity) for product, quantity in orders if quantity > 3]

    product_totals = {}
    for product, quantity in orders:
        product_totals[product] = product_totals.get(product, 0) + quantity

    most_ordered_product = max(product_totals, key=product_totals.get)

    with open('03_eredmeny.txt', 'w', encoding='utf-8') as f:
        f.write(f'total orders items {total_items}')
        for product, quantity in more_than_3:
            f.write(f'{product};{quantity}')
        f.write(f'{most_ordered_product}\n')


task_03()