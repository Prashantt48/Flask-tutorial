import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    filename="banking.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Customer class
class Customer:
    def __init__(self, customer_id, name, phone):
        if not all(
            isinstance(value, str) and value.strip()
            for value in (customer_id, name, phone)
        ):
            raise ValueError("Customer details cannot be empty.")

        self.__customer_id = customer_id.strip()
        self.__name = name.strip()
        self.__phone = phone.strip()

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if not isinstance(phone, str) or not phone.strip():
            raise ValueError("Phone number cannot be empty.")
        self.__phone = phone.strip()


# Abstract Account class
class Account(ABC):
    total_accounts = 0

    def __init__(self, account_number, customer, initial_balance=0):
        if not isinstance(account_number, str) or not account_number.strip():
            raise ValueError("Account number cannot be empty.")

        if not isinstance(customer, Customer):
            raise TypeError("A valid Customer object is required.")

        if (
            not isinstance(initial_balance, (int, float))
            or isinstance(initial_balance, bool)
        ):
            raise TypeError("Initial balance must be numeric.")

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.__account_number = account_number.strip()
        self.__customer = customer
        self.__balance = float(initial_balance)

        Account.total_accounts += 1
        logging.info("Account created: %s", self.__account_number)

    def get_account_number(self):
        return self.__account_number

    def get_customer(self):
        return self.__customer

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount, allow_overdraft=False):
        if not allow_overdraft and amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = float(amount)

    @staticmethod
    def get_total_accounts():
        return Account.total_accounts

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def display_details(self):
        print("\nAccount Number:", self.get_account_number())
        print("Customer ID:", self.__customer.get_customer_id())
        print("Customer Name:", self.__customer.get_name())
        print("Phone:", self.__customer.get_phone())
        print("Account Type:", type(self).__name__)
        print(f"Balance: Rs. {self.get_balance():.2f}")


# Savings Account
class SavingsAccount(Account):
    def __init__(
        self, account_number, customer, initial_balance=500,
        minimum_balance=500
    ):
        if (
            not isinstance(minimum_balance, (int, float))
            or isinstance(minimum_balance, bool)
            or minimum_balance < 0
        ):
            raise ValueError("Minimum balance must be non-negative.")

        if (
            not isinstance(initial_balance, (int, float))
            or isinstance(initial_balance, bool)
            or initial_balance < minimum_balance
        ):
            raise ValueError(
                "Initial deposit must meet the minimum balance."
            )

        super().__init__(account_number, customer, initial_balance)
        self.minimum_balance = float(minimum_balance)

    def deposit(self, amount):
        try:
            if (
                not isinstance(amount, (int, float))
                or isinstance(amount, bool)
                or amount <= 0
            ):
                raise ValueError("Deposit must be a positive number.")

            self._update_balance(self.get_balance() + amount)
            logging.info(
                "Deposit successful for account %s",
                self.get_account_number()
            )
            print("Deposit successful.")

        except (ValueError, TypeError) as error:
            logging.error("Savings deposit failed: %s", error)
            print("Error:", error)

    def withdraw(self, amount):
        try:
            if (
                not isinstance(amount, (int, float))
                or isinstance(amount, bool)
                or amount <= 0
            ):
                raise ValueError("Withdrawal must be positive.")

            remaining = self.get_balance() - amount

            if remaining < self.minimum_balance:
                raise ValueError(
                    "Insufficient funds or minimum balance violation."
                )

            self._update_balance(remaining)
            logging.info(
                "Withdrawal successful for account %s",
                self.get_account_number()
            )
            print("Withdrawal successful.")

        except (ValueError, TypeError) as error:
            logging.error("Savings withdrawal failed: %s", error)
            print("Error:", error)


