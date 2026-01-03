from dataclasses import dataclass
from enum import Enum

from orai_feladat.Accountable.Accountable import Accountable
from orai_feladat.DomainError.DomainError import ItemNotFound, NoBankAccount
from orai_feladat.Person.Person import Person


class ItemCategory(Enum):
    IT = "I"
    ACCESSORY = "K"


@dataclass(frozen=True)
class Item:
    id: str
    name: str
    price: float
    category: ItemCategory


class InventoryRepository:
    def __init__(self):
        self._items: dict[str, Item] = {}

    def add(self, item: Item):
        self._items[item.id] = item

    def get(self, item_id: str):
        if item_id not in self._items:
            raise ItemNotFound("item not foundz err")
        return self._items[item_id]


class ShopService:
    def __init__(self, inventory: InventoryRepository, bank: Accountable):
        # TODO: bank... jogosultságok
        self.inventory = inventory
        self.bank = bank

    def purchase(self, buyer: Person, item_id: str):
        if not buyer.account_number:
            raise NoBankAccount()

        item = self.inventory.get(item_id)
        self.bank.withdraw(buyer.account_number, item.price)

        return item
