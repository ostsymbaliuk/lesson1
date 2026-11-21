import requests
import re

url = "https://www.toyota.ua/new-cars"

html = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
).text

cars = []

models = [
    "Yaris Cross",
    "Corolla",
    "Corolla Cross",
    "Toyota C-HR",
    "Camry",
    "Toyota bZ4X",
    "RAV4",
    "Land Cruiser Prado",
    "Land Cruiser",
    "Hilux",
    "PROACE CITY"
]

for model in models:

    if model in html:

        part = html[html.find(model):html.find(model) + 3000]

        price = re.findall(r'([\d\s]+)₴', part)

        if len(price) > 0:

            try:

                car_price = int(
                    price[0]
                    .replace(" ", "")
                    .replace("\xa0", "")
                )

                cars.append([model, car_price])

            except:
                pass

if len(cars) == 0:

    print("Не вдалося отримати дані із сайту")
    exit()

print()
print("Доступні автомобілі:")
print()

for i in range(len(cars)):
    print(i + 1, "-", cars[i][0])

print()

choice = int(input("Введіть номер автомобіля: "))

if choice < 1 or choice > len(cars):
    print("Такого авто немає")
    exit()

car_name = cars[choice - 1][0]
car_price = cars[choice - 1][1]

data = requests.get(
    "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11"
).json()

usd = 0

for item in data:

    if item["ccy"] == "USD":
        usd = float(item["sale"])

print()
print("Автомобіль:", car_name)
print("Ціна в гривнях:", car_price)
print("Ціна в доларах:", round(car_price / usd, 2))

salary = float(input("Введіть зарплату: "))

print()
print("1 - Економне харчування")
print("2 - Середнє харчування")
print("3 - Багате харчування")

food = int(input("Ваш вибір: "))

if food == 1:
    food_cost = 1500
elif food == 2:
    food_cost = 5000
elif food == 3:
    food_cost = 10000
else:
    print("Неправильний вибір")
    exit()

rent = 0

home = input("Орендуєте квартиру? (так/ні): ")

if home.lower() == "так":
    rent = float(input("Вартість оренди: "))

utility = 2500

transport = float(input("Транспорт: "))
internet = float(input("Інтернет: "))
phone = float(input("Телефон: "))
other = float(input("Інші витрати: "))

total = (
    food_cost
    + rent
    + utility
    + transport
    + internet
    + phone
    + other
)

save = salary - total

print()
print("Загальні витрати:", total)
print("Залишок грошей:", save)

if save > 0:

    months = car_price / save
    years = months / 12

    print()
    print("Можна відкладати:", round(save, 2))
    print("До покупки авто:", round(months), "місяців")
    print("Або:", round(years, 1), "років")

else:
    print("Грошей для накопичення не залишається")
