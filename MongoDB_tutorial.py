import pymongo

#Creating connections
con_string = "mongodb://localhost:27017/"
cluster = pymongo.MongoClient(con_string, connect=False)

db = cluster['testdb']
collection = db['testCollection']

#Inserting the data
data = {"_id":0,"name":"Prakhar","score":10}

collection.insert_one(data)
collection.insert_many([data,data]) #multiple insertion in one go 

#Searching the data
results = collection.find({}) # finds everything --> select * from db
results = collection.find({"name":"Prakhar"})
results = collection.find_one({"name":"Prakhar"})

for result in results:
    print(result)#Dictionary 

#Deleting 
results = collection.delete_one({}) #  deletes every data from the database
results = collection.delete_one({"_id":1})
results = collection.delete_many({"_id":1})

#Updating
results = collection.updata_one({"_id":5},{"$set":{"name":"tim"}})
results = collection.updata_many({"_id":5},{"$set":{"name":"tim"}})

#Counting
post_count = collection.count_documents({}) #count all --> select count(*) from db

#datetime insertion
from pymongo.mongo_client import MongoClient
import datetime

d = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")

with MongoClient() as mongo:
    db = mongo.get_database("test")
    db['dates'].insert({"date" : d})
