# -*- coding: UTF-8 -*-
import numpy
import xlrd
import matplotlib
import matplotlib.pyplot as plt

# get the data of MSN
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData.xlsx')
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
nrows = sheet1.nrows  
ncols = sheet1.ncols

# get the kindName of the MSN
def getKingName(kingNum):
    if kingNum == 1:
        return sheet2.cell(1,2).value
    elif kingNum == 2:
        return sheet2.cell(2,2).value
    else:
        return sheet2.cell(3,2).value

# sort the MSN,the num is the kingNum of MSN
def getKingArr(kingNum):
    kingName = getKingName(kingNum)
    kingArr = []
    kingNum = 0
    for i in range(1,605):
        kingNum = kingNum + 1
        if sheet2.cell(i,2).value == kingName:
            kingArr.append(kingNum)
    return kingArr


if __name__ =="__main__":
    kingArr1 = getKingArr(1)
    print kingArr1
