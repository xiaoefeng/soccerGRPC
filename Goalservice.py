#coding:utf-8
import time
import grpc
import pandas as pd
import json
import Goal_pb2 as pb2
import Goal_pb2_grpc as pb2_grpc
from concurrent import futures
from goal1 import Goal1
from passes import Passes

class Goal(pb2_grpc.GoalServicer):#所有的服务器部署都是pb2_grpc
    def GoalLys(self,request,context):
        playData = pd.read_json('/home/rlf/project/1/World_Cup_Final.json')
        playerID = request.playerID
        Data = Goal1(playData,playerID)
        num = Data.count()
        result="进球数是{d}".format(d=num)
        return pb2.GoalRes(result=result)#所有的proto的res和req都是在pb2当中
       

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