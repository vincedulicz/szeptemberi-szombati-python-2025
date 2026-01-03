class DomainError(Exception):
    def __init__(self, message: str = None):
        if message is None:
            message = self.__class__.__name__
        super().__init__(message)


class AccountAlreadyExists(DomainError):
    pass


class AccountNotFound(DomainError):
    pass


class InsufficientFunds(DomainError):
    pass


class InvalidAmount(DomainError):
    pass


class ItemNotFound(DomainError):
    pass


class NoBankAccount(DomainError):
    pass
