import requests

from bs4 import BeautifulSoup

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# print(response.status_code)

# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())

# print(list(soup.children))

# loop through the children tags and print them out
# print([type(item) for item in list(soup.children)])

# select the html tag by taking the third item in the list

html = list(soup.children)[2]
# print (html)

# find the children inside the html tag

# print(list(html.children))

# get the p tag by finding children of the body tag

body = list(html.children)[3]

# print(body)

list(body.children)

p = list(body.children)[1]

# print(p)

p_text = p.get_text()

# print(p_text)


# using the find_all method to find instances on a page

soup = BeautifulSoup(response.content, 'html.parser')

all_p_instances = soup.find_all('p')

# print(all_p_instances)
