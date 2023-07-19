import requests
from bs4 import BeautifulSoup
import csv

url = 'https://jiji.co.ke/cars'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_='b-list-advert__gallery__item')
data = []

for product in products:
    title = product.find('div', class_='b-advert-title-inner').text.strip()
    price_element = product.find('div', class_='qa-advert-price')
    if price_element:
        price = price_element.text.strip()
    else:
        price = 'Price not found'
    img_element = product.find('img')
    if img_element:
        img_url = img_element.get('src')
    else:
        img_url = 'Image not found'
    data.append({'title': title, 'price': price, 'url': img_url})

with open('jiji.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'price', 'url'])
    writer.writeheader()
    writer.writerows(data)
