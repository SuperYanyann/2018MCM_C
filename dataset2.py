# -*- coding: UTF-8 -*-
import numpy
import xlrd
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# get the dataset
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData2.xlsx')
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
nrows = sheet1.nrows  
ncols = sheet1.ncols
source = '/home/yanwang/文档/competition/2018美赛/photo/data1/'

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

#get the num
# stateNum is the num of the stateNum
# MSNNum is the num of the stateNum
def getPhoto(stateNum,MSNNum):
    MSNName = sheet2.cell(MSNNum,0).value
    stateName = getNameOfState(stateNum)
    #print stateName
    oriX = 0
    oriY = []
    for i in range(1,105944):
        if sheet1.cell(i,0).value == MSNName and sheet1.cell(i,1).value == stateName:
            oriX = oriX + 1
            oriY.append(sheet1.cell(i,3).value)


    xcord1 =range(1,oriX+1)
    ycord1 = oriY

    plt.plot(xcord1,ycord1,'bo-')
    plt.plot(xcord1, ycord1, marker='o', mec='r', mfc='w',label=u'test1')
    #plt.savefig("/home/yanwang/文档/competition/2018美赛/photo/data1/examples.jpg")

# get the photo of certain 4 MSN
# the MSNNum is 77 428 360 487
def getCertainPhoto4Satte(MSNNum):
    MSNName = sheet2.cell(MSNNum,0).value
    Y_Sum = []
    for i in range(1,5):
        stateName = getNameOfState(i)
        oriX = 0
        oriY = []
        for i in range(1,105945):
            if sheet1.cell(i,0).value == MSNName and sheet1.cell(i,1).value == stateName:
                oriX = oriX + 1
                oriY.append(sheet1.cell(i,3).value)
        Y_Sum.append(oriY)

    xcord1 =range(1+1959,oriX+1+1959)
    l1 = plt.plot(xcord1, Y_Sum[0] , marker='.', mec='r', mfc='w',label=u'AZ')
    l2 = plt.plot(xcord1, Y_Sum[1] , marker='.', mec='b', mfc='w',label=u'CA')
    l3 = plt.plot(xcord1, Y_Sum[2] , marker='.', mec='g', mfc='w',label=u'TX')
    l4 = plt.plot(xcord1, Y_Sum[3] , marker='.', mec='y', mfc='w',label=u'NM')
    plt.xlabel('time/year')
    plt.ylabel('Billion Btu')
    plt.legend(loc='upper left')
    #plt.legend(handles = [l1, l2, l3, l4,], labels = ['AZ', 'CA','TX','NM'], loc = 'best')
    #plt.title('resule:('+str(MSNNum)+')')
    plt.title(MSNName)


# enter the main def
if __name__ =="__main__":
    '''
    for i in range(1,605):
        for j in range(1,5):   #attention
            getPhoto(j,i)
        print '第' + str(i) + '种' + '.png'
        f_name = '第' + str(i) + '种' + '.png'
        f_path = source + f_name
        plt.savefig(f_path)
        plt.close()
    '''
    plt.subplot(231)
    getCertainPhoto4Satte(77)
    plt.subplot(232)
    getCertainPhoto4Satte(428)
    plt.subplot(233)
    getCertainPhoto4Satte(360)
    plt.subplot(234)
    getCertainPhoto4Satte(487)
    plt.subplot(235)
    getCertainPhoto4Satte(382)
    plt.subplot(236)
    getCertainPhoto4Satte(606)

    plt.show()
