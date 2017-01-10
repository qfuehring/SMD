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

Test1 = np.array(Test)
Train1 = np.array(Train)
print(Train1[:,-1])

# a) Korrelationsmatrix
corTest = Train.corr()['SalePrice']
#print(abs(corTest).nlargest(4))

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

# b) lineare Regression
# Datenbereinigung
'''
index = Train['OverallQual'].index[Train
['OverallQual'].apply(np.isnan)]
Train_index = Train.index.values.tolist()
print(Train_index.index(i) for i in index)
'''
reg = linear_model.LinearRegression()
reg.fit(np.split(Train1[:,-1],1460),Train['OverallQual'])
m = reg.coef_
b = reg.intercept_
print(reg.coef_)
print(reg.intercept_)


#par, cov = curve_fit(lin, Train['GarageCars'],Train['SalePrice'])
#print(par)

#print(Train['OverallQual'])
x = np.linspace(0,10,1460)
plt.plot(x, x/m[0]-b/m[0], 'r',label= 'Fit')
plt.scatter(Train['OverallQual'],Train['SalePrice'], s = 5, alpha = 0.6)
plt.xlabel('OverallQual')
plt.ylabel('SalePrice')
#plt.show()
plt.savefig('SP_OvQ.pdf')
plt.legend()
plt.close()
