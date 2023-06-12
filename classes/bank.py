class Account:
    bank_name = "Absa"
    transaction_charge_percent = 10

    #Add attributes deposits and withdrawals in the init method which are empty
    #lists by default and another attribute loan_balance which is zero by default.

    def __init__(self, balance, account_name,account_number):
        self.balance = balance
        self.account_name = account_name
        self.account_number = account_number
        self.deposits = []
        self.withdrawls = []
        self.loan_balance= 0
        
    
    def deposit(self,amount):
        self.balance += amount
        withdrawal_transaction = {"amount":amount, "naration":deposits}
        self.deposits.append(withdrawal_transaction)
        return f"{self.account_name} has deposited {amount}, the balance is {self.balance}."
        # return f"{self.account_name} has deposited {amount} to {self.account_number} and balance is now{self.balance}"
    
    def withdraw(self,withdrawn_amount):
        self.balance -= withdrawn_amount
        withdrawal_transaction = {"amount":withdrawn_amount, "naration":withdrwals}
        self.deposits.append(withdrawal_transaction)
        return f"{self.account_name} has withdhdrawn {withdrawn_amount}, the balance is {self.balance}."
        # return f"{self.account_name} has withdrawn {amount} from {self.account_number} and balance is now{self.balance}"

    def display_details(self):
        return f"{self.account_number} at {self.bank_name} belongs to {self.account_name} and balance is now{self.balance}"

    def check_balance (self):
        return f"Dear {self.account_name} your balance for account no. {self.account_number} is {self.balance}"
    
    #Add a new method  print_statement which combines both deposits and withdrawals into one list
    #  and, using a for loop, prints each transaction in a new line like this 
    # deposit - 1000
    # withdrawal - 500
    def print_statement(self):
        deposit_and_withdrawals = []
        for transaction in self.withdrawal_transaction:
            if transaction > 0:
                deposit_and_withdrawals.append("withdrawal - " + (withdrawn_amount))
            else:
                deposit_and_withdrawals.append("withdrawal - " + (amount))
        for transaction in deposit_and_withdrawals:
            print(transaction)
    
    def borrow_loan(self, amount):
        total_deposits=sum([t[amount] for t in self.deposits])
        limit = total_deposits/3

        if self.loan_balance > 0:
            return "You already have an outstanding loan"
        elif amount <= 100:
            return "Loan amount must be greater than 100"
        elif len(self.deposits) < 10:
            return "You must have made at least 10 deposits to be eligible for a loan"
        elif amount > sum([deposit['amount'] for deposit in self.deposits])/3:
            return "Loan amount requested is more than 1/3 of your total deposits"
        else:
            self.loan_balance += amount
            self.balance +=amount
            return f"Your loan of ${amount} was successful. Your new account balance is ${self.balance}"
    def repay_loan(self, amount):
        if amount > self.loan_balance:
            self.balance += amount - self.loan_balance
            self.loan_balance = 0
            return f"You have successfully repaid your loan. Your new balance is ${self.balance}"
        else:
            self.loan_balance -= amount
            return f"You have successfully repaid ${amount} of your loan. Your new loan balance is ${self.loan_balance}"
    def transfer(self, amount, account):
        total_amount = amount +(amount*transaction_charge_percent/10)
        if amount > self.balance:
            return f"Insufficient funds. Your current balance is ${self.balance}"
        else:
            self.balance -= amount
            account.deposit(amount)
            return f"You have successfully transferred ${amount} to account {account.account_number}. Your new balance is ${self.balance}"





