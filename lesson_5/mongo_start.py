import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.chromienews
#db.chromienews.delete_many({})
print(client.list_database_names())
news = db.chromienews.find()
for i in news:
    print(i)

