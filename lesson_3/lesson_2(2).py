import json
from pprint import pprint
import pymongo
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client.vacancydb

#adding our jobs.json in MongoDB
#with open('jobs.json') as a:
    #db_json = json.load(a)
    #print(type(db_json))
    #db.vacancy.insert_many(db_json)
#print(db.list_collection_names())

#2) Function that returns your wanted salary

def money_checker(number):
    vacancy_list = []
#using $and for checking both numbers
    for i in db.vacancy.find({'$and':[{'salary':{'$gt':number}},{'salary':{'$gt':number}}]}):
        vacancy_list.append(i)
    return(vacancy_list)

money_number = int(input('type your wanted salary here: '))
check_money = money_checker(money_number)
for i in check_money:
    pprint(i)


