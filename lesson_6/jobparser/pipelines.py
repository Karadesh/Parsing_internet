# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancies1507


    def process_item(self, item, spider):
        # item['salary'] = self.process_salary(item['salary'])
        item['salary'] = self.salary_corrector(item['salary'])

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item

    def salary_corrector(vacancy_salary):
        if vacancy_salary != None:
            try:
                vacancy_salary.remove('–')
            except ValueError:
                pass
            try:
                vacancy_salary.remove('от')
            except ValueError:
                pass
            try:
                vacancy_salary.remove('до')
            except ValueError: 
                pass
            try:
                vacancy_salary.remove('на руки')
            except ValueError:
                pass
            salary_list = []
#making int from strings 
            if vacancy_salary[-1] =='руб.':
                for i in vacancy_salary:
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
                for i in vacancy_salary:
                    if len(i)> 3:
                        d = i[:1]
                        j= i[-3:]
                        salary_digit = int(''.join([d,j]))
                        salary_list.append(salary_digit)
            salary_list.append(vacancy_salary[-1])
        else:
            salary_list= ["wasn't announced"]
        return salary_list
