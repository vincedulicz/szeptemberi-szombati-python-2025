from abc import abstractmethod, ABC


class Accountable(ABC):
    @abstractmethod
    def create_account(self, account_number: str, initial_balance: float):
        pass

    @abstractmethod
    def deposit(self, account_number: str, amount: float):
        pass

    @abstractmethod
    def withdraw(self, account_number: str, amount: float):
        pass

    @abstractmethod
    def get_balance(self, account_number: str):
        pass
