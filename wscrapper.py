import requests

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print(response.status_code)
