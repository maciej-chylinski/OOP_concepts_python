import savingsAccount as sa
import checkingAccount as ca


def main():

    #task1
    savingsAccount = sa.SavingsAccount(100)
    checkingAccount = ca.CheckingAccount(200)

    print("Savings account balance: $", savingsAccount.get_balance())
    print("Checking account balance: $", checkingAccount.get_balance(), end="\n\n")

    print("Making deposit into checking account for: $ 75 ...")
    checkingAccount.deposit(75)
    print("New checking account balance: $", checkingAccount.get_balance(), end="\n\n")

    print("Making deposit into savings account for: $ 300 ...")
    savingsAccount.deposit(300)
    print("New savings account balance: $", savingsAccount.get_balance(), end="\n\n")

    #task2
    print("Transferring $100 from checking to saving account")
    savingsAccount.transfer(checkingAccount, 100)
    print("New checking account balance: $", checkingAccount.get_balance())
    print("New savings account balance: $", savingsAccount.get_balance())

main()
