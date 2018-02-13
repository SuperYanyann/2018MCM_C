# -*- coding: UTF-8 -*-
import numpy
import xlrd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# get the dataset
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData3.xlsx')
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
sheet3 = data.sheet_by_index(7)
nrows = sheet1.nrows  
ncols = sheet1.ncols
source = '/home/yanwang/文档/competition/2018美赛/photo/data1/'

# get the data used to photo
# stateNum is the num of state{1:AZ,2:CA,3:NM,4:TX}
# indicatorNum is {1:G,2:I,3:P,4:C}
def getDataNeed(stateNum,indicatorNum):
    stateNum = stateNum - 1
    indicatorNum = indicatorNum - 1

    beginNum = 1 + stateNum*50
    endNum = beginNum + 49

    data1S1I = []
    for i in range(beginNum,endNum):
        data1S1I.append(sheet3.cell(i,indicatorNum).value)
    return data1S1I

def getPhoto1I(indicatorNum):
    indicatorNum = indicatorNum - 1
    indicatorName = sheet3.cell(0,indicatorNum).value
    Y_Sum = []

    for i in range(1,5):
        Y_Sum.append(getDataNeed(i,indicatorNum))

    xcord1 =range(1960,2009)
    l1 = plt.plot(xcord1, Y_Sum[0] , marker='.', mec='r', mfc='w',label=u'AZ')
    l2 = plt.plot(xcord1, Y_Sum[1] , marker='.', mec='b', mfc='w',label=u'CA')
    l3 = plt.plot(xcord1, Y_Sum[2] , marker='.', mec='g', mfc='w',label=u'TX')
    l4 = plt.plot(xcord1, Y_Sum[3] , marker='.', mec='y', mfc='w',label=u'NM')
    plt.xlabel('time/year')
    plt.ylabel('weight '+indicatorName)
    plt.legend(loc='upper left')
    #plt.legend(handles = [l1, l2, l3, l4,], labels = ['AZ', 'CA','TX','NM'], loc = 'best')
    #plt.title('resule:('+str(MSNNum)+')')
    plt.title(indicatorName)


if __name__ =="__main__":
    plt.subplot(221)
    getPhoto1I(1)
    plt.subplot(222)
    getPhoto1I(2)
    plt.subplot(223)
    getPhoto1I(3)
    plt.subplot(224)
    getPhoto1I(4)

    plt.show()
