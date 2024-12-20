import getpass

class BankAccount:
    def __init__(self, account_number, name, pin, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = initial_balance

    def verify_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! Current balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful! Current balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def display(self):
        print("\nAccount Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, pin, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, name, pin, initial_balance)
            print("Account created successfully!")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def perform_transaction(self):
        while True:
            print("\n===== WELCOME TO BMS BANKWISE! =====")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Display Account Details")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                account_number = input("Enter account number: ")
                if len(account_number) != 13 or not account_number.isdigit(): 
                 print("Account number must be a 13-digit number.")
                account_number = input("Enter account number: ")
                name = input("Enter account user's name: ")
                pin = getpass.getpass("Set a 6-digit PIN: ")
                while len(pin) != 6 or not pin.isdigit():
                  print("PIN must be a 6-digit number.")
                  pin = getpass.getpass("Set a 6-digit PIN: ")
                  initial_balance = float(input("Enter initial balance: "))
                self.create_account(account_number, name, pin, initial_balance=0)

            elif choice == '2':
                account_number = input("Enter account number: ")
                account = self.get_account(account_number)
                
                if account:
                    pin = getpass.getpass("Enter your PIN: ")
                    if account.verify_pin(pin):
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)
                    else:
                        print("Incorrect PIN.")
                else:
                    print("Account not found.")

            elif choice == '3':
                account_number = input("Enter account number: ")
                account = self.get_account(account_number)
                if account:
                    pin = getpass.getpass("Enter your PIN: ")
                    if account.verify_pin(pin):
                        amount = float(input("Enter withdrawal amount: "))
                        account.withdraw(amount)
                    else:
                        print("Incorrect PIN.")
                else:
                    print("Account not found.")

            elif choice == '4':
                account_number = input("Enter account number: ")
                account = self.get_account(account_number)
                if account:
                    pin = getpass.getpass("Enter your PIN: ")
                    if account.verify_pin(pin):
                        account.display()
                    else:
                        print("Incorrect PIN.")
                else:
                    print("Account not found.")

            elif choice == '5':
                print("Exiting BMS BankWise. Thank You!")

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bank = Bank()
    bank.perform_transaction()