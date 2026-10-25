from app.services.baking_service import BankingService
from decimal import Decimal

class BankingController:

    def __init__(self, service : BankingService):
        self.service = service

    def create_account(self, name: str, balance: Decimal):
        return self.service.create_account(name, balance)

    def get_account(self, account_id: str):
        return self.service.get_account(account_id)

    def get_all_accounts(self):
        return self.service.get_all_accounts()

    def deposit(self, account_id: str, amount: Decimal):
        return self.service.deposit(account_id, amount)

    def withdraw(self, account_id: str, amount: Decimal):
        return self.service.withdraw(account_id, amount)

    def transfer(self, from_account_id: str, to_account_id: str, amount: Decimal):
        return self.service.transfer(from_account_id, to_account_id, amount)