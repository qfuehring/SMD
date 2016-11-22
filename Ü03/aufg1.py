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
    u = 1+np.random.rand(n_sig)*10**9
    E = (1-u)**(1/(1-gamma))

    tree = ROOT.TTree("Signal_MC", "Signal_MC")
    tree.Branch("Energie", E, "Energie/D")
    for i in range(len(E)):
        tree.Fill()

    f.Write()
    f.Close()

    plt.plot(u,E)
    plt.show()

if __name__ == '__main__':
    aufg1()
