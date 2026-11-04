class Rahunok:
    def __init__(self, vlasnyk, nomer, balans=0):
        self.vlasnyk = vlasnyk
        self.nomer = nomer
        self.balans = balans

    def pokazy(self):
        print("\nДані рахунку:")
        print("Власник:", self.vlasnyk)
        print("Номер:", self.nomer)
        print("Баланс:", self.balans, "грн")

    def popovnyty(self, suma):
        self.balans += suma
        print("Гроші зараховано.")

    def znyaty(self, suma):
        if suma <= self.balans:
            self.balans -= suma
            print("Гроші знято.")
        else:
            print("Йой, грошей троха бракує.")


class Bank:
    def __init__(self):
        self.rahunky = {}

    def dodaty_rahunok(self, rahunok):
        self.rahunky[rahunok.nomer] = rahunok

    def znajty(self, nomer):
        return self.rahunky.get(nomer)

    def perekaz(self, vid_kogo, komu, suma, povidomlennya):
        if suma > vid_kogo.balans:
            print("Не файно, на рахунку нема стільки грошей.")
            return

        vid_kogo.balans -= suma
        komu.balans += suma

        print("\nПереказ пройшов успішно.")
        print("Від:", vid_kogo.vlasnyk)
        print("До:", komu.vlasnyk)
        print("Сума:", suma, "грн")

        if povidomlennya != "":
            print("Повідомлення:", povidomlennya)


bank = Bank()

kilkist = int(input("Скільки рахунків створюємо? "))

for i in range(kilkist):
    print("\nСтворення рахунку", i + 1)

    vlasnyk = input("Ім'я власника: ")
    nomer = input("Номер рахунку: ")
    balans = float(input("Початковий баланс: "))

    bank.dodaty_rahunok(Rahunok(vlasnyk, nomer, balans))

while True:
    print("\n===== МЕНЮ =====")
    print("1 - Переглянути рахунок")
    print("2 - Поповнити рахунок")
    print("3 - Зняти кошти")
    print("4 - Переказати гроші")
    print("5 - Вийти")

    vibir = input("Що робимо? ")

    if vibir == "1":
        nomer = input("Введіть номер рахунку: ")
        rahunok = bank.znajty(nomer)

        if rahunok:
            rahunok.pokazy()
        else:
            print("Такого рахунку нема.")

    elif vibir == "2":
        nomer = input("Номер рахунку: ")
        rahunok = bank.znajty(nomer)

        if rahunok:
            suma = float(input("Скільки закидаємо? "))
            rahunok.popovnyty(suma)
        else:
            print("Такого рахунку нема.")

    elif vibir == "3":
        nomer = input("Номер рахунку: ")
        rahunok = bank.znajty(nomer)

        if rahunok:
            suma = float(input("Скільки знімаємо? "))
            rahunok.znyaty(suma)
        else:
            print("Такого рахунку нема.")

    elif vibir == "4":
        vid = input("Рахунок відправника: ")
        do = input("Рахунок отримувача: ")

        rah_vid = bank.znajty(vid)
        rah_do = bank.znajty(do)

        if rah_vid and rah_do:
            suma = float(input("Сума переказу: "))
            povid = input("Повідомлення до переказу: ")

            bank.perekaz(rah_vid, rah_do, suma, povid)
        else:
            print("Якийсь з рахунків не знайдено.")

    elif vibir == "5":
        print("Бувайте здорові!")
        break

    else:
        print("Та щось не те вибрали, спробуйте ще раз.")
