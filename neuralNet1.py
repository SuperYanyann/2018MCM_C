# -*- coding: UTF-8 -*-
import torch
import torch.nn as nn
from torch.autograd import *
import torch.optim as optim
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import xlrd

#learn from https://mp.weixin.qq.com/s?__biz=MzA5NDM4MjMxOQ==&mid=2447578969&idx=1&sn=1ae03db749b56b1d2a140e1369bd8dba&chksm=8458c6d9b32f4fcf2ade01c726fa734476a9e173eb1189cc3a4eef3e0d350a635ea986e8f35c&mpshare=1&scene=1&srcid=0212XZYGJ80skfO7hOjclOb7&pass_ticket=4Ny3sz5foHRLUkvLoDFapNEMyCtao9JWtiG8SlAqvSYQiUvIQsIROlNPJ5l3iFyN#rd

# get the dataset
data = xlrd.open_workbook('/home/yanwang/文档/competition/2018美赛/数据/ProblemCData2.xlsx')
sheet1 = data.sheet_by_index(0)
sheet2 = data.sheet_by_index(1)
sheet3 = data.sheet_by_index(4)
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



def SeriesGen(N):
    x = torch.range(1,N,0.01)
    return torch.sin(x)

def trainDataGen(seq,k):
    dat = list()
    L = len(seq)
    for i in range(L-k-1):
        indat = seq[i:i+k]
        outdat = seq[i+1:i+k+1]
        dat.append((indat,outdat))
    return dat

def ToVariable(x):
    tmp = torch.FloatTensor(x)
    return Variable(tmp)


class LSTMpred(nn.Module):

    def __init__(self,input_size,hidden_dim):
        super(LSTMpred,self).__init__()
        self.input_dim = input_size
        self.hidden_dim = hidden_dim
        self.lstm = nn.LSTM(input_size,hidden_dim)
        self.hidden2out = nn.Linear(hidden_dim,1)
        self.hidden = self.init_hidden()

    def init_hidden(self):
        return (Variable(torch.zeros(1, 1, self.hidden_dim)),
                Variable(torch.zeros(1, 1, self.hidden_dim)))

    def forward(self,seq):
        lstm_out, self.hidden = self.lstm(
            seq.view(len(seq), 1, -1), self.hidden)
        outdat = self.hidden2out(lstm_out.view(len(seq),-1))
        return outdat


if __name__ =="__main__":
    #y = SeriesGen(10)
    #dat = trainDataGen(y.numpy(),10)
    y = getData1S1M(1,190)
    y = torch.FloatTensor(y)
    dat = trainDataGen(y.numpy(),4)

    print np.shape(dat)

    model = LSTMpred(1,6)
    loss_function = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    for epoch in range(100):
        print(epoch)
        for seq, outs in dat[:19]:

            seq = ToVariable(seq)
            outs = ToVariable(outs)
            #outs = torch.from_numpy(np.array([outs]))

            optimizer.zero_grad()

            model.hidden = model.init_hidden()

            modout = model(seq)

            loss = loss_function(modout, outs)
            loss.backward()
            optimizer.step()

    predDat = []
    inCicle = 1
    for seq, trueVal in dat[19:]:
        inCicle = inCicle+1
        print inCicle
        seq = ToVariable(seq)
        trueVal = ToVariable(trueVal)
        print seq
        print trueVal
        print model(seq)
        predDat.append(model(seq)[-1].data.numpy()[0])


    fig = plt.figure()
    plt.plot(y.numpy())
    print predDat
    plt.plot(range(30,40),predDat)
    plt.show()
