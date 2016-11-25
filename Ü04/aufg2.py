import matplotlib.pyplot as plt
import numpy as np
import ROOT

# Make a directory for plots
import os
if not os.path.exists("./build"):
    os.makedirs("./build")




def aufg2():
    Plotten()
    proj()


def Plotten():
    #Einlesen
    f = ROOT.TFile("./build/zwei_populationen.root", "READ")
    P_0 = f.Get("P_0_10000")
    n_0 = P_0.GetEntries()
    x_0_val = np.zeros(1, dtype=float)
    x_0 = np.zeros(n_0, dtype=float)
    y_0_val = np.zeros(1, dtype=float)
    y_0 = np.zeros(n_0, dtype=float)
    P_0.SetBranchAddress("x", x_0_val)
    P_0.SetBranchAddress("y", y_0_val)
    for i in range(n_0):
        P_0.GetEntry(i)
        x_0[i] = x_0_val
        y_0[i] = y_0_val

    P_1 = f.Get("P_1")
    n_1 = P_1.GetEntries()
    x_1_val = np.zeros(1, dtype=float)
    x_1 = np.zeros(n_1, dtype=float)
    y_1_val = np.zeros(1, dtype=float)
    y_1 = np.zeros(n_1, dtype=float)
    P_1.SetBranchAddress("x", x_1_val)
    P_1.SetBranchAddress("y", y_1_val)
    for i in range(n_1):
        P_1.GetEntry(i)
        x_1[i] = x_1_val
        y_1[i] = y_1_val
    f.Close()

    x_sum = np.concatenate((x_0,x_1))
    y_sum = np.concatenate((y_0,y_1))

    #Plotten
    fig, ax_0 = plt.subplots(1,1)
    ax_0.scatter(x_0,y_0,c='b',marker='.',label=r"$P_0$")
    ax_0.scatter(x_1,y_1,c='r',marker='.',label=r"$P_1$")
    ax_0.set_ylabel("y")
    ax_0.set_xlabel("x")
    ax_0.set_title("zwei Populationen")
    ax_0.legend(loc='best')
    fig.savefig("build/scatter_aufg2.pdf")

def proj():
    f = ROOT.TFile("./build/zwei_populationen.root", "READ")
    P_0 = f.Get("P_0_10000")
    n_0 = P_0.GetEntries()
    x_0_val = np.zeros(1, dtype=float)
    x_0 = np.zeros(n_0, dtype=float)
    y_0_val = np.zeros(1, dtype=float)
    y_0 = np.zeros(n_0, dtype=float)
    P_0.SetBranchAddress("x", x_0_val)
    P_0.SetBranchAddress("y", y_0_val)
    for i in range(n_0):
        P_0.GetEntry(i)
        x_0[i] = x_0_val
        y_0[i] = y_0_val

    P_1 = f.Get("P_1")
    n_1 = P_1.GetEntries()
    x_1_val = np.zeros(1, dtype=float)
    x_1 = np.zeros(n_1, dtype=float)
    y_1_val = np.zeros(1, dtype=float)
    y_1 = np.zeros(n_1, dtype=float)
    P_1.SetBranchAddress("x", x_1_val)
    P_1.SetBranchAddress("y", y_1_val)
    for i in range(n_1):
        P_1.GetEntry(i)
        x_1[i] = x_1_val
        y_1[i] = y_1_val
    f.Close()

    a_0 = 0
    a_1 = -3/4
    a_2 = -5/4
    x_P0_0 = x_0
    x_P1_0 = x_1
    x_P0_1 = (x_0+a_1*y_0)/(a_1**2+1)
    x_P1_1 = (x_1+a_1*y_1)/(a_1**2+1)
    x_P0_2 = (x_0+a_2*y_0)/(a_2**2+1)
    x_P1_2 = (x_1+a_2*y_1)/(a_2**2+1)

    fig, [ax_1, ax_2, ax_3] = plt.subplots(1,3,figsize=(18,6))
    ax_1.hist(x_P0_0,bins=50, color="b", alpha=0.5, label=r"$P_0$")
    ax_1.hist(x_P1_0,bins=50, color="r", alpha=0.5, label=r"$P_1$")
    ax_1.legend(loc='best')
    ax_1.set_xlabel(r"$x_{proj}$")
    ax_1.set_title("g(x)=0")
    ax_2.hist(x_P0_1,bins=50, color="b", alpha=0.5, label=r"$P_0$")
    ax_2.hist(x_P1_1,bins=50, color="r", alpha=0.5, label=r"$P_1$")
    ax_2.legend(loc='best')
    ax_2.set_xlabel(r"$x_{proj}$")
    ax_2.set_title("g(x)=-3/4x")
    ax_3.hist(x_P0_2,bins=50, color="b", alpha=0.5, label=r"$P_0$")
    ax_3.hist(x_P1_2,bins=50, color="r", alpha=0.5, label=r"$P_1$")
    ax_3.legend(loc='best')
    ax_3.set_xlabel(r"$x_{proj}$")
    ax_3.set_title("g(x)=-5/4x")
    fig.savefig("./build/proj_aufg2.pdf")


if __name__ == '__main__':
    aufg2()
