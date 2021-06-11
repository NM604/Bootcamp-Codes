import sys
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="./drivers/geckodriver")

c = input("What do you want to search on wikipedia for? ")

url = "https://en.wikipedia.org/wiki/"+c

driver.get(url)

soup = bs4.BeautifulSoup(driver.page_source, features = "html.parser") 

driver.close()

results = soup.find('div', class_='mw-body')
content = results.find('div', class_='mw-parser-output')
print(content.text)
