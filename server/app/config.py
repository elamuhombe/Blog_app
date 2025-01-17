#server/app/config.py
from pymongo import MongoClient

#MongoDB configuration
MONGO_DB_URI = "mongodb://localhost:27017"
DB_NAME = "blog"

#connect to MongoDB
client=MongoClient(MONGO_DB_URI)

#create or connect to the database
db=client[DB_NAME]