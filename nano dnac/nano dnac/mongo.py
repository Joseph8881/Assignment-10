from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://MONGO_PRIVATE_IP:27017/")
db = client["dnac_logs"]
collection = db["logs"]

def log_action(action, ip=None, status="success"):
    collection.insert_one({
        "action": action,
        "ip": ip,
        "status": status,
        "timestamp": datetime.now()
    })