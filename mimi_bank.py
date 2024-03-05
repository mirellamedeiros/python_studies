# here we are going to make a bank by creating two types of "accounts", a current account and a savings account
# both of these accounts will inherit from the account parent class, being able to deposit and withdraw money,
# and also print a stayman, however each account will have different minimum limits, and the current account will have
# an overdraft of a thousand :D

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds :(")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000 )

    def __str__(self):  # defining a string function so the result is more readable
        return "{}'s Current Account : Balance £{}".format(self.name, self.balance)


mimi_account = Current("Mimi", 500)
print(mimi_account)
mimi_account.deposit(300)
mimi_account.withdraw(1000)
mimi_account.withdraw(800)
mimi_account.statement()  # after a £1000 overdraft...
mimi_account.withdraw(1)  # you can't withdraw any more money!

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance)


babi_account = Savings("Babi", 300)
print(babi_account)
babi_account.withdraw(300)
babi_account.statement()
babi_account.withdraw(1)  # with a savings account you can't have any overdraft !!
