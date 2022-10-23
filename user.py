from bankAccount import BankAccount


class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checking": BankAccount(0.01, 500),
            "savings": BankAccount(0.15, 250)
        }

    def print_balance(self):
        print(
            f"Savings balance is {self.account['savings'].balance} and Checking balance is {self.account['checking'].balance}")

    def transfert(self, client2, amount):
        self.account["checking"].withdraw(amount)
        client2.account["checking"].deposit(amount)
        return self


client1 = User("1")
client2 = User("2")


client1.transfert(client2, 100).print_balance()
client2.print_balance()
