# -*- coding: UTF-8 -*-
import numpy as np
import xlrd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#learn from https://www.cnblogs.com/zhizhan/p/5664214.html

# get the dataset
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData2.xlsx')
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
sheet3 = data.sheet_by_index(4)
nrows = sheet1.nrows  
ncols = sheet1.ncols
source = '/home/yanwang/文档/competition/2018美赛/photo/data1/'

# the fun2 use to fit
def func(x,a,b):
    return a*np.exp(b/x)

# the fun use to fit
def func2(x,a,b,k):
    return k/(1 + b*np.exp(-a*x))

'''
# get the data of (CA,GETCB) from 1960 to 2009
def getDataNeedFit():
    dataNeedFit = []
    for i in range(51,100):
        dataNeedFit.append(sheet3.cell(i,4).value)
    return dataNeedFit
'''

# get the data of (stateNum,MSNNum) from 1960 to 2009
# stateNum is the num of state {0:AZ,1:CA,2:NM,3:TX}
# MSNNum is the num of MSN {1:NGTCB,2:NUETN,3:WYTCB,4:HTTCB,5:GETCB,6:BMTCB}
# sheet3 is a sheet be changed by myself
def getDataNeedFit(stateNum,MSNNum):
    MSNNum = MSNNum - 1
    beginNum = 1 + stateNum*50
    endNum = beginNum + 49
    dataNeedFit = []
    for i in range(beginNum,endNum):
        dataNeedFit.append(sheet3.cell(i,MSNNum).value)
    return dataNeedFit

# enter the main
if __name__ =="__main__":
   x = np.arange(1, 50, 1)
   y = getDataNeedFit(3,3)
   y = np.array(y)

   popt, pcov = curve_fit(func, x, y)
   a=popt[0]
   b=popt[1]
   #k=popt[2]

   print popt

   yvals=func(x,a,b)
   plot1=plt.plot(x, y, '*',label='original values')
   plot2=plt.plot(x, yvals, 'r',label='fit values')
   plt.xlabel('x axis')
   plt.ylabel('y axis')
   plt.legend(loc=4)
   plt.title('GETCB')
   plt.show()
