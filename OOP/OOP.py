class BalanceException(Exception) : 
    pass

class BankAccount :
    def __init__(self, initialAmount, accName):
        self.balance :int = initialAmount
        self.name :str = accName
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f}")

    def getBalance(self) -> None :
        print(f"\nAccount {self.name} \nBalance = ${self.balance}")

    def deposit(self, amount) -> None :
        self.balance += amount
        self.getBalance()

    def viableTransaction(self, amount) :
        if self.balance >= amount :
            return
        else :
            raise BalanceException(
                f"\n Sorry account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount) :
        try :
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete")
            self.getBalance()

        except BalanceException as error :
            print(f"\nWithdraw interrupted : {error}")

    def transfer(self, amount, account) :
        try :
            print('*******\n\nBegining Transfer..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!\n\n**********')
        except BalanceException as error :
            print(f"\nTransfer interrupt.")

class InterestRewardsAcct(BankAccount) :
    def deposit(self, amount):
        self.balance :int= self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()
    
class SavingAcct(InterestRewardsAcct) :
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee :int = 5

    def withdraw(self, amount):
        try : 
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nwithdraw completed.")
            self.getBalance()
        except BalanceException as error :
            print(f"\nWithdraw interrupted: {error}")



if __name__ == "__main__" :
    sanmi = BankAccount(100,"sanmi")
    gozan = BankAccount(200,"gozan")
    
    agus = SavingAcct(1000,"agus")
    agus.withdraw(1005)