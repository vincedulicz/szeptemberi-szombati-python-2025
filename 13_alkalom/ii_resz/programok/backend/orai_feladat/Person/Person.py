import uuid

from orai_feladat.Accountable.Accountable import Accountable


class Person:
    def __init__(self, name: str, age: int, country: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.country = country
        self.account_number = None

    def open_account(self, bank: Accountable, initial_balance: float):
        if self.account_number:
            return
        self.account_number = f'ACC-{self.id[:8]}'
        bank.create_account(self.account_number, initial_balance)
