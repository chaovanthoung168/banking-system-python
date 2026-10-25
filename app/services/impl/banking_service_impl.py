from uuid import uuid4
from decimal import Decimal

from app.exceptions.backing_exception import (
    InvalidAmountException,
    AccountNotFoundException,
    InsufficientFundsException,
)
from app.model.backing_account import BankAccount
from app.repositories.account_repository_impl import AccountRepositoryImpl
from app.services.baking_service import BankingService


class BankingServiceImpl(BankingService):

    def __init__(self, repository: AccountRepositoryImpl):
        self.repository = repository

    def _validate_amount(self, amount: Decimal) -> None:
        if (
            not amount.is_finite()
            or amount <= 0
            or amount.as_tuple().exponent < -2
        ):
            raise InvalidAmountException(
                "Amount must be positive with at most 2 decimal places"
            )

    def create_account(
        self,
        owner_name: str,
        initial_balance: Decimal
    ) -> BankAccount:

        if not owner_name.strip():
            raise ValueError("Owner name is required")

        if not initial_balance.is_finite() or initial_balance < 0:
            raise InvalidAmountException("Invalid initial balance")

        if initial_balance.as_tuple().exponent < -2:
            raise InvalidAmountException(
                "Use at most 2 decimal places"
            )

        account = BankAccount(
            account_number=str(uuid4()),
            owner_name=owner_name.strip(),
            balance=initial_balance
        )

        return self.repository.save(account)

    def get_account(self, account_number: str) -> BankAccount:
        account = self.repository.find_by_id(account_number)

        if account is None:
            raise AccountNotFoundException("Account not found")

        return account

    def get_all_accounts(self) -> list[BankAccount]:
        return self.repository.find_all()

    def deposit(
        self,
        account_number: str,
        amount: Decimal
    ) -> BankAccount:

        self._validate_amount(amount)

        account = self.get_account(account_number)
        account.balance += amount

        return self.repository.save(account)

    def withdraw(
        self,
        account_number: str,
        amount: Decimal
    ) -> BankAccount:

        self._validate_amount(amount)

        account = self.get_account(account_number)

        if account.balance < amount:
            raise InsufficientFundsException("Insufficient funds")

        account.balance -= amount

        return self.repository.save(account)

    def transfer(
        self,
        from_account: str,
        to_account: str,
        amount: Decimal
    ) -> None:

        self._validate_amount(amount)

        if from_account == to_account:
            raise ValueError("Cannot transfer to the same account")

        sender = self.get_account(from_account)
        receiver = self.get_account(to_account)

        if sender.balance < amount:
            raise InsufficientFundsException("Insufficient balance")

        sender.balance -= amount
        receiver.balance += amount

        self.repository.save(sender)
        self.repository.save(receiver)