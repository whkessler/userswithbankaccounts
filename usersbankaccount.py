class User:
    def __init__ (self,name):
        self.name = name
        self.account = BankAccount(int_rate=.02, balance =0)
    def deposit(self, amount):
        self.account += amount
    def withdraw(self,amount):
        if amount > self.account:
            print ("insufficient funds")
        self.account -= amount
    def display_user_balance(self):
        print (self.account)

class BankAccount:
    def __init__ (self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if amount > self.balance:
            print ("insufficient funds:Charging a $5 fee")
        self.balance -= amount
        return self
    def display_account_info(self):
        print (("Balance:$"),self.balance,("Interest Rate:"),self.int_rate)
        if self.balance < 0:
            print(("Balance with fee :$"), self.balance - 5)
        return self
    def yeild_interest(self):
        print (("Interest Yielded:$"),self.balance * self.int_rate)
        print(("New Balance:$"), (self.balance*self.int_rate)+self.balance)
        return self

self = User("John Smith")
self = User("Andrew Jones")
self = User("Jane Curtan")
self.account.deposit(100)
self.account.deposit(360)
self.account.deposit(20)
self.account.withdraw(330)
print(self.account.balance)
self.account.deposit(3245)
self.account.deposit(23)
self.account.withdraw(654)
self.account.withdraw(345)
print(self.account.balance)
self.account.deposit(1000)
self.account.withdraw(25)
self.account.withdraw(345)
self.account.withdraw(999)
print(self.account.balance)