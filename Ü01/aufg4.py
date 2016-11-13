import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg as LA

plt.rcParams['figure.figsize'] = (15,10)
plt.rcParams['font.size'] = 14

def aufg4():
    print("Übungsblatt01, Aufagbe 4")

    mean_x = 4
    mean_y = 2
    sigma_x = 3.5
    sigma_y = 1.5
    cov_xy = 4.2
    rho_xy = cov_xy/sigma_x/sigma_y
    E_xy=cov_xy+mean_x*mean_y

    B=np.matrix([[sigma_y**2,-cov_xy],[-cov_xy,sigma_x**2]])/(sigma_x**2*sigma_y**2-cov_xy**2)

    def f(x,y):
        F = np.zeros((len(x),len(y)))
        i=0
        while i < len(x):
            j=0
            while j < len(y):
                F[i, j] = 1/(2*np.pi*sigma_x*sigma_y*np.sqrt(1-rho_xy**2))*np.exp(-0.5*(((x[i]-mean_x)/sigma_x)**2-2*rho_xy*((x[i]-mean_x)/sigma_x)*((y[j]-mean_y)/sigma_y)+((y[j]-mean_y)/sigma_y)**2)/(1-rho_xy**2))
                j=j+1
            i=i+1
        return F

    a=5
    n=100
    x=np.linspace(mean_x-a,mean_x+a,n)
    y=np.linspace(mean_y-a,mean_y+a,n)
    X, Y = np.meshgrid(x, y)
    plt.pcolormesh(X,Y,f(x,y))
    plt.colorbar()
    CS=plt.contour(X,Y,f(x,y),levels=[1/(2*np.pi*sigma_x*sigma_y*np.sqrt(1-rho_xy**2))*np.exp(-0.5)])
    plt.errorbar(mean_x,mean_y,yerr=sigma_x,xerr=sigma_y,fmt='kx',label=r"$(\mu_x\pm\sigma_x,\mu_y\pm\sigma_y)$")
    plt.axis([x.min(), x.max(), y.min(), y.max()])
    CS.collections[0].set_label(r"$1/\sqrt{e}$")

    print()
    print("a)")
    print("rho(x,y) =",rho_xy)

    print()
    print("d)")
    print("B =", B)
    B0 = np.matrix([[1.38876,0],[0,0.725693]])
    print("B0 =",B0)
    M = np.matrix([[-0.342268,-0.939602],[0.939602,-0.342268]])
    M_= M.I
    print("M =",M)
    print("M_=",M_)
    print(M_*B*M)
    sigma_x_ = B0[0,0]**-2
    sigma_y_ = B0[1,1]**-2
    print("sigma_x_ =",sigma_x_)
    print("sigma_y_ =",sigma_y_)
    plt.errorbar(mean_x,mean_y,yerr=sigma_y_,xerr=sigma_x_,fmt='bx',label=r"$(\mu_x\pm\sigma'_x,\mu_y\pm\sigma'_y)$")

    print()
    print("e)")
    alpha = 0.5*np.arctan(2*rho_xy*sigma_x*sigma_y/(sigma_x**2-sigma_y**2))
    print("alpha =",alpha/np.pi*180)
    p1=np.sqrt((1-rho_xy**2)/(np.cos(alpha)**2/sigma_x**2-2*rho_xy*np.sin(alpha)*np.cos(alpha)/sigma_x/sigma_y+np.sin(alpha)**2/sigma_y**2))
    p2=np.sqrt((1-rho_xy**2)/(np.sin(alpha)**2/sigma_x**2-2*rho_xy*np.sin(alpha)*np.cos(alpha)/sigma_x/sigma_y+np.cos(alpha)**2/sigma_y**2))
    print("p1 =",p1)
    print("p2 =",p2)
    s=np.linspace(0,p1)
    plt.plot(mean_x+s*np.sin(alpha),mean_y+s*np.cos(alpha),'k--',label=r"$p_1$")
    s=np.linspace(0,p2)
    plt.plot(mean_x+s*np.cos(alpha),mean_y-s*np.sin(alpha),'k-.',label=r"$p_2$")


    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
    plt.savefig("aufg4.pdf")

if __name__ == '__main__':
    aufg4()
