import requests

from bs4 import BeautifulSoup

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# print(response.status_code)

# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())

# print(list(soup.children))

# loop through the children tags and print them out
print([type(item) for item in list(soup.children)])

