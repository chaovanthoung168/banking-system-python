# Banking System Python

A console-based Banking Management System built with **Python**, **object-oriented programming (OOP)**, and a **layered MVC architecture**. This learning project demonstrates service and repository abstractions, dependency injection, custom exceptions, and unit testing.

## Features

- Create bank accounts with an opening balance
- List and find accounts
- Deposit and withdraw funds
- Transfer funds between accounts
- Validate amounts and handle common banking errors
- Store accounts in memory (no database required)

## Tech stack

- Python 3.10+
- Python standard library (`abc`, `dataclasses`, `decimal`, `uuid`, `unittest`)
- MVC-inspired layered architecture

## Project structure

```text
banking-system-python/
├── main.py
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── bank_account.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── account_repository.py
│   │   └── account_repository_impl.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── banking_service.py
│   │   └── impl/
│   │       ├── __init__.py
│   │       └── banking_service_impl.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── banking_controller.py
│   ├── views/
│   │   ├── __init__.py
│   │   └── banking_view.py
│   └── exceptions/
│       ├── __init__.py
│       └── banking_exception.py
└── tests/
    └── test_banking_service.py
```

## Architecture

```text
User → Console View → Banking Controller → Banking Service (ABC)
                                            ↓
                                    Banking Service Impl
                                            ↓
                                    Account Repository (ABC)
                                            ↓
                                    Account Repository Impl
                                            ↓
                                        BankAccount
```

| Layer | Responsibility |
| --- | --- |
| Model | Represents a bank account |
| View | Handles terminal input and output |
| Controller | Delegates requests to the service |
| Service interface | Defines banking operations with `ABC` and `@abstractmethod` |
| Service implementation | Validates requests and applies banking rules |
| Repository interface | Defines storage operations |
| Repository implementation | Stores accounts in a Python dictionary |

Dependencies are passed through constructors in `main.py`, similar to constructor injection in Java Spring Boot.

## Getting started

### Requirements

Install Python 3.10 or newer. Verify:

```bash
python --version
```

### Clone

```bash
git clone https://github.com/chaovanthoung168/banking-system-python.git
cd banking-system-python
```

> Replace the clone URL if your GitHub repository uses a different owner or name.

### Optional virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No third-party dependencies are required for the current version.

### Run

From the project root:

```bash
python main.py
```

The application displays a menu:

```text
====== BANKING SYSTEM ======
1. Create Account
2. View All Accounts
3. Find Account
4. Deposit
5. Withdraw
6. Transfer
0. Exit
```

## Example workflow

1. Select **1** to create an account for Alice with an initial balance of `500.00`.
2. Copy the generated account number.
3. Select **4** to deposit `100.00`.
4. Select **3** to view the account. The balance should be `600.00`.
5. Create another account and select **6** to transfer money to it.

Money is represented using Python's `Decimal` type instead of `float` to avoid binary floating-point rounding issues.

## Run tests

```bash
python -m unittest discover -s tests -v
```

Tests cover basic account creation, deposits, and insufficient-balance withdrawals.

## Learning objectives

- Classes, constructors, inheritance, and encapsulation
- Abstract base classes as service/repository contracts
- Dependency injection and separation of concerns
- Custom exceptions and input validation
- Unit testing with `unittest`

## Limitations

**For educational use only — not a real banking application.** Data is stored in memory and is lost when the program exits. This example does not implement authentication, authorization, durable transaction records, concurrency controls, or atomic database transactions. It must not be used to manage real funds.

## Potential improvements

- SQLite or PostgreSQL persistence
- Atomic transfers and transaction history
- Better encapsulation of account balances
- Authentication and authorization
- REST API using FastAPI
- More unit and integration tests

## License

No license has been specified yet. Add a `LICENSE` file if you want to define how others may use or contribute to this project.
