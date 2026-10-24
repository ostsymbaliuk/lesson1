import random

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"🤑 {self.owner} поповнив рахунок на {money} грн.")
        print(f"💰 Баланс: {self.balance} грн")

    def find_money(self):
        found = random.randint(10, 1000)
        self.balance += found

        places = [
            "на дорозі",
            "під диваном",
            "у старій куртці",
            "у шкільному рюкзаку",
            "біля магазину"
        ]

        place = random.choice(places)

        print(f"🎉 {self.owner} знайшов {found} грн {place}!")
        print(f"💰 Баланс: {self.balance} грн")

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print(f"💸 {self.owner} витратив {money} грн.")
            print(f"💰 Баланс: {self.balance} грн")

            if self.balance == 0:
                print("🐭 У гаманці миша повісилась!")
        else:
            print("🐭 У гаманці миша повісилась!")
            print("🏜️ У гаманці пустеля Сахара!")
            print("😭 Грошей не вистачає!")

user = BankAccount("Остап", 100)

user.withdraw(50)
user.withdraw(100)
user.find_money()
user.withdraw(30)