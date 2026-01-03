from orai_feladat.Bank.Bank import Bank
from orai_feladat.DomainError.DomainError import DomainError
from orai_feladat.Person.Person import Person
from orai_feladat.Shop.Shop import InventoryRepository, ItemCategory, Item, ShopService


def main():
    bank = Bank()
    inventory = InventoryRepository()

    inventory.add(Item("I001", "laptop", 500, ItemCategory.IT))
    inventory.add(Item("K001", "egérpad", 666, ItemCategory.ACCESSORY))

    shop = ShopService(inventory, bank)

    janos = Person("Jani", 30, "HU")

    # számla nélkül
    try:
        shop.purchase(janos, 'I001')
    except DomainError as e:
        print(f"hiba: {e}")

    # nincs elég pénz
    try:
        janos.open_account(bank, 369)
        shop.purchase(janos, 'I001')
    except DomainError as e:
        print(f'hiba: {e}')

    # nincs termék
    try:
        shop.purchase(janos, "nincs")
    except DomainError as e:
        print(f'hiba: {e}')

    try:
        bank.deposit(janos.account_number, 963)
        item = shop.purchase(janos, 'I001')
        print(f'sikeres vásárlás: {item.name}')
        print(f'egyenleg: {bank.get_balance(janos.account_number)}')
    except DomainError as e:
        print(f'hiba: {e}')


main()
