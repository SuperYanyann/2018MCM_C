# -*- coding: UTF-8 -*-
import numpy
import xlrd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# get the dataset
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData.xlsx')
sheet1 = data.sheet_by_index(0)
nrows = sheet1.nrows 
ncols = sheet1.ncols

#get the num
# stateNum is the num of the stateNum
# MSNNum is the num of the stateNum
def getPhoto(stateNum,MSNNum):
    x = (MSNNum-1)*200 + (stateNum-1)*50 +2
    y = (MSNNum-1)*200 + (stateNum-1)*50 +51
    print (x,y)

    # get the data
    xcord1 =range(1,50)
    ycord1 = []
    for i in range(x,y):
        ycord1.append(sheet1.cell(i,3).value)


    #plt.plot(xcord1,ycord1,'bo-')
    plt.plot(xcord1, ycord1, marker='.', mec='r', mfc='w',label=u'test1')

if __name__ =="__main__":
    plt.subplot(221)
    getPhoto(1,77)
    plt.subplot(222)
    getPhoto(2,77)
    plt.subplot(223)
    getPhoto(3,77)
    plt.subplot(224)
    getPhoto(4,7)

    plt.show()
