import matplotlib.pyplot as plt
import numpy as np

def aufg3():
    print("Übungsblatt00, Aufagbe 3")

    def f(x):   #Aufagbenteil a)
        return (x**3+1/3)-(x**3-1/3)

    def f_(x):  #vereinfacht
        return 2/3*np.ones(len(x))

    def g(x):   #Aufagbenteil a)
        return ((3+x**3/3)-(3-x**3/3))/x**3

    def g_(x):  #vereinfacht
        return 2/3*np.ones(len(x))

    n=100
    x = np.linspace(-100000,100000,n)
    y = np.linspace(-0.0001,0.0001,n)

    # a = [x, f(x), f_(x), np.abs(f(x)-f_(x))/f_(x)]
    # b = [y, g(y), g_(y), np.abs(g(y)-g_(y))/g_(y)]
    # print(a)
    # print(b)
    # #Plots
    # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    #
    # ax1.plot(x,f(x),label=r"$f(x)$")
    # ax1.set_xlim(x[0],x[-1])
    # ax1.set_title(r"$f(x)$")
    # ax2.plot(x,g(x),'b',label=r"$g(x)$")
    # ax2.plot(y,g_(y),'r--',label=r"wahrer Wert")
    # ax2.set_xlim(y[0],y[-1])
    # ax2.set_title(r"$g(x)$")
    # ax3.plot(x,np.abs(f(x)-f_(x))/2*3,'r--',label=r"wahrer Wert")
    # ax3.set_xlim(x[0],x[-1])
    # ax3.set_yscale('log')
    # ax3.set_title(r"$f(x)$")
    # ax4.plot(y,np.abs(g(y)-g_(y))/2*3,'r--',label=r"wahrer Wert")
    # ax4.set_xlim(y[0],y[-1])
    # ax4.set_yscale('log')
    # ax4.set_title(r"$g(x)$")
    # fig.tight_layout()
    # fig.savefig("A3.pdf")
    # print(g(y))
    i=10000
    while i < n:
        if f(x[i])>1.01*2/3 or f(x[i])<0.99*2/3:
            if f(x[i])==0:
                print(x[i],"\t",f(x[i]), "\t=0")
            else:
                print(x[i],"\t",f(x[i]), "\tAbweichung >1%") #ab größer 40000
        else:
            print(x[i],"\t",f(x[i]), "\tAbweichung <1%")
        i=i+1

    i=0
    while i < n:
        if g(y[i])>1.01*2/3 or g(y[i])<0.99*2/3:
            if g(y[i])==0:
                print(y[i],"\t",g(y[i]), "\t=0") #ab kleiner 0,7e05
            else:
                print(y[i],"\t",g(y[i]), "\tAbweichung >1%") #ab kleiner 2,7e05
        else:
            print(y[i],"\t",g(y[i]), "\tAbweichung <1%")
        i=i+1

if __name__ == '__main__':
    aufg3()
