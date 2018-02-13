# -*- coding: UTF-8 -*-
import numpy
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

# !!!data needed
# the firsr is the aimArr,and others is the inputsArr
#you can get the liner model use inputs to get the aimArr
# if you want to get other aimoutput,you just change the arr 'dataMSNNum' is OK
# Attention: 'dataMSNNum' is the real Arr to count
dataMSNNum1 = [77,44,39,48,54,72]  # coal
dataMSNNum2 = [428,400,405,410,416,423] #petroleum
dataMSNNum4 = [360,328,330,334,338,355] #natual
dataMSNNum = [428,190,563] #natual

# data of TPOPP and GDPRV in 2025,2050
predictedTPOPP = numpy.mat([[9706.38,16260.11],
                 [45716.811,59352.42],
                 [2531.75,3439.29],
                 [31497.46,45390.81]])
predictedGDPRV = numpy.mat([[754276.76,1478646.74],
                  [4716646.0,8649939.39],
                  [182242.21,329062.844],
                  [2994993.27,5678289.72]])


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

# get the data of 6 certain MSNs' dataset
# the test number is 77,39,44,48,54,72
# the 77 is the aim
def getRegData(stateNum):
    regData = []
    for i in range(0,3):
        MSNNum = dataMSNNum[i]
        MSNName = sheet2.cell(MSNNum,0).value
        stateName = getNameOfState(stateNum)

        oriX = 0
        oriY = []
        for i in range(1,105744):
            if sheet1.cell(i,0).value == MSNName and sheet1.cell(i,1).value == stateName and sheet1.cell(i,2).value > 1969 and sheet1.cell(i,2).value <2006:
                oriX = oriX + 1
                oriY.append(sheet1.cell(i,3).value)
        regData.append(oriY)

    return regData

# get the data use to test
def getTestData(stateNum):
    regData = []
    for i in range(0,3):
        MSNNum = dataMSNNum[i]
        MSNName = sheet2.cell(MSNNum,0).value
        stateName = getNameOfState(stateNum)

        oriX = 0
        oriY = []
        for i in range(1,105744):
            if sheet1.cell(i,0).value == MSNName and sheet1.cell(i,1).value == stateName and sheet1.cell(i,2).value > 1969:
                oriX = oriX + 1
                oriY.append(sheet1.cell(i,3).value)
        regData.append(oriY)

    return regData

# to achieve the regression
def regreAim(stateNum):
    oriData = getRegData(stateNum)
    testData = getTestData(stateNum)

    X = oriData[1:3]
    X = trans(X)
    Y = oriData[0]

    test_X = testData[1:3]
    test_X = trans(test_X)
    test_Y = testData[0]

    '''
    # ouput the original dataset for testing
    print 'X:'
    print X
    print 'Y:'
    print Y
    '''

    # define the model and train
    model = linear_model.LinearRegression()
    model.fit(X,Y)


    # get the aimCoefficients and aimIndependent
    aimCoefficients =  model.coef_
    aimIndependent = model.intercept_

    print 'aimCoefficients:'
    print aimCoefficients
    print 'aimIndependent:'
    print aimIndependent

    # get the output by the originalData
    test_x = test_X
    testPredict = model.predict(test_x)

    stateNum = int(stateNum - 1)
    print stateNum
    print predictedGDPRV
    predictedGDPRV[0,0]
    # use to get the value of 2025,2050
    data2025 = []
    data2025.append(float(predictedGDPRV[stateNum,0]))
    data2025.append(float(predictedTPOPP[stateNum,0]))

    data2050 = []
    data2050.append(float(predictedGDPRV[stateNum,1]))
    data2050.append(float(predictedTPOPP[stateNum,1]))


    predict2025 = aimCoefficients[0]*data2025[0] + aimCoefficients[1]*data2025[1] +aimIndependent
    predict2050 = aimCoefficients[0]*data2050[0] + aimCoefficients[1]*data2050[1] +aimIndependent


    print 'State is ' + str(stateNum)
    print '2025:'
    print predict2025
    print '2050:'
    print predict2050

    # get the means of difference between oriY and new Y
    comparation = (testPredict - test_Y)**2
    MSE_Y = numpy.mean(comparation)  # get the mean to detect

    # ouput the meas
    '''
    print 'ori:'
    print Y
    print 'new'
    print testPredict
    '''

    print 'MSE:'
    print MSE_Y


    # output is the original data:Y and the prodict:testPredict
    return test_Y,testPredict

# get the photo to compare to the original data
def getPhotoAimPredict(stateNum):
    ori_Y,new_Y = regreAim(stateNum)


    X = range(1970,2010)
    plt.subplot(311)
    plt.title('Original')
    l1 = plt.plot(X, ori_Y , marker='.', mec='r', mfc='w',label=u'Original')
    plt.ylabel('Billion Btu')
    plt.legend(loc='upper left')

    plt.subplot(312)
    plt.title('Predict')
    l2 = plt.plot(X, new_Y , marker='.', mec='b', mfc='w',label=u'Predict')
    plt.ylabel('Billion Btu')
    plt.legend(loc='upper left')

    plt.subplot(313)
    l1 = plt.plot(X, ori_Y , marker='.', mec='r', mfc='w',label=u'Original')
    l2 = plt.plot(X, new_Y , marker='.', mec='b', mfc='w',label=u'Predict')
    plt.xlabel('time/year')
    plt.ylabel('Billion Btu')
    plt.legend(loc='upper left')
    plt.title('Compare')


# enter the main
if __name__ =="__main__":
    for i in range(1,5):
        getPhotoAimPredict(i)
    plt.show()
