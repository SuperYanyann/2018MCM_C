# -*- coding: UTF-8 -*-
import numpy
import xlrd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import csv

def writeToTxt(list_name,file_path):
    try:
        fp = open(file_path,"rb+")
        for item in list_name:
            fp.write(str(item)+"\n")
        fp.close()
    except IOError:
        print("fail to open file")

# get the dataset
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData.xlsx')
sheet1 = data.sheet_by_index(0)
nrows = sheet1.nrows
ncols = sheet1.ncols

# get the data
#1
#plt.subplot(221)
xcord1 =range(1,50)
ycord1 = []
for i in range(1482,1531):
    ycord1.append(sheet1.cell(i,3).value)

xcord1_2 =range(1,50)
ycord1_2 = []
for i in range(1842,1891):
    ycord1_2.append(sheet1.cell(i,3).value)

writeToTxt(ycord1_2,'/home/yanwang/文档/competition/2018美赛/数据/test.txt')
writeToTxt(xcord1_2,'/home/yanwang/文档/competition/2018美赛/数据/test.txt')


plt.plot(xcord1,ycord1,'bo-')
plt.plot(xcord1, ycord1, marker='o', mec='r', mfc='w',label=u'test1')
plt.plot(xcord1_2,ycord1_2,'ro-')
plt.plot(xcord1_2, ycord1_2, marker='o', mec='r', mfc='w',label=u'test2')


plt.show()
