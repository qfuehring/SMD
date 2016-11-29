import matplotlib.pyplot as plt
import numpy as np
import ROOT

# Make a directory for plots
import os
if not os.path.exists("./build"):
    os.makedirs("./build")




def aufg1():
    TreesErstellen()
    Plotten()

def TreesErstellen():

    mu_x0 = 0
    mu_y0 = 3
    sigma_x0 = 3.5
    sigma_y0 = 2.6
    rho_0 = 0.9
    #Da der Koeffzientenvgl. bei Aufgabe a fehlschlug, wird für P1 die selbe Verteilung der y-Werte und Korrelation wie bei P0 verwendet
    mu_x1 = 6
    mu_y1 = 3
    sigma_x1 = 3.5
    sigma_y1 = 2.6
    cov_0 = np.matrix([[sigma_x0**2,sigma_y0*sigma_x0*rho_0],[sigma_y0*sigma_x0*rho_0,sigma_y0**2]])

    u_0_10000 = np.random.multivariate_normal([mu_x0,mu_y0],cov_0,10000)
    u_0_1000 = np.random.multivariate_normal([mu_x0,mu_y0],cov_0,1000)
    u_1 = np.random.multivariate_normal([mu_x1,mu_y1],cov_0,10000) #ANPASSEN!!!
    x_0_10000 = np.zeros(len(u_0_10000[:,0]))
    y_0_10000 = np.zeros(len(u_0_10000[:,0]))
    x_0_1000 = np.zeros(len(u_0_1000[:,0]))
    y_0_1000 = np.zeros(len(u_0_1000[:,0]))
    x_1 = np.zeros(len(u_1[:,0]))
    y_1 = np.zeros(len(u_1[:,0]))

    #selber ümstandlicher Umgang mit ROOT statt ROOT_Numpy/Pandas, da wir erst heute die Anmerkungen bekommen haben ;)

    f = ROOT.TFile("./build/eigene_zwei_populationen.root", "RECREATE")
    P_0_10000 = ROOT.TTree("P_0_10000", "P_0_10000")
    P_0_10000.Branch("x", x_0_10000, "x/D")
    P_0_10000.Branch("y", y_0_10000, "y/D")
    P_1 = ROOT.TTree("P_1", "P_1")
    P_1.Branch("x", x_1, "x/D")
    P_1.Branch("y", y_1, "y/D")
    P_0_1000 = ROOT.TTree("P_0_1000", "P_0_1000")
    P_0_1000.Branch("x", x_0_1000, "x/D")
    P_0_1000.Branch("y", y_0_1000, "y/D")
    for i in range(len(u_0_10000[:,0])):
        x_0_10000[0] = u_0_10000[i,0]
        y_0_10000[0] = u_0_10000[i,1]
        P_0_10000.Fill()
    for i in range(len(u_0_1000[:,0])):
        x_0_1000[0] = u_0_1000[i,0]
        y_0_1000[0] = u_0_1000[i,1]
        P_0_1000.Fill()
    for i in range(len(u_1[:,0])):
        x_1[0] = u_1[i,0]
        y_1[0] = u_1[i,1]
        P_1.Fill()

    f.Write()
    f.Close()

def Plotten():
    #Einlesen
    f = ROOT.TFile("./build/eigene_zwei_populationen.root", "READ")
    P_0_10000 = f.Get("P_0_10000")
    n_0_10000 = P_0_10000.GetEntries()
    x_0_10000_val = np.zeros(1, dtype=float)
    x_0_10000 = np.zeros(n_0_10000, dtype=float)
    y_0_10000_val = np.zeros(1, dtype=float)
    y_0_10000 = np.zeros(n_0_10000, dtype=float)
    P_0_10000.SetBranchAddress("x", x_0_10000_val)
    P_0_10000.SetBranchAddress("y", y_0_10000_val)
    for i in range(n_0_10000):
        P_0_10000.GetEntry(i)
        x_0_10000[i] = x_0_10000_val
        y_0_10000[i] = y_0_10000_val

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

    x_sum = np.concatenate((x_0_10000,x_1))
    y_sum = np.concatenate((y_0_10000,y_1))

    print("P1")
    print("x =",np.mean(x_1),"pm",np.std(x_1))
    print("y =",np.mean(y_1),"pm",np.std(y_1))
    print("P0")
    print("x =",np.mean(x_0_10000),"pm",np.std(x_0_10000))
    print("y =",np.mean(y_0_10000),"pm",np.std(y_0_10000))
    print("P1+P0")
    print("x =",np.mean(x_sum),"pm",np.std(x_sum))
    print("y =",np.mean(y_sum),"pm",np.std(y_sum))

    #Plotten
    fig, ax_0 = plt.subplots(1,1)
    ax_0.scatter(x_0_10000,y_0_10000,c='b',marker='.',label=r"$P_0$")
    ax_0.scatter(x_1,y_1,c='r',marker='.',label=r"$P_1$")
    ax_0.set_title("zwei Populationen")
    ax_0.set_ylabel("y")
    ax_0.set_xlabel("x")
    ax_0.legend(loc='best')
    fig.savefig("build/scatter_aufg1.png")


if __name__ == '__main__':
    aufg1()
