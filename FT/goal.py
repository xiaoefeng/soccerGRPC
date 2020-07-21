import pandas as pd
import json

class Goals:
    """ 统计某场比赛的某个球员进球数"""
    def __init__(self, Data, playerId):

        self.Data = Data
        self.PlayerId = playerId
        self.Shots = self.Data.loc[self.Data['subEventName'] == 'Shot']
        self.Penaltys = self.Data.loc[self.Data['subEventName'] == 'Penalty']

    def countGoal(self):  # 统计进球数  区分普通进球和点球进球   先遍历所有的进球的球员，统计某个球员的进球数
        SampleGoals = []
        Penaltys = []
        # 通过tagsId判断射门动作的结果
        for shot in self.Shots.loc[:, ['playerId', 'tags']].values:
            for tags in shot[1]:
                if tags['id'] == 101:
                    SampleGoals.append(shot[0])

                else:
                    continue

        for penalty in self.Penaltys.loc[:, ['playerId', 'tags']].values:
            for tags in penalty[1]:
                if tags['id'] == 101:
                    Penaltys.append(penalty[0])

                else:
                    continue
        #  分别统计单个球员的点球进球和普通进球
        num1 = 0
        num2 = 0
        for n in SampleGoals:
            if n == self.PlayerId:
                num1 = num1 + 1

            else:
                continue

        for n in Penaltys:
            if n == self.PlayerId:
                num2 = num2 + 1

            else:
                continue
        if num2 == 0:
            num = num1 + num2

        else:
            num = num1+num2
            num = '{0}({1})'.format(num, num2)

        return num