class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.mood = 50

    def eat(self):
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0
        print(self.name, "поїв")

    def play(self):
        self.mood += 20
        if self.mood > 100:
            self.mood = 100
        self.hunger += 10
        print(self.name, "грається")

    def sleep(self):
        self.hunger += 5
        print(self.name, "спить")

    def info(self):
        print("Ім'я:", self.name)
        print("Голод:", self.hunger)
        print("Настрій:", self.mood)
        print()


cat = Cat("Барсік")

cat.info()
cat.eat()
cat.play()
cat.sleep()
cat.info()