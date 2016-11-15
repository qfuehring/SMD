import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['figure.figsize'] = (15,10)
#plt.rcParams['font.size'] = 14

def aufg4():
    a0 = 1
    a1 = 1
    a0_sigma = 0.2
    a1_sigma = 0.2
    rho = -0.8
    n = 10000
    cov = a0_sigma*a1_sigma*np.array([[1,rho],[rho,1]])            
    a = np.random.multivariate_normal(np.array([a0,a1]), cov, n)
    plt.plot(a[:,0],a[:,1],'bo')
    plt.xlim(0,2)
    plt.ylim(0,2)
    plt.xlabel(r"$a_0$")
    plt.ylabel(r"$a_1$")
    plt.savefig("A4.pdf")



if __name__ == '__main__':
    aufg4()
