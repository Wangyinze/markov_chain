import numpy as np
import random as rm

#定义状态及其概率，也就是转移矩阵。
#状态空间
states = ["Sleep","Icecream","Run"]

#可能的事件序列
transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

#概率矩阵（转移矩阵）
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

#实现了可以预测状态的马尔可夫模型的函数
def activity_forecast(days):
    #选择初始状态
    activityToday = "Sleep"
    print("Start state: " + activityToday)
    #应该记录选择的状态序列。这里现在只有初始状态
    activityList = [activityToday]
    i = 0
    #计算activityList的概率
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace = True,p = transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday ="Run"
                activityList.append("Run")
            else:
                prob = prob * 0.2
                activityToday = "Icecream"
                activityList.append("Icecream")

        elif activityToday == "Run":
            change = np.random.choice(transitionName)
            if change =="RR":
                prob = prob *0.5
                activityList.append("Run")
                pass
            elif change =="RS":
                prob = prob *0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.3
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace = True,p = transitionMatrix[2])
            if change == "II":
                prob = prob*0.1
                activityList.append("Icecream")
                pass
            elif change =="IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.7
                activityToday = "Run"
                activityList.append("Run")