import pandas as pd
import json

class Assist:
    def __init__(self, Data, playerId):
        self.Data = Data
        self.PlayerId = playerId
        self.Passes = self.Data.loc[self.Data['eventName'] == 'Pass']

    def countAssist(self):
        Counts = []
        for i in self.Passes.loc[:, ['playerId', 'tags']].values:
            for tags in i[1]:
                if tags['id'] == 301:
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