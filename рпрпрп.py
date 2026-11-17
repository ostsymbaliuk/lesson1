import requests

response = requests.get("http://books.toscrape.com/")
response_text = response.text

kurs_response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
kurs_text = kurs_response.json()

usd_uah = float(kurs_text[0]["sale"])

books_info = []

books = response_text.split('<article class="product_pod">')

for book in books[1:]:

    title = book.split('title="')[1].split('"')[0]

    title = title.replace("&#39;", "'")
    title = title.replace("&amp;", "&")
    title = title.replace("&quot;", '"')

    price = book.split('<p class="price_color">')[1].split("</p>")[0]

    stock = book.split('<p class="instock availability">')[1].split("</p>")[0]

    if "In stock" in stock:
        stock = "В наявності"
    else:
        stock = "Немає в наявності"

    price_gbp = price.replace("Â£", "")
    price_gbp = price_gbp.replace("£", "")
    price_gbp = float(price_gbp)

    gbp_usd = 1.25

    price_usd = round(price_gbp * gbp_usd, 2)

    price_uah = round(price_usd * usd_uah, 2)

    books_info.append({
        "title": title,
        "price": price,
        "stock": stock,
        "price_uah": price_uah
    })

print("ЗАВДАННЯ 1")
print("Назви всіх книг")
print()

for book in books_info:
    print(book["title"])

print()
print("ЗАВДАННЯ 2")
print("Ціни всіх книг")
print()

for book in books_info:
    print(book["price"])

print()
print("ЗАВДАННЯ 3")
print("Інформація про всі книги")
print()

for book in books_info:
    print("Назва:", book["title"])
    print("Ціна:", book["price"])
    print("Курс долара:", usd_uah)
    print("Ціна в гривнях:", book["price_uah"])
    print("Наявність:", book["stock"])
    print("--------------------")