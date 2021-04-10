import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

# print(soup.find_all('p', class_='outer-text'))

# print(soup.find(id='first'))

print(soup.select('div p'))


