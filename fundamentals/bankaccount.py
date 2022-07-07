class BankAccount:
    #declaring class attribute, has to be outside init
    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        #need to add to all_account list for class function
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"You have {self.balance} remaining")
        elif self.balance < amount:
            self.balance - 5
            print(f"Insufficient funds, charging a $5 fee. New balance is {self.balance}")
        return self

    def display_account_info(self):
        print(f"Balance is {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    #declare with @classmethod and pass cls. return cls instead of self? loop and print
    @classmethod
    def account_balance(cls):
        for account in cls.all_accounts:
            print(account.balance)
        return cls

user1 = BankAccount(0.01,0).deposit(10).deposit(20).deposit(30).withdraw(50).yield_interest() #expecting 10.1 to display, 60 in dep 50 withdrawn 10 * .01 interest
user2 = BankAccount(.01, 0).deposit(20).deposit(20).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest() #expecting to see 20.2, 40 in deposits, 20 in withdrawl 0.01 interest
#challenge - use a class to display all account info
BankAccount.account_balance()