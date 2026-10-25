from abc import ABC, abstractmethod

from app.model.backing_account import BankAccount


class AccountRepository(ABC):

    @abstractmethod
    def save(self, account: BankAccount) -> BankAccount | None:
        pass

    @abstractmethod
    def find_by_id(self, account_number: str) -> BankAccount | None: 
        pass

    @abstractmethod
    def find_all(self) -> list[BankAccount]:
        pass