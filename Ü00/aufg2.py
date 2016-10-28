import matplotlib.pyplot as plt
import numpy as np

def aufg2():
    print("Übungsblatt00, Aufagbe 1")

    #Aufgabe b
    print("b)")

    def f(x):
        return (np.sqrt(9-x)-3)/x

    i=1
    while i<21:
        x = 10**-i
        print("x =",x, "f(x) =",f(x))
        i=i+1

if __name__ == '__main__':
    aufg2()
