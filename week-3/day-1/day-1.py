import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.nytimes.com/international/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='css-xdandi')
data = []

for article in articles[:2]:
    title = article.find('h3', class_='indicate-hover').text.strip()
    description_element = article.find('p', class_='summary-class')
    if description_element:
        description = description_element.text
    else:
        description = 'Description not found'
    data.append({'title': title, 'description': description})

print(data)

with open('nytimes.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'description'])
    writer.writeheader()
    writer.writerows(data)
