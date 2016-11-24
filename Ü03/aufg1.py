import matplotlib.pyplot as plt
import numpy as np
import ROOT

# Make a directory for plots
import os
if not os.path.exists("./build"):
    os.makedirs("./build")




def aufg1():
    aufg1_a()
    aufg1_b()
    aufg1_c()
    aufg1_e()

def aufg1_a():

    f = ROOT.TFile("./build/NeutrinoMC.root", "RECREATE")
    gamma = 2.7
    E_min = 1
    n_sig = 10**5
    phi_0 = (1-gamma)/(E_min**(1-gamma))
    #aufgabenteil a
    u = np.random.rand(n_sig)
    E = (1-u)**(1/(1-gamma))

    tree = ROOT.TTree("Signal_MC", "Signal_MC")
    tree.Branch("Energie", E, "Energie/D")
    for i in range(len(E)):
        E[0] = E[i]
        tree.Fill()

    f.Write()
    f.Close()

def aufg1_b():

    def P(E):
        return (1-np.exp(-E/2))**3
    #Einlesen
    f = ROOT.TFile("./build/NeutrinoMC.root", "READ")
    tree = f.Get("Signal_MC")
    nentries = tree.GetEntries()
    E_val = np.zeros(1, dtype=float)
    E = np.zeros(nentries, dtype=float)
    tree.SetBranchAddress("Energie", E_val)
    nentries = tree.GetEntries()
    for i in range(nentries):
        tree.GetEntry(i)
        E[i] = E_val
    f.Close()

    #Rückweisungsverfahren
    Energie = np.zeros(1, dtype=float)
    f = ROOT.TFile("./build/NeutrinoMC.root", "RECREATE")
    tree = ROOT.TTree("Signal_MC", "Signal_MC")
    tree.Branch("Energie", Energie, "Energie/D")
    u = np.random.rand(len(E))
    E_neu = np.zeros(1)
    for i in range(len(E)):
        if u[i]<=P(E[i]):
            E_neu = np.append(E_neu,E[i])
    E_neu = np.delete(E_neu,0)
    for i in range(len(E_neu)):
        Energie = E_neu[i]
        tree.Fill()
    f.Write()
    f.Close()

    #Plotten
    #fig_a, ax_a = plt.subplots(1,1)
    #ax_a.hist(E,bins=np.logspace(1,3,50),range=(0,E.max()),log=True,label="Ereignisse")
    #ax_a.hist(E_neu,bins=np.logspace(1,3,50),range=(0,E.max()),log=True,label="detektierte Ereignisse")
    #ax_a.set_xscale('log')
    #ax_a.set_xlabel('Energie')
    #ax_a.set_ylabel('Ereignisse')
    #a_a.legend(loc="best")
    #fig_a.savefig("build/SignalEreignis.pdf")
    #f.Close()

def aufg1_c():
#Polar
    u1 = np.random.rand(50000)
    u2 = np.random.rand(50000)
    v1 = 2*u1-1
    v2 = 2*u2-1
    s = v1**2+v2**2
    temp = v1
    v1 = np.delete(np.sqrt(s-v2**2),s>=1)
    v2 = np.delete(np.sqrt(s-temp**2),s>=1)
    s = np.delete(s,s>=1)
    theta = np.arctan(v2/v1)
    r = np.sqrt(s)
    np.cos(theta)
    v3 = r*np.cos(theta)
    v4 = r*np.sin(theta)
    x1 = v3*np.sqrt(-2/s*np.log(s))
    x2 = v4*np.sqrt(-2/s*np.log(s))
    x1 = x1[np.logical_not(np.isnan(x1))]
    x2 = x2[np.logical_not(np.isnan(x2))]

    #fig_a, ax_a = plt.subplots(1,1)
    #ax_a.hist(x1,bins=np.linspace(0,5,50),label="Ereignisse")
    #ax_a.set_ylabel('Counts')
    #ax_a.legend(loc="best")
    #fig_a.savefig("Histpolar.pdf")

# umrechnen zu 10/2 -> z traffo
    x1 = (2*x1+10)
    x2 = (2*x2+10)
    x1 = np.around(x1)
    x2 = np.around(x2)
    x1 = x1[x1 != 0]
    x2 = x2[x2 != 0]

    plt.hist(x1)
    plt.show()
    E1 = (1-x1)**(1/(1-2.7))
    E2 = (1-x2)**(1/(1-2.7))
    def P(E):
        return (1-np.exp(-E/2))**3

    fig_a, ax_a = plt.subplots(1,1)
    ax_a.hist(x2,bins=np.linspace(0,5,50),label="Ereignisse")
    ax_a.set_ylabel('Counts')
    ax_a.legend(loc="best")
    fig_a.savefig("Histf.pdf")





def aufg1_e():

    #rootfile schreiben
    f = ROOT.TFile("./build/NeutrinoMC.root", "UPDATE")
    tree = ROOT.TTree("Untergrund_MC", "Untergrund_MC")
    n = 10**7
    rho = 0.5
    mean_N = 2
    sigma_xy = 3
    mean_xy = 5
    N =  np.random.randn(n)
    x_ = np.random.randn(n)
    y_ = np.random.randn(n)
    x = x_
    y = y_
    tree.Branch("AnzahlHits", N, "AnzahlHits/D")
    tree.Branch("x", x, "x/D")
    tree.Branch("y", y, "y/D")
    for i in range(len(N)):
        positiv = False
        while positiv == False:
            if N[i]+mean_N>0:
                N[i] = np.log(N[i]+mean_N)%1
                positiv = True
            else:
                N[i] = np.random.randn(1)
        positiv = False
        while positiv == False:
            x[i] = np.sqrt(1-rho**2)*sigma_xy*x_[i]+rho*sigma_xy*y_[i]+mean_xy
            y[i] = sigma_xy*y_[i]+mean_xy
            if x[i]>=0 and x[i]<=10 and y[i]>=0 and y[i]<=10:
                positiv = True
            else:
                x_[i] = np.random.randn(1)
                y_[i] = np.random.randn(1)
        N[0] = N[i]
        x[0] = x[i]
        y[0] = y[i]
        tree.Fill()
    f.Write()
    f.Close()

    #plotten
    f = ROOT.TFile("./build/NeutrinoMC.root", "READ")
    tree = f.Get("Untergrund_MC")
    nentries = tree.GetEntries()
    N_val = np.zeros(1, dtype=float)
    x_val = np.zeros(1, dtype=float)
    y_val = np.zeros(1, dtype=float)
    N = np.zeros(nentries, dtype=float)
    x = np.zeros(nentries, dtype=float)
    y = np.zeros(nentries, dtype=float)
    tree.SetBranchAddress("AnzahlHits", N_val)
    tree.SetBranchAddress("x", x_val)
    tree.SetBranchAddress("y", y_val)
    nentries = tree.GetEntries()
    for i in range(nentries):
        tree.GetEntry(i)
        N[i] = N_val
        x[i] = x_val
        y[i] = y_val

    fig_e1, ax_e1 = plt.subplots(1,1)
    ax_e1.hist2d(x,y,bins=100)
    ax_e1.set_xlabel("x")
    ax_e1.set_ylabel("y")
    #fig_e1.colorbar()
    fig_e1.savefig("build/UntergrungXY.pdf")

    fig_e2, ax_e2 = plt.subplots(1,1)
    ax_e2.hist(np.log(N),bins=100)
    ax_e1.set_xlabel("Logarithmus der Anzahl der Hits")
    fig_e2.savefig("build/UntergrungN.pdf")

    f.Close()

if __name__ == '__main__':
    aufg1()
