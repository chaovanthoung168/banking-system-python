
from app.model.backing_account import BankAccount
from app.repositories.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):

    def __init__(self):
        self._accounts: dict [str, BankAccount] = {}

    def save(self, account: BankAccount) -> BankAccount :
        self._accounts[account.account_number] = account
        return account

    def find_by_id(self, account_number: str) -> BankAccount | None:
        return self._accounts.get(account_number)

    def find_all(self) -> list[BankAccount]:
        return list(self._accounts.values())