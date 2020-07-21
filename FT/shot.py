import pandas as pd
import json

class Shot:
    def __init__(self, Data, playerId):
        self.Data = Data
        self.PlayerId = playerId
        self.Shots = self.Data.loc[self.Data['eventName'] == 'Shot']

    def countShots(self):
        df = self.Shots.loc[self.Shots['playerId'] == self.PlayerId]
        num = len(df)
        return num

    def countShotsStraight(self):
        Counts = []
        for i in self.Shots.loc[:, ['playerId', 'tags']].values:
            for tags in i[1]:
                if tags['id'] == 1801:
                    Counts.append(i[0])

                else:
                    continue
        num1 = 0
        for n in Counts:
            if n == self.PlayerId:
                num1 = num1 + 1
            else:
                continue
        num = num1
        return num