# Checking Account
class CheckingAccount(Account):
    def __init__(
        self, account_number, customer, initial_balance=0,
        overdraft_limit=2000
    ):
        if (
            not isinstance(overdraft_limit, (int, float))
            or isinstance(overdraft_limit, bool)
            or overdraft_limit < 0
        ):
            raise ValueError("Overdraft limit must be non-negative.")

        super().__init__(account_number, customer, initial_balance)
        self.overdraft_limit = float(overdraft_limit)

    def deposit(self, amount):
        try:
            if (
                not isinstance(amount, (int, float))
                or isinstance(amount, bool)
                or amount <= 0
            ):
                raise ValueError("Deposit must be a positive number.")

            self._update_balance(self.get_balance() + amount)
            logging.info(
                "Deposit successful for account %s",
                self.get_account_number()
            )
            print("Deposit successful.")

        except (ValueError, TypeError) as error:
            logging.error("Checking deposit failed: %s", error)
            print("Error:", error)

    def withdraw(self, amount):
        try:
            if (
                not isinstance(amount, (int, float))
                or isinstance(amount, bool)
                or amount <= 0
            ):
                raise ValueError("Withdrawal must be positive.")

            remaining = self.get_balance() - amount

            if remaining < -self.overdraft_limit:
                raise ValueError("Overdraft limit exceeded.")

            self._update_balance(remaining, allow_overdraft=True)
            logging.info(
                "Withdrawal successful for account %s",
                self.get_account_number()
            )
            print("Withdrawal successful.")

        except (ValueError, TypeError) as error:
            logging.error("Checking withdrawal failed: %s", error)
            print("Error:", error)


# Bank class
class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = {}
        self.__customers = {}

    def add_customer(self, customer):
        customer_id = customer.get_customer_id()

        if customer_id in self.__customers:
            raise ValueError("Customer ID already exists.")

        self.__customers[customer_id] = customer
        logging.info("Customer registered: %s", customer.get_name())

    def get_customer(self, customer_id):
        customer = self.__customers.get(customer_id)

        if customer is None:
            raise ValueError("Customer not found.")

        return customer

    def create_account(self, account):
        number = account.get_account_number()

        if number in self.__accounts:
            raise ValueError("Account number already exists.")

        customer_id = account.get_customer().get_customer_id()

        if customer_id not in self.__customers:
            raise ValueError("Register the customer before opening an account.")

        self.__accounts[number] = account
        logging.info("Account registered: %s", number)

    def get_account(self, account_number):
        account = self.__accounts.get(account_number)

        if account is None:
            raise ValueError("Account not found.")

        return account

    def display_all_accounts(self):
        if not self.__accounts:
            print("No accounts available.")
            return

        for account in self.__accounts.values():
            account.display_details()

    def get_total_accounts(self):
        return len(self.__accounts)


# Main program
def main():
    bank = Bank("Python National Bank")

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Register Customer")
        print("2. Open Savings Account")
        print("3. Open Checking Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Check Balance")
        print("7. Display All Accounts")
        print("8. Total Accounts")
        print("9. Update Customer Phone")
        print("10. Exit")

        try:
            choice = input("Enter choice: ").strip()

            if choice == "1":
                customer_id = input("Customer ID: ").strip()
                name = input("Customer name: ").strip()
                phone = input("Phone number: ").strip()

                customer = Customer(customer_id, name, phone)
                bank.add_customer(customer)
                print("Customer registered successfully.")

            elif choice in ("2", "3"):
                customer_id = input("Customer ID: ").strip()
                customer = bank.get_customer(customer_id)

                account_number = input("Account number: ").strip()
                initial = float(input("Initial deposit: "))

                if choice == "2":
                    account = SavingsAccount(
                        account_number, customer, initial
                    )
                else:
                    limit = float(input("Overdraft limit: "))
                    account = CheckingAccount(
                        account_number, customer, initial, limit
                    )

                bank.create_account(account)
                print("Account opened successfully.")

            elif choice in ("4", "5", "6"):
                number = input("Account number: ").strip()
                account = bank.get_account(number)

                if choice == "4":
                    amount = float(input("Deposit amount: "))
                    account.deposit(amount)

                elif choice == "5":
                    amount = float(input("Withdrawal amount: "))
                    account.withdraw(amount)

                else:
                    print(f"Balance: Rs. {account.get_balance():.2f}")

            elif choice == "7":
                bank.display_all_accounts()

            elif choice == "8":
                print("Accounts registered in bank:",
                      bank.get_total_accounts())
                print("Total accounts created:",
                      Account.get_total_accounts())

            elif choice == "9":
                customer_id = input("Customer ID: ").strip()
                customer = bank.get_customer(customer_id)
                phone = input("New phone number: ").strip()
                customer.set_phone(phone)
                print("Phone number updated successfully.")

            elif choice == "10":
                print("Thank you for using the banking system.")
                break

            else:
                print("Invalid choice. Please enter 1-10.")

        except (ValueError, TypeError) as error:
            logging.error("Operation failed: %s", error)
            print("Error:", error)

        except (EOFError, KeyboardInterrupt):
            print("\nProgram terminated.")
            break

        except Exception:
            logging.exception("Unexpected banking system error")
            print("Unexpected error. Check banking.log.")


if __name__ == "__main__":
    main()