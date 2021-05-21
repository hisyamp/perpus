from pymongo import MongoClient
from pymongo.message import query
from bson.objectid import ObjectId

class database:
    def __init__(self):
        try:
            self.nosql_db = MongoClient()
            self.db = self.nosql_db.perpustakaan
            self.mongo_col = self.db.books
            print("database connected")
        except Exception as e:
            print(e)
    
    def showBooks(self):
        result = self.mongo_col.find()
        return result
    
    def showBookById(self, key):
        id = ObjectId(key)
        query = ({"_id" : id})
        result = self.mongo_col.find(query)
        return result
    
    def searchBookByName(self, key):
        query = {"nama" : {"$regex": key, "$options": "i"}}
        result = self.mongo_col.find(query)
        return result
    
    def insertBook(self,document):
        self.mongo_col.insert_one(document)
    
    def updateBookById(self, key):
        id = {"_id" : ObjectId(key)}
        query = {"$set":{"nama":"Visakhapatnam"}}
        self.mongo_col.update(id,query)
        
    
    def deleteBookById(self, key):
        id = {"_id" : ObjectId(key)}
        self.mongo_col.remove(id)

# kelas = database()
# kelas.updateBookById('60a36da97a229313d8ef20f4')