import sys
import requests
import bs4
import psycopg2

def parse():

  url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="
  headers = {"appid":"109","systemid":"109"}
  r = requests.get(url,headers=headers)
  data = r.json()
  jobs = data['jobDetails']
  
  dbconn = psycopg2.connect("dbname=naukri")
  cur = dbconn.cursor()
  for i in jobs:
    job_id = i['jobId']
    title = i['title']
    company_name = i['companyName']
    job_url = i['jdURL']
    soup = bs4.BeautifulSoup(i['jobDescription'], features='html.parser')
    job_description = str(soup.text)
    cur.execute("""INSERT INTO openings (job_id, title, company_name, job_description, job_url) VALUES (%s,%s,%s,%s,%s)""", (job_id, title, company_name, job_description, job_url))
  dbconn.commit()
  cur.close()
  dbconn.close()
  
  
