import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams['figure.figsize'] = (15,10)
#plt.rcParams['font.size'] = 14

def aufg4():
    a0_mean = 1
    a1_mean = 1
    a0_sigma = 0.2
    a1_sigma = 0.2
    rho = -0.8
    n = 1000

    cov = a0_sigma*a1_sigma*np.array([[1,rho],[rho,1]])
    a = np.random.multivariate_normal(np.array([a0_mean,a1_mean]), cov, n)
    a0, a1 = a[:,0],a[:,1]

    # plt.plot(a0, a1,'bo')
    # plt.xlim(0,2)
    # plt.ylim(0,2)
    # plt.xlabel(r"$a_0$")
    # plt.ylabel(r"$a_1$")
    # plt.savefig("A4.pdf")

    print("numerisch:")
    print("mean_a0 =", np.mean(a0))
    print("mean_a1 =", np.mean(a1))
    print("sigma_a0 =", np.std(a0))
    print("sigma_a1 =", np.std(a1))
    print("y(-3)  = (", np.mean(a0+a1*-3),"+/-", np.std(a0+a1*-3),")")
    print("y( 0)  = (", np.mean(a0+a1* 0),"+/-", np.std(a0+a1* 0),")")
    print("y( 3)  = (", np.mean(a0+a1* 3),"+/-", np.std(a0+a1* 3),")")
    print("analytisch:")
    print("y(-3)  = (", 1+1*-3,"+/-", 0.2*np.sqrt(1+(-3)*(-3-1.6)),")")
    print("y( 0)  = (", 1+1* 0,"+/-", 0.2*np.sqrt(1+( 0)*( 0-1.6)),")")
    print("y( 3)  = (", 1+1* 3,"+/-", 0.2*np.sqrt(1+( 3)*( 3-1.6)),")")




if __name__ == '__main__':
    aufg4()
