from orai_feladat.Accountable.Accountable import Accountable
from orai_feladat.DomainError.DomainError import AccountAlreadyExists, InvalidAmount, InsufficientFunds, AccountNotFound


class Bank(Accountable):
    def __init__(self):
        self._accounts: dict[str, float] = {}

    def create_account(self, account_number: str, initial_balance: float):
        if account_number in self._accounts:
            raise AccountAlreadyExists("már létezik ez az acc")
        if initial_balance < 0:
            raise InvalidAmount()
        self._accounts[account_number] = initial_balance

    def deposit(self, account_number: str, amount: float):
        self._validate_account(account_number)
        self._validate_amount(amount)
        self._accounts[account_number] += amount

    def withdraw(self, account_number: str, amount: float):
        self._validate_account(account_number)
        self._validate_amount(amount)
        if self._accounts[account_number] < amount:
            raise InsufficientFunds()
        self._accounts[account_number] -= amount

    def get_balance(self, account_number: str):
        self._validate_account(account_number)
        return self._accounts[account_number]

    def _validate_account(self, account_number: str):
        if account_number not in self._accounts:
            raise AccountNotFound("acc not foundz")

    def _validate_amount(self, amount: float):
        if amount <= 0:
            raise InvalidAmount("invalid amountzzz")
