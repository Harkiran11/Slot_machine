from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, number: int, balance: float = 0.0):
        self.number = number
        self.balance = balance
    
    def check_balance(self) -> float:
        return self.balance
    
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
    
    def deposit(self, amount: float) -> None:
        self.balance += amount
    
    @abstractmethod
    def print(self) -> None:
        pass

class SavingsAccount(Account):
    def __init__(self, number: int, interest_rate: float, balance: float = 0.0):
        super().__init__(number, balance)
        self.interest_rate = interest_rate
    
    def calculate_return(self) -> float:
        return self.balance * self.interest_rate
    
    def print(self) -> None:
        print(f"Savings Account #{self.number}: Balance = ${self.balance:.2f}, Interest Rate = {self.interest_rate:.2f}")

class CheckingAccount(Account):
    def __init__(self, number: int, balance: float = 0.0):
        super().__init__(number, balance)
    
    def transaction(self, amount: float) -> None:
        self.withdraw(amount)
    
    def print(self) -> None:
        print(f"Checking Account #{self.number}: Balance = ${self.balance:.2f}")

class Customer:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = []
    
    def open_savings_account(self, number: int, interest_rate: float) -> None:
        account = SavingsAccount(number, interest_rate)
        self.accounts.append(account)
    
    def open_checking_account(self, number: int) -> None:
        account = CheckingAccount(number)
        self.accounts.append(account)
    
    def print_accounts(self) -> None:
        print(f"Customer: {self.first_name} {self.last_name}")
        for account in self.accounts:
            account.print()

# Example usage
customer = Customer("John", "Doe")
customer.open_savings_account(101, 0.05)
customer.open_checking_account(102)
customer.accounts[0].deposit(1000)
customer.accounts[1].deposit(500)
customer.accounts[1].transaction(200)
customer.print_accounts()
