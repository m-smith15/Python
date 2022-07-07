class BankAccount:
    #declaring class attribute, has to be outside init
    all_accounts = []

    def __init__(self, int_rate, balance, accountname): 
        self.int_rate = int_rate
        self.balance = balance
        self.accountname = accountname
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
        print(f"Balance is {self.balance} for account {self.accountname}")
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
#creating user class
class User:
    
    user_accounts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def user_createAccount(self,int_rate, balance, accountname):
        self.account = BankAccount(int_rate, balance, accountname) #pass in accountname when creating account, then append to list - can use to loop through accounts in classmethod below.
        # User.user_accounts.append(self) #getting error here - why? Same as BankAccount?
        return self
        

    def user_deposit(self, amount): #user CLASS instance reaching out to bankaccount CLASS' deposit method and depositing amount
        self.account.deposit(amount)
        return self
    
    def user_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    
    def user_display_info(self):
        self.account.display_account_info()
        return self

    @classmethod
    def user_accounts(cls):
        for account in cls.user_accounts:
            print(account.accountname)
        return cls

# user1 = BankAccount(0.01,0).deposit(10).deposit(20).deposit(30).withdraw(50).yield_interest() #expecting 10.1 to display, 60 in dep 50 withdrawn 10 * .01 interest
# user2 = BankAccount(.01, 0).deposit(20).deposit(20).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest() #expecting to see 20.2, 40 in deposits, 20 in withdrawl 0.01 interest
# #challenge - use a class to display all account info
# BankAccount.account_balance()

user_one = User("Example", "lobster@ocean.gov")
user_one.user_createAccount(0.01, 0, "Fishing").user_display_info()
#.user_createAccount("Shrimping").user_display_info()
#User.user_accounts()
user_two = User("Test","shrimp@ocean.gov")
#user_one.user_display_info()