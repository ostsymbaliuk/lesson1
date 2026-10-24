import random

class Pet:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.money = 100
        self.level = 1
        self.foods = {
            "Корм": 20,
            "М'ясо": 50,
            "Смаколик": 100
        }

    def feed(self):
        print("\nДоступна їжа:")
        for i, (food, price) in enumerate(self.foods.items(), 1):
            print(f"{i}. {food} ({price}$)")

        choice = input("Вибір: ")

        items = list(self.foods.items())

        if choice.isdigit() and 1 <= int(choice) <= len(items):
            food, price = items[int(choice) - 1]

            if self.money >= price:
                self.money -= price

                if food == "Корм":
                    self.hunger = max(0, self.hunger - 20)
                    self.happiness += 5

                elif food == "М'ясо":
                    self.hunger = max(0, self.hunger - 40)
                    self.happiness += 15

                elif food == "Смаколик":
                    self.hunger = max(0, self.hunger - 15)
                    self.happiness += 30

                print(f"{self.name} з'їв(ла) {food}")
            else:
                print("Недостатньо грошей")

    def sleep(self):
        self.energy = min(100, self.energy + 35)
        print(f"{self.name} відпочиває")

    def play(self):
        if self.energy >= 15:
            earnings = random.randint(10, 40)

            self.energy -= 15
            self.hunger += 10
            self.happiness += 20
            self.money += earnings

            print(f"{self.name} грався і заробив {earnings}$")
        else:
            print(f"{self.name} дуже втомився")

    def upgrade(self):
        cost = self.level * 200

        if self.money >= cost:
            self.money -= cost
            self.level += 1
            self.happiness += 20
            print(f"Рівень підвищено до {self.level}")
        else:
            print(f"Потрібно {cost}$")

    def emotions(self):
        if self.hunger >= 80:
            print("Стан: дуже голодний")
        elif self.energy <= 20:
            print("Стан: сонний")
        elif self.happiness >= 80:
            print("Стан: щасливий")
        elif self.happiness <= 20:
            print("Стан: сумний")
        else:
            print("Стан: нормальний")

    def live_time(self):
        self.hunger = min(100, self.hunger + random.randint(5, 10))
        self.energy = max(0, self.energy - random.randint(5, 10))
        self.happiness = max(0, self.happiness - random.randint(2, 5))

    def status(self):
        print("\n---------------------")
        print(f"Ім'я: {self.name}")
        print(f"Тварина: {self.kind}")
        print(f"Рівень: {self.level}")
        print(f"Гроші: {self.money}$")
        print(f"Голод: {self.hunger}/100")
        print(f"Енергія: {self.energy}/100")
        print(f"Щастя: {self.happiness}/100")
        self.emotions()
        print("---------------------")


name = input("Ім'я тваринки: ")
kind = input("Котик чи Собачка: ")

pet = Pet(name, kind)

while True:
    pet.status()

    print("\n1 - Погодувати")
    print("2 - Спати")
    print("3 - Гратися")
    print("4 - Покращення")
    print("5 - Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        pet.feed()

    elif choice == "2":
        pet.sleep()

    elif choice == "3":
        pet.play()

    elif choice == "4":
        pet.upgrade()

    elif choice == "5":
        break

    else:
        print("Невірна команда")

    pet.live_time()