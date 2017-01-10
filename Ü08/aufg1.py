import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from scipy.optimize import curve_fit

def lin(x, m, b):
    return m*x+b
# a) Importing Data from csv

Test = pd.read_csv('test.csv')
Train = pd.read_csv('train.csv')

# a) Korrelationsmatrix
corTest = Train.corr()['SalePrice']
print(abs(corTest).nlargest(4))

# a) scatterplots

plt.scatter(Train['GrLivArea'],Train['SalePrice'], s = 5, alpha = 0.6)
plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
#plt.show()
plt.savefig('SP_GLA.pdf')
plt.close()

plt.scatter(Train['GarageCars'],Train['SalePrice'], s = 5, alpha = 0.6)
plt.xlabel('GarageCars')
plt.ylabel('SalePrice')
#plt.show()
plt.savefig('SP_GC.pdf')
plt.close()
'''
# b) lineare Regression

reg = linear_model.LinearRegression()
reg.fit(Train['OverallQual'].values.reshape(-1, 1),Train['SalePrice'].values.reshape(-1, 1))
m = reg.coef_
par, cov = curve_fit(lin, Train['GarageCars'],Train['SalePrice'])
print(par)

#print(Train['OverallQual'])
x = np.linspace(0,10,1460)
plt.plot(x, x*m[0]-50000, 'r',label= 'Fit')
'''
plt.scatter(Train['OverallQual'],Train['SalePrice'], s = 5, alpha = 0.6)
plt.xlabel('OverallQual')
plt.ylabel('SalePrice')
#plt.show()
plt.savefig('SP_OvQ.pdf')
plt.legend()
plt.close()
