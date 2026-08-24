import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text,"html.parser")
products = soup.find_all("article",class_="product_pod")
print("products found:",len(products))
scraped_products = []
for product in products:
    name = product.h3.a["title"]
    price = product.find("p",class_="price_color").text
    rating = product.find("p",class_="star-rating")["class"][1]
    availability = product.find("p",class_="instock").text.strip()
    product_url = urljoin(url,product.h3.a["href"])
    product_data = {
    "name": name,
    "price": price,
    "rating": rating,
    "availability": availability,
    "url": product_url
}
scraped_products.append(product_data)
for product in scraped_products:
    print("Name:", product["name"])
    print("Price:", product["price"])
    print("Rating:", product["rating"])
    print("Availability:", product["availability"])
    print("URL:", product["url"])
    print("-" * 50)
print("Name:",name)
print("Price:",price)
print("Rating:",rating)
print("Availability:",availability)
print("URL:",product_url)
