#https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/berlin
#Working python interpreter 3.9.6

from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import csv
import os


url = input("what url are you scraping? ")
driver = webdriver.Chrome()
driver.get(url)
sleep(5)
page = driver.page_source
soup = BS(page, 'lxml')

content = soup.find('ul', class_='ubsf_sitemap-list')
restaurantsList = content.find_all('div', class_='ubsf_sitemap-location-address')


# try:
#   os.mkdir("web-scrape-bs4-selenium/Burgers/CSV")
# except OSError as e:
#   print("Directory exists")

with open('restaurant.txt', 'w') as file:
  file.write(str(soup))


with open('CSV/restaurant.csv', mode='w', newline='') as outputFile:
  restaurantCSV = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  restaurantCSV.writerow((['restaurant', 'street', 'zip', 'city', 'country']))

  restaurants = 'McDonalds'
  city = 'Berlin'
  country = 'Germany'

  for restaurant in restaurantsList:
    street = restaurant.text.split(',')[0]
    zip = restaurant.text.split(',')[1:6]
    restaurantCSV.writerow(([restaurants, street, zip, city, country]))

driver.close()