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
# 1-6 is need to get the proportion
MSNNumArr = [360,382,207,197,27,77] # the Nums need to count the proportion
MSNNumArrCouSum = [77,428,487,360,382] # the total of Nums

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

# get the Arr of certain MSNs
def getArrMSNName(MSNNumList):
    lenMSNlist = len(MSNNumList)
    MSNNameArr = []
    for i in range(0,lenMSNlist):
        MSNNameArr.append(sheet1.cell(MSNNumList[i],0).value)
    return MSNNameArr

# get the Name of years
# because the coded format of excel is special
def getNameOfYear(numYear):
    rowNum = numYear - 1959
    nameYear = sheet1.cell(rowNum,2).value
    return nameYear

# get sum of 5 MSNs
# the ouput is the sum of one year and one dtate
def getEnergySum1S1Y(stateNum,yearNum):
    yearName = getNameOfYear(yearNum)
    stateName = getNameOfState(stateNum)
    MSNNameArr = getArrMSNName(MSNNumArrCouSum)

    print MSNNameArr

    energy1S1Y = []
    oriX = 0
    for i in range(1,105744):
        if sheet1.cell(i,0).value in MSNNameArr and sheet1.cell(i,1).value == stateName and sheet1.cell(i,2).value == yearName:
            oriX = oriX + 1
            '''
            print sheet1.cell(i,3).value
            '''
            energy1S1Y.append(sheet1.cell(i,3).value)
    energySum1S1Y = sum(energy1S1Y)
    '''
    print 'partSum'
    print energySum1S1Y
    '''

    return energySum1S1Y

# get sum of MSNs
# the ouput is all of the sums,the ouput is 1*50
# for all years but one state
def getEnergySum1S(stateNum):
    energySum1S = []
    for i in range(1960,2010):
        energySum1S1Y = getEnergySum1S1Y(stateNum,i)
        energySum1S.append(energySum1S1Y)
    return energySum1S


# get sum of MSNs
# the ouput is all of the sums,the ouput is 4*50
# for all years and all state
def getEnergySumAll():
    energySumAll = []
    for i in range(1,5):
        energySum1S = getEnergySum1S(i)
        energySumAll.append(energySum1S)
    return energySumAll

# get the data of one state and one MSN
# from year 1960 to 2009,the len is 50
def getData1S1M(stateNum,MSNNum):
    MSNName = sheet2.cell(MSNNum,0).value
    stateName = getNameOfState(stateNum)

    oriX = 0
    oriY = []
    for i in range(1,105744):
        if sheet1.cell(i,0).value == MSNName and sheet1.cell(i,1).value == stateName:
            oriX = oriX + 1
            oriY.append(sheet1.cell(i,3).value)
    return oriY

# get the data of one MSN but four states
# the shape of output is 4*50
def getData1M(MSNNum):
    data1M = []

    for i in range(1,5):
        data1S1M = getData1S1M(i,MSNNum)
        data1M.append(data1S1M)
    return data1M


# count the proportion of one MSN
# the shape of output is 4*50
def getProportion1M(MSNNum):
    energySumAll = getEnergySumAll()
    data1M = getData1M(MSNNum)

    print 'energySumAll:'
    print energySumAll
    print 'data1M:'
    print data1M

    '''
    if np.shape(energySumAll) == np.shape(data1M):
        proportion1M = np.mat(data1M)/np.mat(energySumAll)
    else:
        print 'len of data1M and energySumAll is diffrernt'
    '''
    proportion1M = np.mat(data1M)/np.mat(energySumAll)
    proportion1M = proportion1M.tolist()
    return proportion1M

# count the proportion of all 6 MSN
# the shape of output is 6*4*50
def getProportionAll():
    lenOfMSN = len(MSNNumArr)
    proportionAll = []
    for i in range(0,lenOfMSN):
        proportion1M = getProportion1M(MSNNumArr[i])
        proportionAll.append(proportion1M)
    return proportionAll


# enter the main
if __name__ =="__main__":
    proportionAll = getProportionAll()
    print 'proportionAll[0]'
    print proportionAll[0]
