import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.jumia.co.ke/mlp-warehouse-clearance-sale/")

status_code = page.status_code

print(status_code)

contents = page.content


soups = BeautifulSoup(contents, 'html.parser')

article_items = soups.find_all(class_="prd _fb _p col c-prd")

print(article_items)


'''
for item in article_items:
    if 'shoes' in item:
        print(shoe)

'''