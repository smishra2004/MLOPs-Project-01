import os 
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME,MONGODB_URL_KEY

ca = certifi.where()

class MongoDBClinet:
    client = None
    
    def __init__(self, database_name:str = DATABASE_NAME)->None:
        try:
            if MongoDBClinet.client is None:
                mongodb_url = os.getenv(MONGODB_URL_KEY)
                if mongodb_url is None:
                    raise Exception(f"Environment variable {MONGODB_URL_KEY} is not set")
            
                MongoDBClinet.client = pymongo.MongoClient(mongodb_url,tlsCAFile=ca)
            
            self.client = MongoDBClinet.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info('MongoDB connection successful')
        
        except Exception as e:
            raise MyException(e,sys)