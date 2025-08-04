from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    _instance = None
    _client = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self._client is None:
            self.connect()

    def connect(self):
        try:
            mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/haveli_housing')
            self._client = MongoClient(mongodb_uri)
            
            # Extract database name from URI or use default
            if '/' in mongodb_uri:
                db_name = mongodb_uri.split('/')[-1]
            else:
                db_name = 'haveli_housing'
            
            self._db = self._client[db_name]
            
            # Test connection
            self._client.admin.command('ping')
            print(f"Successfully connected to MongoDB database: {db_name}")
            
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise

    def get_db(self):
        if self._db is None:
            self.connect()
        return self._db

    def close(self):
        if self._client:
            self._client.close()

# Global database instance
db_instance = Database()

def get_database():
    return db_instance.get_db()