class Account:
    bank_name = "Absa"

    def __init__(self, balance, account_name,account_number):
        self.balance = balance
        self.account_name = account_name
        self.account_number = account_number
    
    def deposit(self,amount):
        self.balance += amount
        return f"{self.account_name} has deposited {amount} to {self.account_number} and balance is now{self.balance}"
    
    def withdraw(self,amount):
        self.balance -= amount
        return f"{self.account_name} has withdrawn {amount} from {self.account_number} and balance is now{self.balance}"

    def display_details(self):
        return f"{self.account_number} at {self.bank_name} belongs to {self.account_name} and balance is now{self.balance}"
        
