import numpy as np
import random as rd
import xlrd
import xlwt
from xlrd import open_workbook
from fractions import Fraction


#读取数据 存数据 到data数组中
wb = open_workbook(r'G:\CPI.xls')
tb = wb.sheets()[0]
data = []

for r in range(tb.nrows):
    val = []
    for c in range(tb.ncols):
        val.append(tb.cell_value(r,c))
    data.append((tuple(val)))

print(data)
# print(len(data))
for i in range(1,25):
    print(data[i])

#计算频数矩阵1步
Frequencey_arry=[[0 for x in range(4)]for y in range(4)]
print(Frequencey_arry)
#range(x,y)从X开始到Y前结束
for i in range(1,25):
    if(i+1 != 25 and data[i+1][2] == 1 ):
        if(data[i][2]==1):
            Frequencey_arry[0][0] += 1
        elif(data[i][2] == 2):
            Frequencey_arry[1][0] += 1
        elif (data[i][2] == 3):
            Frequencey_arry[2][0] += 1
        elif (data[i][2] == 4):
            Frequencey_arry[3][0] += 1

    elif(i+1!=25 and data[i+1][2] == 2 ):
        if (data[i][2] == 1):
            Frequencey_arry[0][1] += 1
        elif (data[i][2] == 2):
            Frequencey_arry[1][1] += 1
        elif (data[i][2] == 3):
            Frequencey_arry[2][1] += 1
        elif (data[i][2] == 4):
            Frequencey_arry[3][1] += 1

    elif (i+1!=25 and data[i+1][2] == 3 ):
        if (data[i][2] == 1):
            Frequencey_arry[0][2] += 1
        elif (data[i][2] == 2):
            Frequencey_arry[1][2] += 1
        elif (data[i][2] == 3):
            Frequencey_arry[2][2] += 1
        elif (data[i][2] == 4):
            Frequencey_arry[3][2] += 1

    elif (i+1!=25 and data[i+1][2] == 4 ):
        if (data[i][2] == 1):
            Frequencey_arry[0][3] += 1
        elif (data[i][2] == 2):
            Frequencey_arry[1][3] += 1
        elif (data[i][2] == 3):
            Frequencey_arry[2][3] += 1
        elif (data[i][2] == 4):
            Frequencey_arry[3][3] += 1
print("\t")
#打印频数矩阵
for i in range(len(Frequencey_arry)):
    for j in range(len(Frequencey_arry[i])):
        print(Frequencey_arry[i][j],end='\t')
    print()
print("\t")

#转移概率矩阵
FrequenceyPer_arry=[[0 for x in range(4)]for y in range(4)]
sum = 0
for i in range(len(Frequencey_arry)):
    for s in range(len(Frequencey_arry[i])):
        sum += Frequencey_arry[i][s]
    for j in range(len(Frequencey_arry[i])):

        if(Frequencey_arry[i][j] == 0):
            FrequenceyPer_arry[i][j] = 0
        else:
            b = Fraction(Frequencey_arry[i][j],sum)
            FrequenceyPer_arry[i][j] = b

        print(FrequenceyPer_arry[i][j],end='\t')
    sum = 0
    print()

#