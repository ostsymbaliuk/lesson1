class Car:

    def __init__(self, make, model, year, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.fuel = fuel

    def get_info(self):
        print(f"🚗 Машина: {self.make} {self.model}")
        print(f"📅 Рік: {self.year}")
        print(f"⛽ Бензин: {self.fuel} л")

    def drive(self, liters):
        if self.fuel >= liters:
            self.fuel -= liters

            print(f"💨 Ланос помчав! Витрачено {liters} л бензину.")
            print(f"⛽ Залишилось: {self.fuel} л")

            if self.fuel == 0:
                print("😭 Бензин закінчився!")
                print("🚶 Тепер це пішохідний Ланос.")
        else:
            print("💀 Ланос заглох.")
            print("⛽ Бензину немає.")
            print("🚶 Далі штовхаємо всією сім'єю.")

    def find_fuel(self):
        self.fuel += 5
        print("🎉 Знайшлася каністра в гаражі!")
        print("⛽ +5 л бензину")


lanos = Car("Daewoo", "Lanos", 2007, 10)

lanos.get_info()

lanos.drive(5)
lanos.drive(5)

lanos.find_fuel()

lanos.drive(3)