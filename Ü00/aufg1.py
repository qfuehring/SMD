import matplotlib.pyplot as plt
import numpy as np

def aufg1():
    print("Übungsblatt00, Aufagbe 1")

    def a(x):
        return (1-x)**6

    def b(x):
        return x**6 - 6*x**5 + 15*x**4 - 20*x**3 + 15*x**2 -6*x + 1

    def c(x):
        return x*(x*(x*(x*((x-6)*x+15)-20)+15)-6)+1

    x = np.linspace(0.999,1.001,1000)

    #Plots
    plt.subplot(311)
    plt.plot(x,a(x),label=r"$(1-x)^6$")
    plt.xlim(0.999,1.001)
    plt.legend()
    plt.subplot(312)
    plt.plot(x,b(x),label=r"naiv")
    plt.xlim(0.999,1.001)
    plt.legend()
    plt.subplot(313)
    plt.plot(x,c(x),label=r"Horner")
    plt.xlim(0.999,1.001)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    aufg1()
