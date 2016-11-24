import matplotlib.pyplot as plt
import numpy as np

def aufg3():
    print("Übungsblatt00, Aufagbe 3")

    def f(x):   #Aufagbenteil a)
        return (x**3+1/3)-(x**3-1/3)            #entspricht konst. 2/3

    def g(x):   #Aufagbenteil a)
        return ((3+x**3/3)-(3-x**3/3))/x**3     #entspricht konst. 2/3


    n=20000
    fig, (ax1, ax2) = plt.subplots(2, 1)

    print("\n\nAufgabenteil a)\n")
    x = np.linspace(-100000,100000,n+1)
    abweichung=10
    i=0
    while i < n:
        if f(x[i])>1.01*2/3 or f(x[i])<0.99*2/3:
            if f(x[i])==0:
                abweichung_neu=0
            else:
                abweichung_neu=1
        else:
            abweichung_neu=-1
        if abweichung!=abweichung_neu:
            if abweichung_neu==1:
                print("Ab x =",x[i],"ist die Abweichung größer 1%")
                abweichung=abweichung_neu
            elif abweichung_neu==-1:
                print("Ab x =",x[i],"ist die Abweichung kleiner 1%")
                abweichung=abweichung_neu
            elif abweichung_neu==0:
                print("Ab x =",x[i]," ist der numerisch berechnete Funktionswert = 0")
                abweichung=10
        i=i+1

    ax1.plot(x,np.abs((f(x)-2/3)/(2/3)),label=r"(f(x)-2/3)/(2/3)")
    ax1.plot(x,0.01*x/x,'r--')
    #ax1.set_xlim(0.999,1.001)
    ax1.set_title(r"f(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("rel. Abweichung")
    #ax1.set_xscale("log")

    print("\n\nAufgabenteil b)\n")
    x = np.linspace(-0.01,0.01,n+1)
    abweichung=10
    i=0
    while i < n:
        if g(x[i])>1.01*2/3 or g(x[i])<0.99*2/3:
            if g(x[i])==0:
                abweichung_neu=0
            else:
                abweichung_neu=1
        else:
            abweichung_neu=-1
        if abweichung!=abweichung_neu:
            if abweichung_neu==1:
                print("Ab x =",x[i],"ist die Abweichung größer 1%")
                abweichung=abweichung_neu
            elif abweichung_neu==-1:
                print("Ab x =",x[i],"ist die Abweichung kleiner 1%")
                abweichung=abweichung_neu
            elif abweichung_neu==0:
                print("Ab x =",x[i]," ist der numerisch berechnete Funktionswert = 0")
                abweichung=10

        i=i+1

    ax2.plot(x,np.abs((g(x)-2/3)/(2/3)),label=r"(g(x)-2/3)/(2/3)")
    ax2.plot(x,0.01*x/x,'r--')
    ax2.set_xlim(0.000005,0.0002)
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlabel("|x|")
    ax2.set_ylabel("rel. Abweichung")
    ax2.set_title(r"g(x)")


    fig.tight_layout()
    fig.savefig("A3.pdf")

if __name__ == '__main__':
    aufg3()
