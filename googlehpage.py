import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.google.com/")

status_codes = page.status_code

print(status_codes)

