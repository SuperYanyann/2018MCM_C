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

    if type == 1:
            yaim = (ymax - ymin)*(oriData - xmin)/(xmax - xmin)+ymin
    else:
            yaim = (ymax - ymin)*(xmax - oriData)/(xmax - xmin)+ymin

    return yaim

# to get the score of samples and the weight of the target
# for the data numSample is the num of sample
# numTarget is the num of target
def getEntropy(oriData,types):
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

    # data of part1 C
    inData = [[254099.0,-0.02927,6587.653,6.29971,1454313.0,527243.0,2662.45,19.6648,0.24,0.31,0.45],
              [1884452.0,-0.02178,36887.615,4.60908,8005515.0,1863792.0,2838.67,18.4053,0.01,0.51,0.48],
              [74388.0,-0.0480,2007.315,9.7042,670095.0,155425.0,3215.38,17.179,0.37,0.30,0.33],
              [1141287.0,-0.04864,24770.651,10.5936,11297410.59,2479198.0,4651.35,15.3793,0.31,0.31,0.20]]
    #use to get the data of sensitivity analysis
    coal = [0.24,0.01,0.37,0.31]
    petroleum = [0.31,0.51,0.30,0.31]
    renewable = [0.45,0.48,0.33,0.20]

    '''
    print 'coal'
    print np.mat(coal)
    print 'petroleum'
    print 0.9*np.mat(petroleum)
    print 'renewable'
    print np.mat(renewable)+0.1*np.mat(petroleum)
    '''

    #sensitivity analysis 1
    inData1 = [[254099.0,-0.02927,6587.653,6.29971,1454313.0,527243.0,2662.45,19.6648,0.216,0.334,0.45],
              [1884452.0,-0.02178,36887.615,4.60908,8005515.0,1863792.0,2838.67,18.4053,0.009,0.511,0.48],
              [74388.0,-0.0480,2007.315,9.7042,670095.0,155425.0,3215.38,17.179,0.333,0.37,0.33],
              [1141287.0,-0.04864,24770.651,10.5936,11297410.59,2479198.0,4651.35,15.3793,0.279,0.341,0.20]]

    #sensitivity analysis 2
    inData2 = [[254099.0,-0.02927,6587.653,6.29971,1454313.0,527243.0,2662.45,19.6648,0.271,0.279,0.45],
              [1884452.0,-0.02178,36887.615,4.60908,8005515.0,1863792.0,2838.67,18.4053,0.061,0.459,0.48],
              [74388.0,-0.0480,2007.315,9.7042,670095.0,155425.0,3215.38,17.179,0.4,0.27,0.33],
              [1141287.0,-0.04864,24770.651,10.5936,11297410.59,2479198.0,4651.35,15.3793,0.341,0.279,0.20]]

    #sensitivity analysis 3
    inData3 = [[254099.0,-0.02927,6587.653,6.29971,1454313.0,527243.0,2662.45,19.6648,0.216,0.31,0.474],
              [1884452.0,-0.02178,36887.615,4.60908,8005515.0,1863792.0,2838.67,18.4053,0.009,0.51,0.481],
              [74388.0,-0.0480,2007.315,9.7042,670095.0,155425.0,3215.38,17.179,0.333,0.30,0.367],
              [1141287.0,-0.04864,24770.651,10.5936,11297410.59,2479198.0,4651.35,15.3793,0.279,0.31,0.231]]

    #sensitivity analysis 4
    inData4 = [[254099.0,-0.02927,6587.653,6.29971,1454313.0,527243.0,2662.45,19.6648,0.24,0.279,0.481],
              [1884452.0,-0.02178,36887.615,4.60908,8005515.0,1863792.0,2838.67,18.4053,0.01,0.459,0.531],
              [74388.0,-0.0480,2007.315,9.7042,670095.0,155425.0,3215.38,17.179,0.37,0.27,0.36],
              [1141287.0,-0.04864,24770.651,10.5936,11297410.59,2479198.0,4651.35,15.3793,0.31,0.279,0.231]]


    inTypes = [1,1,1,-1,-1,-1,-1,-1,-1,-1,1]
    tempS,tempW = getEntropy(inData4,inTypes)
    print 'tempS:'
    print tempS
    print 'tempW:'
    print tempW
