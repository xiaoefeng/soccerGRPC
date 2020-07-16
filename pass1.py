import pandas as pd
import json
from passes import Passes

playData = pd.read_json('/home/rlf/project/1/World_Cup_Final.json')
playerID = 7936
print(playerID)
Data = Passes(playData,playerID)
num = Data.countPasses()
print(num)