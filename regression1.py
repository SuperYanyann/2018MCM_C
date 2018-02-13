import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm

# test
nsample = 100
x = np.linspace(0,10,nsample)
x = sm.add_constant(x)

beta = np.array([1,10])
e = np.random.normal(size = nsample)
y = np.dot(x,beta) + e

model = sm.OLS(y,x)
result = model.fit()
print result.params
