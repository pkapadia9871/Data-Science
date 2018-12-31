class BankAccount:

    def __init__(self,bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
                self.__balance -= amount
        else:
            print('Error : Insufficient funds')

    def get_balance(self):
        return self.__balance

def main():

    start_bal = float(input('Enter your starting balance: '))

    savings = BankAccount(start_bal)

    pay = float(input('How much were you paid this week?'))

    print('I will deposit that into your account. ')

    savings.deposit(pay)

    print('Your account balance is $', \
          format(savings.get_balance(), ',.2f'))

    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    print('Your account balance is $', \
           format(savings.get_balance(), ',.2f'))

main()
