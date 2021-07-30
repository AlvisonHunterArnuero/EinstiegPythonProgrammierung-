import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient)
#use database named "organisation"
mydb = myclient["organisation"]

#use collection named "developers"
mycol = mydb["developers"]

#a document
developer = {"name": "Alvison Hunter", "country": "Nicaragua"}

#insert a document to the collection
x = mycol.insert_one(developer)

#list the databases
for db in myclient.list_databases():
    print(db)
