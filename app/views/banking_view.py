

from decimal import Decimal, InvalidOperation


class BankingView:

    def show_menu(self):
        print("\n====== BANKING SYSTEM ======")
        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Find Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("0. Exit")

        return input("Choose option: ").strip()

    def get_text(self, message: str) -> str:
        return input(message).strip()

    def get_amount(self, message: str) -> Decimal:
        try:
            return Decimal(input(message).strip())
        except InvalidOperation:
            raise ValueError("Invalid number")

    def show_account(self, account):
        print(
            f"Account: {account.account_number} | "
            f"Owner: {account.owner_name} | "
            f"Balance: ${account.balance:.2f}"
        )

    def show_message(self, message: str):
        print(message)
