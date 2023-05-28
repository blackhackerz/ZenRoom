import pymongo
import time
import random
import secrets
ext = secrets.token_hex(10)  

timestamp = int(time.time())
random_number = random.randint(1, 10)

unique_id = timestamp-random_number

client = pymongo.MongoClient('mongodb+srv://zenroom:Si1Gly32eKOO4WM3@cluster0.nt5nnqv.mongodb.net/')
db = client['zenroom']
col = db["users"]

res = col.find({"email": "xyz@g.com"})
print(res[0]["user_id"])

