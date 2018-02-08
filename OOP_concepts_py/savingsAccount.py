class BankAccount():

    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enough money on banl account")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):

    def __init__(self, balance):
        BankAccount.__init__(self, balance)

    def get_balance(self):
        #print("Savings account balance: $", BankAccount.get_balance(self))
        return BankAccount.get_balance(self)

    def transfer(self, accountObj, amount):
        if amount > accountObj.get_balance():
            print("Not enoungh funds.")
        else:
            accountObj.withdraw(amount)
            self.deposit(amount)