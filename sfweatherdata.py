import requests
import json
from bs4 import BeautifulSoup

#   Download the web page containing the forecast.

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.YHEwAhJRXeQ")

# Create a BeautifulSoup class to parse the page.

soup = BeautifulSoup(page.content, 'html.parser')

# Find the div with id seven-day-forecast, and assign to seven_day

seven_day = soup.find(id="seven-day-forecast")

forecast_item = seven_day.find_all(class_="tombstone-container")

# Extract and print the first forecast item.

tonight = forecast_item[0]

# print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()

# description of the conditions

short_desc = tonight.find(class_="short-desc").get_text()

# The temperature low

temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)



