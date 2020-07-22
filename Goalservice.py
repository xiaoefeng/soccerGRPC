#coding:utf-8
import time
import grpc
import pandas as pd
import json
import Goal_pb2 as pb2
import Goal_pb2_grpc as pb2_grpc
from concurrent import futures
from functions import Goals
from functions import Passes
from functions import Assist
from functions import Shot
from functions import Keypasses
from functions import Smartpass
from functions import Foul
class Goal(pb2_grpc.GoalServicer):#所有的服务器部署都是pb2_grpc
    def GoalLys(self,request,context):
        playData = pd.read_json('/home/rlf/project/soccerGrpc/World_Cup_Final.json')
        playerID = request.playerID
        Data1 = Goals(playData,playerID)
        num1 = Data1.countGoal()
        Data2 = Passes(playData,playerID)
        num2 = Data2.countPasses()
        num3 = Data2.countAccurate()
        Data3 = Assist(playData,playerID)
        num4 = Data3.countAssist()
        Data4 = Shot(playData,playerID)
        num5 = Data4.countShots()
        num6 = Data4.countShotsStraight()
        Data5 = Keypasses(playData,playerID)
        num7 = Data5.countKey()
        Data6 = Smartpass(playData,playerID)
        num8 = Data6.countsmart()
        Data7 = Foul(playData,playerID)
        num9 = Data7.countT()
        num10 = Data7.countYellowcard()
        num11 = Data7.countRedcards()
        # technical = {"goal":num1,"assist":num2}
        # result="goal:{a},assist:{b},pass:{c},accuratePass:{d},keyPass:{e},smartPass:{f},shot:{g},shotOnTarget:{h},fouls:{i},yellowCard:{j},redCard:{k}".format(a=num1,b=num4,c=num2,d=num3,e=num7,f=num8,g=num5,h=num6,i=num9,j=num10,k=num11)
        result="{a},{b},{c},{d},{e},{f},{g},{h},{i},{j},{k}".format(a=num1,b=num4,c=num2,d=num3,e=num7,f=num8,g=num5,h=num6,i=num9,j=num10,k=num11)
        return pb2.GoalRes(result=result)#所有的proto的res和req都是在pb2当中
        # return pb2.GoalRes(result=technical)

       

def run():
    server =grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    pb2_grpc.add_GoalServicer_to_server(Goal(),server)
    server.add_insecure_port('0.0.0.0:2000')
    print('服务器在2000端口启动')
    server.start()

    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run()