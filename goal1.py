import pandas as pd
import json
from functions import Goals
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Soccer"]
mycol = mydb["World_Cup_Final"]
data = mycol.find_one()
playerID = 7936
print(playerID)
Data = Goals(data,playerID)
num = Data.countGoal()
print(num)