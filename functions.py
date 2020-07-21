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

class Passes:
    def __init__(self, Data, playerId):
        self.Data = Data
        self.PlayerId = playerId
        self.Passes = self.Data.loc[self.Data['eventName'] == 'Pass']

    def countPasses(self):
        df = self.Passes.loc[self.Passes['playerId'] == self.PlayerId]
        num = len(df)
        return num

    def countAccurate(self):
        Counts = []
        for i in self.Passes.loc[:, ['playerId', 'tags']].values:
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

class Keypasses:
    def __init__(self, Data, playerId):
        self.Data = Data
        self.PlayerId = playerId
        self.Passes = self.Data.loc[self.Data['eventName'] == 'Pass']

    def countKey(self):
        Counts = []
        for i in self.Passes.loc[:, ['playerId', 'tags']].values:
            for tags in i[1]:
                if tags['id'] == 302:
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

class Smartpass:
    def __init__(self, Data, playerId):
        self.Data = Data
        self.PlayerId = playerId
        self.SmartPasses = self.Data.loc[self.Data['subEventName'] == 'smartPass']

    def countsmart(self):
        df = self.SmartPasses.loc[self.SmartPasses['playerId'] == self.PlayerId]
        num = len(df)
        return num

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

class Foul:
    def __init__(self, Data, playerId):
        self.Data = Data
        self.PlayerId = playerId
        self.Fouls = self.Data.loc[self.Data['eventName'] == 'Foul']

    def countT(self):
        df = self.Fouls.loc[self.Fouls['playerId'] == self.PlayerId]
        num = len(df)
        return num

    def countYellowcard(self):
        Counts = []
        for i in self.Fouls.loc[:, ['playerId', 'tags']].values:
            for tags in i[1]:
                if tags['id'] == 1702:
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

    def countRedcards(self):
        Counts = []
        for i in self.Fouls.loc[:, ['playerId', 'tags']].values:
            for tags in i[1]:
                if tags['id'] == 1701:
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