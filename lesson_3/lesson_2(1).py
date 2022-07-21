from cgitb import text
import json
import requests
from bs4 import BeautifulSoup
from transliterate import translit, get_available_language_codes
import pymongo
from pymongo import MongoClient

#shamaning with Mongo Client
client = MongoClient('mongodb://localhost:27017')
db = client.vacancydb
#list of dicts of vacancies (not needed for homework 3)
#main_list = []
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
text_translite=translit(input('write name of vacancy here:').replace(' ', '_').replace("'", "").lower(), 'ru', reversed=True)
url = 'https://hh.ru/search/vacancy'
params = {'text': text_translite, 'page': '0'}
page_counter = 0
session = requests.Session()
while True:
    resp = session.get(url, headers=headers, params=params)
    dom = BeautifulSoup(resp.content, 'html.parser')
    page = dom.find('div', attrs= {'class':'pager'}).find('a', attrs={'data-qa':'pager-next'})
    if page == None:
        break
    vacancy = dom.find_all('div', attrs={'class':'vacancy-serp-item-body__main-info'})
    for i in vacancy:
        vacancy_name = i.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'}).text
#finding link on vacancy        
        vacancy_link = i.find('a', attrs={'data-qa':'vacancy-serp__vacancy-title'})['href']
#checking that link on our db
        finder = db.vacancy.find({'link':{'$eq':vacancy_link}})
        for i in finder:
            if i['link'] != vacancy_link:
                salary_dict = {'name': vacancy_name, 'salary':'', 'link': vacancy_link, 'from': 'https://hh.ru/'}
                vacancy_salary = i.find('span', attrs={'data-qa':'vacancy-serp__vacancy-compensation'})
#making list of vacancy salary
                if vacancy_salary != None:
                    vacancy_salary=vacancy_salary.text
                    splited_salary = vacancy_salary.split(' ')
                    try:
                        splited_salary.remove('–')
                    except ValueError:
                        pass
                    try:
                        splited_salary.remove('от')
                    except ValueError:
                        pass
                    salary_list = []
#making int from strings 
                    if splited_salary[-1] =='руб.':
                        for i in splited_salary:
                            if len(i)> 5:
                                if len(i)<7:
                                    d = i[:2]
                                    j= i[-3:]
                                    salary_digit = int(''.join([d,j]))
                                    salary_list.append(salary_digit)
                                else:
                                    d=i[:3]
                                    j=i[-3:]
                                    salary_digit = int(''.join([d,j]))
                                    salary_list.append(salary_digit)
                    else:
                        for i in splited_salary:
                            if len(i)> 3:
                                d = i[:1]
                                j= i[-3:]
                                salary_digit = int(''.join([d,j]))
                                salary_list.append(salary_digit)
                    salary_list.append(splited_salary[-1])
                    salary_dict['salary'] = salary_list
                    salary_list = []
                else:
                    salary_dict['salary'] = "wasn't announced"
#printing our dict and adding it to db if link isn't in db already
                print(salary_dict)
                db.vacancy.update_one(salary_dict)
                #main_list.append(salary_dict)
            #else:
                #print(vacancy_name)
    page_counter+=1
    params['page'] = str(page_counter)
#adding list of vacancies to json file
#with open('jobs.json', 'w', encoding='utf-8') as a:
    #json.dump(main_list, a)
#for i in main_list:
    #for j,k in i.items():
        #print(j,k)