
class BankingException(Exception):
    pass

class AccountNotFoundException(BankingException):
    pass

class InsufficientFundsException(BankingException):
    pass

class InvalidAmountException(BankingException):
    pass