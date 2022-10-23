class BankAccount:

    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print(
                f'Sorry you do not have enough funds to withdraw. Your balance: {self.balance}')
        return self

    def display_account_info(self):
        print(f" balance is {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print('Your account balance is negative')
        return self

    @classmethod
    def print_accounts(cls):
        for i in cls.accounts:
            print(i.display_account_info())
