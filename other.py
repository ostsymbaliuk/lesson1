class Animal:

    def __init__(self, name, species, age, lifespan, tail, paws):
        self.name = name
        self.species = species
        self.age = age
        self.lifespan = lifespan
        self.tail = tail
        self.paws = paws

    def grow(self, years=1):
        self.age += years

        if self.age > self.lifespan:
            print(f"💀 {self.name} прожив {self.lifespan} років. На жаль, бобік здох...")
        else:
            print(f"🎉 {self.name} підріс! Тепер йому {self.age} років.")


cat = Animal(
    name="Барсік",
    species="Кіт",
    age=10,
    lifespan=15,
    tail=True,
    paws=4
)

print("Ім'я:", cat.name)
print("Вид:", cat.species)
print("Вік:", cat.age)
print("Тривалість життя:", cat.lifespan)
print("Хвіст:", cat.tail)
print("Лапи:", cat.paws)

cat.grow(3)
cat.grow(5)