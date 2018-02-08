class BankAccount():

    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class CheckingAccount(BankAccount):
    def __init__(self, initial_balance):
        BankAccount.__init__(self, initial_balance)

    def get_balance(self):
        #print("Checking account balance: $", BankAccount.get_balance(self))
        return BankAccount.get_balance(self)

    def transfer(self, accountObj, amount):
        if amount > accountObj.get_balance():
            print("Not enoungh funds")
        else:
            accountObj.withdraw(amount)
            self.deposit(amount) 