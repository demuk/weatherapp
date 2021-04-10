import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.google.com/")

status_codes = page.status_code

print(status_codes)

# print(page.headers)

contents = page.content

# print(contents)

soups = BeautifulSoup(contents, 'html.parser')

# print(soups.prettify())


all_links = soups.find_all('a')

# print(all_links)

all_images = soups.find_all('img')

# print(all_images)


for links in all_links:
    if "Hifadhi" in links.text:
        print(links.attrs['href'])
        

