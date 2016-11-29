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
    x = np.linspace(x_sum.min()-3,x_sum.max()+3)
    fig, ax_0 = plt.subplots(1,1)
    ax_0.scatter(x_0,y_0,c='b',marker='.',label=r"$P_0$")
    ax_0.scatter(x_1,y_1,c='r',marker='.',label=r"$P_1$")
    ax_0.plot(x,x-x,label=r"$g_0$")
    ax_0.plot(x,-3/4*x,label=r"$g_1$")
    ax_0.plot(x,-5/4*x,label=r"$g_2$")
    ax_0.set_xlim(x_sum.min()-3,x_sum.max()+3)
    ax_0.set_ylim(y_sum.min()-3,y_sum.max()+3)
    ax_0.set_ylabel("y")
    ax_0.set_xlabel("x")
    ax_0.set_title("zwei Populationen")
    ax_0.legend(loc='best')
    fig.savefig("build/scatter_aufg2.png")

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
    # Proj.: x' = (x y)*(-1 -a)/((-1 -a)*(-1 -a))
    x_P0_0 = (-x_0*1-a_0*y_0)/(a_0*a_0+1*1)
    x_P1_0 = (-x_1*1-a_0*y_1)/(a_0*a_0+1*1)
    x_P0_1 = (-x_0*1-a_1*y_0)/(a_1*a_1+1*1)
    x_P1_1 = (-x_1*1-a_1*y_1)/(a_1*a_1+1*1)
    x_P0_2 = (-x_0*1-a_2*y_0)/(a_2*a_2+1*1)
    x_P1_2 = (-x_1*1-a_2*y_1)/(a_2*a_2+1*1)

    min_0 = np.array([x_P1_0,x_P0_0]).min()
    max_0 = np.array([x_P1_0,x_P0_0]).max()
    min_1 = np.array([x_P1_1,x_P0_1]).min()
    max_1 = np.array([x_P1_1,x_P0_1]).max()
    min_2 = np.array([x_P1_2,x_P0_2]).min()
    max_2 = np.array([x_P1_2,x_P0_2]).max()

    cut_0 = np.linspace(min_0,max_0)
    cut_1 = np.linspace(min_1,max_1)
    cut_2 = np.linspace(min_2,max_2)
    r_0 = np.ones(len(cut_0))
    e_0 = np.zeros(len(cut_0))
    r_1 = np.ones(len(cut_1))
    e_1 = np.zeros(len(cut_1))
    r_2 = np.ones(len(cut_2))
    e_2 = np.zeros(len(cut_2))

    for i in range(len(cut_0)-1):
        r_0[i] = len(x_P0_0[x_P0_0 > cut_0[i]])/(len(x_P0_0[x_P0_0 > cut_0[i]])+len(x_P1_0[x_P1_0 > cut_0[i]]))
        e_0[i] = len(x_P0_0[x_P0_0 > cut_0[i]])/(len(x_P0_0[x_P0_0 > cut_0[i]])+len(x_P0_0[x_P0_0 <= cut_0[i]]))
    for i in range(len(cut_1)-1):
        r_1[i] = len(x_P0_1[x_P0_1 > cut_1[i]])/(len(x_P0_1[x_P0_1 > cut_1[i]])+len(x_P1_1[x_P1_1 > cut_1[i]]))
        e_1[i] = len(x_P0_1[x_P0_1 > cut_1[i]])/(len(x_P0_1[x_P0_1 > cut_1[i]])+len(x_P0_1[x_P0_1 < cut_1[i]]))
    for i in range(len(cut_0)-1):
        r_2[i] = len(x_P0_2[x_P0_2 > cut_2[i]])/(len(x_P0_2[x_P0_2 > cut_2[i]])+len(x_P1_2[x_P1_2 > cut_2[i]]))
        e_2[i] = len(x_P0_2[x_P0_2 > cut_2[i]])/(len(x_P0_2[x_P0_2 > cut_2[i]])+len(x_P0_2[x_P0_2 < cut_2[i]]))

    fig1, [ax_1, ax_2, ax_3] = plt.subplots(1,3,figsize=(18,6))
    ax_1.hist(x_P0_0,bins=50, range=(min_0,max_0), color="b", alpha=0.5, label=r"$P_0$")
    ax_1.hist(x_P1_0,bins=50, range=(min_0,max_0), color="r", alpha=0.5, label=r"$P_1$")
    ax_1.legend(loc='best')
    ax_1.set_xlabel(r"$x_{proj}$")
    ax_1.set_title("g(x)=0")
    ax_2.hist(x_P0_1,bins=50, range=(min_1,max_1), color="b", alpha=0.5, label=r"$P_0$")
    ax_2.hist(x_P1_1,bins=50, range=(min_1,max_1), color="r", alpha=0.5, label=r"$P_1$")
    ax_2.legend(loc='best')
    ax_2.set_xlabel(r"$x_{proj}$")
    ax_2.set_title("g(x)=-3/4x")
    ax_3.hist(x_P0_2,bins=50, range=(min_2,max_2), color="b", alpha=0.5, label=r"$P_0$")
    ax_3.hist(x_P1_2,bins=50, range=(min_2,max_2), color="r", alpha=0.5, label=r"$P_1$")
    ax_3.legend(loc='best')
    ax_3.set_xlabel(r"$x_{proj}$")
    ax_3.set_title("g(x)=-5/4x")
    fig1.savefig("./build/proj_aufg2.png")

    fig2, [ax_4, ax_5, ax_6] = plt.subplots(1,3,figsize=(18,6))
    ax_4.plot(cut_0,r_0,label="Reinheit")
    ax_4.plot(cut_0,e_0,label="Effizienz")
    ax_4.legend(loc='best')
    ax_4.set_xlabel(r"$\lambda_{cut}$")
    ax_4.set_xlim(min_0,max_0)
    ax_4.set_ylim(0,1)
    ax_4.set_title("g(x)=0")
    ax_5.plot(cut_1,r_1,label="Reinheit")
    ax_5.plot(cut_1,e_1,label="Effizienz")
    ax_5.legend(loc='best')
    ax_5.set_xlabel(r"$\lambda_{cut}$")
    ax_5.set_xlim(min_1,max_1)
    ax_5.set_ylim(0,1)
    ax_5.set_title("g(x)=-3/4x")
    ax_6.plot(cut_2,r_2,label="Reinheit")
    ax_6.plot(cut_2,e_2,label="Effizienz")
    ax_6.legend(loc='best')
    ax_6.set_xlabel(r"$\lambda_{cut}$")
    ax_6.set_xlim(min_2,max_2)
    ax_6.set_ylim(0,1)
    ax_6.set_title("g(x)=-5/4x")
    fig2.savefig("./build/Unterscheidung_aufg2.png")


if __name__ == '__main__':
    aufg2()
