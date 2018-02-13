# -*- coding: UTF-8 -*-
import numpy as np
import xlrd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model

# get the dataset
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData.xlsx')
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
nrows = sheet1.nrows  
ncols = sheet1.ncols
source = '/home/yanwang/文档/competition/2018美赛/photo/data1/'

# !!! the Arr is important in the def
# the Arr is the MSNNum of 8 needed MSNs
MSNNumArr = [360,382,605,207,197,27,77,428]

# transposition
def trans(m):
    a = [[] for i in m[0]]
    for i in m:
        for j in range(len(i)):
            a[j].append(i[j])
    return a

# change mat to lise with one row
def mat2list(tempMat):
    tempMat = tempMat.tolist()
    tempMat = sum(tempMat,[])
    return tempMat

# get the Name of State
def getNameOfState(Num):
    if Num == 1:
        return sheet1.cell(1,1).value
    elif Num == 2:
        return sheet1.cell(51,1).value
    elif Num == 3:
        return sheet1.cell(152,1).value
    elif Num == 4:
        return sheet1.cell(101,1).value

# get the Arr of four stats
def getArrStateName():
    stateNameArr = []
    for i in range(1,5):
        stateNameArr.append(getNameOfState(i))
    return stateNameArr

# get the Name of years
# because the coded format of excel is special
def getNameOfYear(numYear):
    rowNum = numYear - 1959
    nameYear = sheet1.cell(rowNum,2).value
    return nameYear

# the first step to get the dataset in right style
# just get the dataset of certain one  MSN and one year
# the Arr's standard is 1*4
def getOneMSNDataSty(MSNNum,yearNum):
    MSNName = sheet2.cell(MSNNum,0).value
    yearName = getNameOfYear(yearNum)
    stateNameArr = getArrStateName()
    aimData = []

    oriX = 0
    oriY = []
    for i in range(1,105744):
        if sheet1.cell(i,0).value == MSNName and sheet1.cell(i,2).value == yearName and sheet1.cell(i,1).value == stateNameArr[0] :
            oriX = oriX + 1
            oriY.append(sheet1.cell(i,3).value)
        elif sheet1.cell(i,0).value == MSNName and sheet1.cell(i,2).value == yearName and sheet1.cell(i,1).value == stateNameArr[1] :
            oriX = oriX + 1
            oriY.append(sheet1.cell(i,3).value)
        elif sheet1.cell(i,0).value == MSNName and sheet1.cell(i,2).value == yearName and sheet1.cell(i,1).value == stateNameArr[2] :
            oriX = oriX + 1
            oriY.append(sheet1.cell(i,3).value)
        elif sheet1.cell(i,0).value == MSNName and sheet1.cell(i,2).value == yearName and sheet1.cell(i,1).value == stateNameArr[3] :
            oriX = oriX + 1
            oriY.append(sheet1.cell(i,3).value)
    return oriY

# the second step to get the dataset in right style
# get the dataset of certain 8 MSNs in one year
# the Arr's standard is 4*8
def getAllMSNDataSty(yearNum):
    lenOfMSN = len(MSNNumArr)
    oriYOneMSN = []

    for i in range(0,lenOfMSN):
        oneMSNData = getOneMSNDataSty(MSNNumArr[i],yearNum)
        oriYOneMSN.append(oneMSNData)

    oriYOneMSN = trans(oriYOneMSN)
    return oriYOneMSN



# normalize the data
# if type == 1 the diection is positive
# else the dieection is nagetive
# for the data numSample is the num of sample
# numTarget is the num of target
def normalize(oriData,type,ymin,ymax):

    lenOfData = len(oriData)
    xmax = max(oriData)
    xmin = min(oriData)
    oriData = np.mat(oriData)

    betweenMaxMIn = xmax-xmin
    if betweenMaxMIn == 0:
        betweenMaxMIn = 0.001

    if type == 1:
            yaim = (ymax - ymin)*(oriData - xmin)/betweenMaxMIn+ymin
    else:
            yaim = (ymax - ymin)*(xmax - oriData)/betweenMaxMIn+ymin

    return yaim

# to get the score of samples and the weight of the target
# for the data numSample is the num of sample
# numTarget is the num of target
def getWeightByEntropy(oriData,types):
    numSample,numTarget = np.shape(oriData)
    proportion = np.zeros((numSample,numTarget))

    aimEntropy = np.zeros(numTarget)
    aimEntropy = aimEntropy.tolist()

    oriData = np.mat(oriData)
    x = np.zeros((numSample,numTarget))

    # ormalize the data
    for i in range(0,numTarget):
       TData = oriData[:,i].T
       TData = mat2list(TData)
       x[:,i] = normalize(TData,types[i],0.002,0.996)

    # get the proportion[i,j],i is the num of the sample
    # j is the num of the target
    for i in range(0,numSample):
        for j in range(0,numTarget):
            proportion[i,j] = x[i,j]/sum(x[:,j])

    # get the entropy of each target
    logSample = np.log(numSample)
    logSample = 1/logSample
    for i in range(0,numTarget):
        tempData1 = np.log(proportion[:,i])
        tempData2 = np.multiply(proportion[:,i],tempData1)
        aimEntropy[i] = -logSample * sum(tempData2)

    # get the redundancy of each target
    b = np.ones((1,numTarget))
    b = mat2list(b)
    redundancy = np.mat(b) - np.mat(aimEntropy)
    redundancy = redundancy.tolist()
    redundancy = sum(redundancy,[])

    # get the weight of the targets and the score of the samples
    aimWeight = np.mat(redundancy)/sum(redundancy)
    proportion = trans(proportion)
    aimScore =  100 * np.dot(aimWeight,proportion)

    # change the output from mat to list
    aimScore = mat2list(aimScore)
    aimWeight = mat2list(aimWeight)

    return aimScore,aimWeight

# enter the main
if __name__ =="__main__":
    MSNStyle = [1,1,1,1,1,1,-1,-1]
    testData = getAllMSNDataSty(1960)
    tempScore,tempWeight = getWeightByEntropy(testData,MSNStyle)

    print 'time is' + '1960'
    print 'tempScore:'
    print tempScore
    print 'tempWeight:'
    print tempWeight
