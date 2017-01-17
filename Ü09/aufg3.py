import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Make a directory for plots
import os
import Tabellen

if not os.path.exists("./build"):
    os.makedirs("./build")

def C_matrix(n):
    C = np.zeros([n,n])
    if n > 2:
        for i in range(n-2):
            C[i+1][i+1] = -2
            C[i][i+1] = 1
            C[i+2][i+1] = 1
        C[0][0] = -1
        C[n-1][n-1] = -1
        C[0][1] = -1
        C[n-1][n-2] = -1
    return np.mat(C)


def polynom(x,p):
    y = np.zeros(len(x))
    for i in range(len(p)):
        y = y + x**i*p[i]
    return y

def MdkQ(x,y,n,yerr=None,l=0): #für Polynome n-ten Grades
    b = True
    if yerr == None:
        yerr = 1
        b = False
    yerr = np.array(yerr)
    W = np.eye(len(y))
    if b:
        for i in range(len(yerr)):
            W[i][i] = 1/yerr[i]**2

    A = np.ones([len(x),n+1])
    for i in range(len(x)):
        for j in range(n+1):
            A[i,j] = x[i]**j
    A = np.mat(A)
    C = C_matrix(len(y))
    y = np.mat(y)
    a = (A.T*W*A+l*(C*A).T*W*(C*A)).I*A.T*W*y.T
    return a.A


def aufg3():
    # a und b
    x, y = np.genfromtxt('aufg_a.csv',delimiter=',',unpack=True)
    lam = np.array([0,0.1,0.3,0.7,3,10])
    x = x[1:]
    y = y[1:]
    plt.plot(x,y,'bx',label='Messwerte')
    x_ = np.linspace(0,8)
    for i in range(len(lam)):
        lab = r"$\lambda$ = " + str(lam[i])
        a = MdkQ(x,y,6,l=lam[i])
        plt.plot(x_,polynom(x_,a),label=lab)
    plt.legend(loc='best')
    plt.savefig('./build/3b.png')
    plt.close()

    # c

    a0,a1,a2,a3,a4,a5,a6,a7,a8 = np.genfromtxt('aufg_c.csv',delimiter=',',unpack=False)
    lam = np.array([0,0.1,0.3,0.7,3,10])
    x = np.array([a1[0],a2[0],a3[0],a4[0],a5[0],a6[0],a7[0],a8[0]])
    y = np.array([np.mean(a1[1:]),np.mean(a2[1:]),np.mean(a3[1:]),np.mean(a4[1:]),np.mean(a5[1:]),np.mean(a6[1:]),np.mean(a7[1:]),np.mean(a8[1:])])
    yerr = np.array([np.std(a1[1:]),np.std(a2[1:]),np.std(a3[1:]),np.std(a4[1:]),np.std(a5[1:]),np.std(a6[1:]),np.std(a7[1:]),np.std(a8[1:])])
    plt.errorbar(x,y,yerr=yerr,fmt='bx',label='Messwerte')
    x_ = np.linspace(0,8)
    for i in range(len(lam)):
        lab = r"$\lambda$ = " + str(lam[i])
        a = MdkQ(x,y,6,yerr=yerr,l=lam[i])
        if i == 5:
            print(np.round(a,3))
        plt.plot(x_,polynom(x_,a),label=lab)
    plt.legend(loc='best')
    plt.savefig('./build/3c.png')
    plt.close()










if __name__ == '__main__':
    aufg3()
