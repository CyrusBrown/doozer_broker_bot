import json
import pymongo
import os 
from dotenv import load_dotenv


load_dotenv()

PASSWORD = os.getenv("MONGOPASSWORD")
MONGOURL = f"mongodb+srv://brokerbot:{PASSWORD}@doozerbroker.twrvxcf.mongodb.net/?retryWrites=true&w=majority&appName=doozerbroker"
client = pymongo.MongoClient(MONGOURL)
db = client['doozerbroker']
users = db['users']


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

class Database:
    def __init__(self):
        self.mongo_url = MONGOURL
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client['doozerbroker']
        self.users = self.db['users']

    def update_document(
        self,
        collection: str,
        new_data: dict,
        query: dict,
    ) -> None:
        """Updates one document that matches 'query' with 'new_data', uses upsert"""
        self.db[collection].update_one(query, {"$set": new_data}, upsert=True)
    
    def find_document(
        self,
        collection: str,
        query: dict,
    ) -> dict:
        """Finds one document that matches 'query'"""
        return self.db[collection].find_one(query)
    
    def get_consilidated_field(
        self,
        collection: str,
        field: str,
        query: dict,
    ) -> list:
        """Returns a list of values of a specific field across all documents that match 'query'"""
        return [doc[field] for doc in self.db[collection].find(query)]
    