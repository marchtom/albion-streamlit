import os

from pymongo import MongoClient

MONGO_URI = os.environ['MONGO_URI']

client = MongoClient(MONGO_URI)
mongo_db = client['default']
