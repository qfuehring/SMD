import matplotlib.pyplot as plt
import numpy as np

def aufg1():
    print("Übungsblatt00, Aufagbe 1")

    def a(x):   #Aufagbenteil a)
        return (1-x)**6

    def b(x):   #Aufagbenteil b)
        return x**6 - 6*x**5 + 15*x**4 - 20*x**3 + 15*x**2 -6*x + 1     #Ausmulitplitziert Binomische Formel

    def c(x):   #Aufagbenteil c)
        return x*(x*(x*(x*((x-6)*x+15)-20)+15)-6)+1                     #Ausmulitplitziert Horner-Schema

    x = np.linspace(0.999,1.001,1000)

    #Plots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

    ax1.plot(x,a(x),label=r"$(1-x)^6$")
    ax1.set_xlim(0.999,1.001)
    ax1.set_title(r"$(1-x)^6$")
    ax2.plot(x,b(x),label=r"naiv")
    ax2.set_xlim(0.999,1.001)
    ax2.set_title(r"naiv")
    ax3.plot(x,c(x),label=r"Horner")
    ax3.set_title(r"Horner")
    ax3.set_xlim(0.999,1.001)
    fig.tight_layout()
    fig.savefig("A1.pdf")

if __name__ == '__main__':
    aufg1()
