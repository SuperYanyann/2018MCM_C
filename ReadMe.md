# 2018 MCM C
  By Wang Yan
  73279


# configuration setting
ubuntu 17.0
python 2.7
numpu
matplotlib
sklearn
xlrd

# introduction of the program
the code is used to slove the Problem C in MCM/ICM 2018
in order to ensure that each program can run alone successfully,I copy the same def in different codes
and change it a little
so that each program can finish its own work
attention please,in some code,the data is changed by my self:
ProblemCData.xlsx is original Data
ProblemCData2.xlsx and ProblemCData3.xlsx are new Data
if you want to get the result of the code,you can ask the new Data from me

# introduction of each code

## dataset2.py
get the photo of certain 4 MSN
the MSNNum is 77 428 360 487
with legend and title
Atttneion:add 382 and 606,606 is "total"

## dataset3.py
can get the photo and dataset of certain stateNum and MSNNum

## dataset4.py
can get the 605 photos,and each photo has the 4 cols of data,every cols data is the data of the four states

## sortMSN.py
can get the kindArrNum of the MSN,by the sheel2

## sortMSN2.py
can get the kindArrData of the MSN,for example,by the sortMSN.py,we know the size of MSN whose unit is "Billion Btu" is 212,
so we can get a 212*n Arr,n is 40 or 50

## PCA1.py
use PCA to down the dataset

## PCA2.py
use PCA to down the dataset of 9 special MSNs,and ouput n photos,n is the num of rows of the downData

## PCA3.py
like to PCA2,but it can ouput line chart

## outputCSV
to put the output dataset to the CSV

## regression1.py
test to use the model of statsmodels

## regression2.py
use the "sklearn .linear_model" to achieve "multiple linear regression"
for examplt,the aim is CLTCB,and the input is [CLACB,CLCCB,CLEIB,CLICB,CLRCB]
we can get the aimCoefficients and aimIndependent,then we get the photo of oriY and newY to compare
we also get the means to detect the model

## entropy1.py
use entropy to get the weight of each targets and the score of the samples
becaus it just have the def,so if you want to use the code,you should get the inputArr by youself
if the inputArr is small and you juse wang to get the weight of one year,ues the code is right

## entropy2.py
use entropy to get the weight of each targets and the score of the samples
it is different from the entropy1.py because it get the needed Data in style 4*8
so it can get the weights and the samples the Part1_C needed

## entropy3.py
use to get the 3 MSNs in 2025,2050 from state1 to state4
the num of MSNs is 360,428,77

## weightTendencyMSN1.py
there is something wrong in this code,so the code is useless
I use Matblab to finish the work

## curveFitting1.py
use to fit the curve
use curve_fit from scipy.optimize,it can fit the curve by a certain function
can optimizate the parameter

## curveFitting2.py
use to get the GDPRV and TPOPP in 2025,2050
