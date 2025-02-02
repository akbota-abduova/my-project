class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Пополнено:", amount)
        print("Баланс:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print("Снято:", amount)
            print("Баланс:", self.balance)

owner_name = input("Введите имя владельца счета: ")
balance = int(input("Введите начальный баланс: "))

acc = Account(owner_name, balance)

deposit_amount = int(input("Введите сумму для пополнения: "))
acc.deposit(deposit_amount)

withdraw_amount = int(input("Введите сумму для снятия: "))
acc.withdraw(withdraw_amount)
