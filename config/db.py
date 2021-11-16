from pymongo import MongoClient

client = MongoClient('mongodb://twitterapi_mongo_1:27017/')
db = client["Twitterdb"]