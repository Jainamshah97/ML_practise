from bs4 import BeautifulSoup
import requests

link = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Science&txtLocation=Bengaluru%2F+Bangalore&cboWorkExp1=0"
link = requests.get(link).text
print("Unfamiliar skills")
unfamiliar_skill=input('>')
# print(link)
soup = BeautifulSoup(link, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    # print(job)
    posting_date = job.find('span', class_='sim-posted').span.text
    #to only get job posted in past few days we can apply following condition
    if 'few' in posting_date:
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        if unfamiliar_skill not in skills:
            company_name = job.find('h3', class_='joblist-comp-name').text

            # print(skills)
            # here span tag another span tag inside so using above span.text

            job_descrip = job.header.h2.a['href']
            # print(posting_date)
            print(f'Company name:{company_name.strip()}')
            print(f'skills:{skills.strip()}')
            # print(job_descrip)
            print(f'posting:{posting_date}')
            print(f'More info:{job_descrip}')
            print('')
# here span tag another span tag inside so using above span.text
