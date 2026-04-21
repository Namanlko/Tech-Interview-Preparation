# Problem 1:
"""
Create a BankAccount class with:
- Constructor: account_number, holder_name, balance (default 0)
- Methods: deposit(amount), withdraw(amount), get_balance(), display_info()
- Ensure balance never goes negative
"""

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:",amount)
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal denied.")
        else:
            self.balance -= amount
            print("Withdrawn:",amount)

    def get_balance(self):
        return self.balance

    def display_info(self):
        print("Account Number:",self.account_number)
        print("Account Holder:",self.holder_name)
        print("Account Balance:",self.balance)

acc = BankAccount("12345", "John Doe", 1000)

acc.deposit(500)
acc.withdraw(300)
acc.withdraw(1500)  # Should be denied

acc.display_info()
print("Current Balance:", acc.get_balance())
    

    
    
