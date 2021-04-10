import requests
from bs4 import BeautifulSoup

# obtain links from the website

page = requests.get('https://www.whitehouse.gov/briefing-room/')

status_codes = page.status_code
print(status_codes)

contents = page.content

soups = BeautifulSoup(contents, 'html.parser')

urls = []

for all_tags in soups.find_all("h2"):
    a_tag = all_tags.find("a")
    print(a_tag.atrrs)
    urls.append(a_tag)

# print(urls)