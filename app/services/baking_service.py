from abc import ABC, abstractmethod
from decimal import Decimal

from app.model.backing_account import BankAccount


class BankingService(ABC):

    @abstractmethod
    def create_account(
            self,
            owner_name: str,
            initial_balance: Decimal
     )-> BankAccount | None:
        pass

    @abstractmethod
    def get_account(self, account_number: str) -> BankAccount:
        pass

    @abstractmethod
    def deposit(self, account_number: str, amount: Decimal) -> BankAccount | None:
        pass

    @abstractmethod
    def withdraw(self, account_number: str, amount: Decimal) -> BankAccount:
        pass

    @abstractmethod
    def transfer(self, from_account: str, to_account: str, amount: Decimal) -> None:
        pass

