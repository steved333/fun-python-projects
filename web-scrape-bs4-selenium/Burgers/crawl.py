#https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/berlin
#Working python interpreter 3.9.6

from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# page =requests.get("https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/berlin")
driver = webdriver.Chrome()
driver.get("https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/berlin")
sleep(10)
page = driver.page_source
soup = BS(page, 'lxml')

content = soup.find('ul', class_='ubsf_sitemap-list')
restaurantsList = content.find_all('div', class_='ubsf_sitemap-location-address')
print(restaurantsList)
driver.close()