
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class BankAccount:
    account_number: str
    owner_name: str
    balance: Decimal = Decimal("0.00")