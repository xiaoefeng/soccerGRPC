import pandas as pd
import json

class Smartpass:
    def __init__(self, Data, playerId):
        self.Data = Data
        self.PlayerId = playerId
        self.SmartPasses = self.Data.loc[self.Data['subEventName'] == 'smartPass']

    def countsmart(self):
        df = self.SmartPasses.loc[self.SmartPasses['playerId'] == self.PlayerId]
        num = len(df)
        return num