class BankAccount:
    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance


class Bank:
    def deposit(self, account, amount):
        account.balance += amount
        print(f"Рахунок поповнено на {amount} грн")

    def withdraw(self, account, amount):
        if amount <= account.balance:
            account.balance -= amount
            print(f"Знято {amount} грн")
        else:
            print("Недостатньо коштів")

    def transfer(self, sender, receiver, amount):
        if amount <= sender.balance:
            sender.balance -= amount
            receiver.balance += amount
            print(f"Переказано {amount} грн")
        else:
            print("На рахунку недостатньо коштів")

    def show_info(self, account):
        print("Власник:", account.owner)
        print("Номер рахунку:", account.number)
        print("Баланс:", account.balance, "грн")
        print()


acc1 = BankAccount("Остап", "123456", 5000)
acc2 = BankAccount("Іван", "654321", 2000)

bank = Bank()

bank.show_info(acc1)
bank.show_info(acc2)

bank.deposit(acc1, 1000)
bank.withdraw(acc2, 500)
bank.transfer(acc1, acc2, 1500)

print("\nПісля операцій:\n")

bank.show_info(acc1)
bank.show_info(acc2)
