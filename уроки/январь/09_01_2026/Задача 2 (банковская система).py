#Transaction, BankAccount
import datetime
class Transaction:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type
        self.date = datetime.datetime.now()

    def __str__(self):
        return f'{self.amount} - {self.type} - {self.date}'


class BankAccount:
    def __init__(self, id_account, balance, user_name):
        self.id_account = id_account
        self.balance = balance
        self.user_name = user_name
        self.transactions = []
        self.active = True

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transactions = Transaction(amount, 'deposit')
            self.transactions.append(transactions)
            print(f'Пополнение на {amount}. Баланс: {self.balance}')
        else:
            raise ValueError('Баланс должен быть положительным')

    def withdraw(self, amount):
        if amount > 0 and self.balance > amount:
            self.balance -= amount
            transactions = Transaction(amount, 'withdraw')
            self.transactions.append(transactions)
            print(f'Снятие на {amount}. Баланс: {self.balance}')
        else:
            raise ValueError('Баланс должен быть положительным или сумма снятия должна быть больше баланса')

    def transfer(self, amount, target_account_1):
        self.withdraw(amount)
        target_account_1.deposit(amount)
        print(f'{self.balance}, {target_account_1.balance}')


class SavingAccount(BankAccount):
    def __init__(self, id_account, balance, user_name, rate=0.05):
        super().__init__(id_account, balance, user_name)
        self.rate = rate

    def apply_interest(self):
        interest = self.rate * self.balance / 12
        self.deposit(interest)

    def withdraw(self, amount):
        super().withdraw(amount)


s = SavingAccount(3, 111, 'Alex')
s.apply_interest()

bank1 = BankAccount(1, 10000, 'Alex')
bank2 = BankAccount(2, 5000, 'Boris')
bank1.deposit(100)
bank1.withdraw(300)

bank2.transfer(200, bank1)
