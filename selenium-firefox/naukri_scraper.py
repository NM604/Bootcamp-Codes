import sys
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import psycopg2

driver = webdriver.Firefox(executable_path="./drivers/geckodriver")

c = input("Do you want to start fresh?: ")

if c=="y" or c=="Y":
  dbconn = psycopg2.connect("dbname=naukri")
  cur = dbconn.cursor()
  f = open("job.sql")
  sql_code = f.read()
  f.close()
  cur.execute(sql_code)
  dbconn.commit()
  cur.close()
  dbconn.close()
    
job_title = input("Enter the job you're looking for with '-' instead of spaces: ")
l = job_title.split('-')
  
url = "https://www.naukri.com/"+job_title+"-jobs-in-bangalore-bengaluru?k="+l[0]+"%20"+l[1]+"&l=bangalore%2Fbengaluru"
  
driver.get(url)
  
soup = bs4.BeautifulSoup(driver.page_source, features = "html.parser") 

#print (soup.prettify())

driver.close()

results = soup.find(class_='list')

job = results.find_all('article', class_='jobTuple bgWhite br4 mb-8')

dbconn = psycopg2.connect("dbname=naukri")
cur = dbconn.cursor()

for i in job:
  job_titles = i.find('a', class_='title fw500 ellipsis')
  print(job_titles.text)
  company = i.find('div', class_='mt-7 companyInfo subheading lh16')
  company_name = company.find('a', class_='subTitle ellipsis fleft')
  print(company_name.text)
  cur.execute("""INSERT INTO jobs (Job_Title, Company_Name) VALUES (%s,%s)""", (job_titles.text, company_name.text))
  
dbconn.commit()
cur.close()
dbconn.close()
