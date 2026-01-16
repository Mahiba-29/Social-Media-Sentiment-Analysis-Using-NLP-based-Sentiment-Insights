import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["social_media"]
collection = db["sentiments"]

with open("data/sentiment_results.json") as f:
    data = json.load(f)

collection.insert_many(data)

print("Data stored in MongoDB")
