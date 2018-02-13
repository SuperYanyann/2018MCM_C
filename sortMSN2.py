# -*- coding: UTF-8 -*-
import numpy
import xlrd
import matplotlib
import matplotlib.pyplot as plt

# get the data of MSN
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData.xlsx')
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
nrows = sheet1.nrows  
ncols = sheet1.ncols

# get the name of State
def getNameOfState(Num):
    if Num == 1:
        return sheet1.cell(1,1).value
    elif Num == 2:
        return sheet1.cell(51,1).value
    elif Num == 3:
        return sheet1.cell(152,1).value
    elif Num == 4:
        return sheet1.cell(101,1).value

# get the kindName of the MSN
def getkindName(kindNum):
    if kindNum == 1:
        return sheet2.cell(1,2).value
    elif kindNum == 2:
        return sheet2.cell(2,2).value
    else:
        return sheet2.cell(3,2).value

# get the dataset of the certain MSNNum
def getDataArr(stateNum,MSNNum):
    MSNName = sheet2.cell(MSNNum,0).value
    stateName = getNameOfState(stateNum)
    #print stateName
    oriX = 0
    oriY = []
    for i in range(1,105744):
        if sheet1.cell(i,0).value == MSNName and sheet1.cell(i,1).value == stateName:
            oriX = oriX + 1
            oriY.append(sheet1.cell(i,3).value)
    return oriY


# sort the MSN,the num is the kindNum of MSN
#retern is the ArrNum Of the same kind
def getkindArrNum(kindNum):
    kindName = getkindName(kindNum)
    kindArr = []
    kindNum = 0
    for i in range(1,605):
        kindNum = kindNum + 1
        if sheet2.cell(i,2).value == kindName:
            kindArr.append(kindNum)
    return kindArr

# get the kindArrData
#return is the data Arr of the certain kindNum
def getkindArrData(kindNum,stateNum):
    kindArr = getkindArrNum(kindNum)
    kindArrData = []
    kindArrSize = len(kindArr)
    for i in range(0,kindArrSize-1):
        kindData = getDataArr(stateNum,kindArr[i])
        kindArrData.append(kindData)
    return kindArrData


# int the last fun we get the len of each Arr is defferent,e.g 0 30 40 50
#for PCA,we should screen the Arr in the same len
def screenKindArrData(kindNum,stateNum):
    kindArr = getkindArrNum(kindNum)
    kindArrData = []
    scrKindArrData = []
    kindArrSize = len(kindArr)
    for i in range(0,kindArrSize-1):
        kindData = getDataArr(stateNum,kindArr[i])
        kindArrData.append(kindData)
    lenkindArr = len(kindArrData)
    for i in range(0,lenkindArr):
        if len(kindArrData[i]) == 50:
            scrKindArrData.append(kindArrData[i])
    return scrKindArrData



# enter the main
if __name__ =="__main__":
    kindArrData1 = screenKindArrData(1,1)
    lenkindArr1 = len(kindArrData1)
    print lenkindArr1
