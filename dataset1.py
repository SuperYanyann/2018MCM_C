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

# get the data
#1
plt.subplot(221)
xcord1 =range(1,50)
ycord1 = []
for i in range(1482,1531):
    ycord1.append(sheet1.cell(i,3).value)

xcord1_2 =range(1,50)
ycord1_2 = []
for i in range(1842,1891):
    ycord1_2.append(sheet1.cell(i,3).value)

plt.plot(xcord1,ycord1,'bo-')
plt.plot(xcord1, ycord1, marker='o', mec='r', mfc='w',label=u'test1')
plt.plot(xcord1_2,ycord1_2,'ro-')
plt.plot(xcord1_2, ycord1_2, marker='o', mec='r', mfc='w',label=u'test2')

'''
# 2
plt.subplot(222)
xcord2=range(1,50)
ycord2 = []
for i in range(52,101):
    ycord2.append(sheet1.cell(i,3).value)

xcord2_2 =range(1,50)
ycord2_2 = []
for i in range(252,301):
    ycord2_2.append(sheet1.cell(i,3).value)
plt.plot(xcord2,ycord2,'bo-')
plt.plot(xcord2, ycord2, marker='o', mec='r', mfc='w',label=u'test1')
plt.plot(xcord2_2,ycord2_2,'ro-')
plt.plot(xcord2_2, ycord2_2, marker='o', mec='r', mfc='w',label=u'test2')


# 3
plt.subplot(223)
xcord3 =range(1,50)
ycord3 = []
for i in range(102,151):
    ycord3.append(sheet1.cell(i,3).value)

xcord3_2 =range(1,50)
ycord3_2 = []
for i in range(302,351):
    ycord3_2.append(sheet1.cell(i,3).value)

plt.plot(xcord3,ycord3,'bo-')
plt.plot(xcord3, ycord3, marker='o', mec='r', mfc='w',label=u'test1')
plt.plot(xcord3_2,ycord3_2,'ro-')
plt.plot(xcord3_2, ycord3_2, marker='o', mec='r', mfc='w',label=u'test2')

# 4
plt.subplot(224)
xcord4 =range(152,201)
ycord4 = []
for i in range(52,101):
    ycord4.append(sheet1.cell(i,3).value)

xcord4_2 =range(352,401)
ycord4_2 = []
for i in range(252,301):
    ycord4_2.append(sheet1.cell(i,3).value)

plt.plot(xcord4,ycord4,'bo-')
plt.plot(xcord4, ycord4, marker='o', mec='r', mfc='w',label=u'test1')
plt.plot(xcord4_2,ycord4_2,'ro-')
plt.plot(xcord4_2, ycord4_2, marker='o', mec='r', mfc='w',label=u'test2')
'''

'''
#point
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xcord,ycord,s=30,c='red',marker='s')
plt.xlabel('X1');plt.ylabel('X2');
plt.show()
'''


plt.show()
