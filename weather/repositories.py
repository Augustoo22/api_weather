import pymongo 
from pymongo.errors import ConnectionFailure
from django.conf import settings
from .exceptions import WeatherExceptions

class WheaterRepository:

    collection = ''

    def __init__(self) -> None:
        self.collection  = collectionName
    
    def getConnection(self):
        try:
            client = pymongo.MongoClient(
                getattr(settings, "MONGO_CONNECTION_STRING")
            )
        except ConnectionFailure as e :
            raise WeatherExceptions(f"Error connecting to database: {e}")
        
        connection = client[
            getattr(settings, "MONGO_DATABASE_NAME")]
        return connection
    
    def getCollection(self):
        conn = self.getConnection()
        collection = conn[self.collection]
        return collection
    
    def getAll(self):
        document = self.getCollection().find({})
        return document

    def insert(self, document):
        self.getCollection().insert_one(document)
    
    def deleteAll(self):
        self.getCollection().delete_many({})
