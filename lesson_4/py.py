import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.yanewsdb

#print(client.list_database_names())
news = db.yanewsdb.find()
for i in news:
    print(i)