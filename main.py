from app.controller.banking_controller import BankingController
from app.exceptions.backing_exception import BankingException
from app.repositories.account_repository_impl import AccountRepositoryImpl
from app.services.impl.banking_service_impl import BankingServiceImpl

from app.views.banking_view import BankingView



def main():
    repository = AccountRepositoryImpl()
    service = BankingServiceImpl(repository)
    controller = BankingController(service)
    view = BankingView()

    while True:
        choice = view.show_menu()

        try:
            if choice == "1":
                name = view.get_text("Owner name: ")
                balance = view.get_amount("Initial balance: ")
                account = controller.create_account(name, balance)
                view.show_account(account)

            elif choice == "2":
                accounts = controller.get_all_accounts()

                if not accounts:
                    view.show_message("No accounts found")

                for account in accounts:
                    view.show_account(account)

            elif choice == "3":
                number = view.get_text("Account number: ")
                view.show_account(controller.get_account(number))

            elif choice == "4":
                number = view.get_text("Account number: ")
                amount = view.get_amount("Deposit amount: ")
                view.show_account(controller.deposit(number, amount))

            elif choice == "5":
                number = view.get_text("Account number: ")
                amount = view.get_amount("Withdraw amount: ")
                view.show_account(controller.withdraw(number, amount))

            elif choice == "6":
                sender = view.get_text("Sender account: ")
                receiver = view.get_text("Receiver account: ")
                amount = view.get_amount("Transfer amount: ")
                controller.transfer(sender, receiver, amount)
                view.show_message("Transfer successful")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option")

        except (BankingException, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
