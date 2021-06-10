import sys
import bs4
import requests
from selenium import webdriver

def fetch_page():
  
  url=input("Enter the Wikipedia URL you want to fetch data from: ")
  
  r=requests.get(url)
  
  soup = bs4.BeautifulSoup(r.content, features="html.parser")
  
  headings = soup.find(id = 'firstHeading') #print (headings.text)
  
  title = headings.text
  
  body = soup.find('div', attrs = {'class':'mw-parser-output'}) #print (body.text)
  
  f = open(title+".txt", "w")
  
  f.write(body.text)
  
  f.close()
  
  
  
  
