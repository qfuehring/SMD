import matplotlib.pyplot as plt
import numpy as np
import ROOT

# Make a directory for plots
import os
if not os.path.exists("./build"):
    os.makedirs("./build")




def aufg1():
    aufg1_a()

def aufg1_a():

    f = ROOT.TFile("./build/NeutrinoMC.root", "RECREATE")
    gamma = 2.7
    E_min = 1
    n_sig = 10**5
    phi_0 = (1-gamma)/(E_min**(1-gamma))
    print(phi_0)
    #aufgabenteil a
    u = np.random.rand(n_sig)
    E = (1-u)**(1/(1-gamma))

    tree = ROOT.TTree("Signal_MC", "Signal_MC")
    tree.Branch("Energie", E, "Energie/D")
    for i in range(len(E)):
        tree.Fill()

    f.Write()
    f.Close()

    plt.hist(E,bins=np.logspace(1,3,50),range=(0,E.max()),log=True)
    plt.xscale('log')
    plt.xlabel('Energie')
    plt.ylabel('Ereignisse')
    plt.show()

if __name__ == '__main__':
    aufg1()
