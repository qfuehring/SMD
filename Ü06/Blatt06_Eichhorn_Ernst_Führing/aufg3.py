import matplotlib.pyplot as plt
import numpy as np
import ROOT

# Make a directory for plots
import os
if not os.path.exists("./build"):
    os.makedirs("./build")

def I(p,n):
    if(p==0 or n==0):
        return 0
    else:
        a = p/(p+n)
        b = n/(p+n)
        return -a*np.log2(a) - b*np.log2(b)

def Schnitt(lab,attr, cut ,s):
    if s=='==':
        return lab[attr==cut],lab[attr!=cut]
    elif s=='!=':
        return lab[attr!=cut],lab[attr==cut]
    elif s=='>':
        return lab[attr>cut],lab[attr<=cut]
    elif s=='>=':
        return lab[attr>=cut],lab[attr<cut]
    elif s=='<':
        return lab[attr<cut],lab[attr>=cut]
    elif s=='<=':
        return lab[attr<=cut],lab[attr>cut]
    else:
        return 0,0

def E(lab,attr,cut,s):
    lab_1,lab_2 = Schnitt(lab,attr, cut, s)
    p1 = len(lab_1[lab_1==0])
    n1 = len(lab_1[lab_1==1])
    p2 = len(lab_2[lab_2==0])
    n2 = len(lab_2[lab_2==1])
    return ((p1+n1)*I(p1,n1)+(p2+n2)*I(p2,n2))/(p1+p2+n1+n2)

def Entropie(lab):
    return I(len(lab[lab==0]),len(lab[lab==1]))

def gain(lab,attr,cut,s):
    return Entropie(lab)-E(lab,attr,cut,s)

def plot(lab,attr,s,name):
    einheit = {'Temperatur':r'$\lambda_{cut}$ in °C','Wettervorhersage':'Wetterklasse $\lambda_{cut}$','Luftfeuchtigkeit':'$\lambda_{cut}$ in %','Wind':'Windstärke $\lambda_{cut}$'}
    b = max(attr)-min(attr)
    x=np.linspace(min(attr)-b/10,max(attr)+b/10,1000)
    x = np.sort(np.concatenate([x,attr]))
    g=np.zeros(len(x))
    for i in range(len(x)):
        g[i]=gain(lab,attr,x[i],s)

    fig, ax = plt.subplots(1,1)
    ax.plot(x,g,label=r"Informationsgewinn für"+name+s+r" $\lambda_{cut}$")
    ax.set_xlim(min(attr)-b/10,max(attr)+b/10)
    #ax.set_ylim(-0.1,1.1)
    ax.legend(loc="best")
    ax.set_xlabel(einheit[name])
    ax.set_title(name)
    fig.savefig("build/"+name+".png")
    print(max(g))




def aufg3():
    T,WV,LF,W,F = np.genfromtxt("aufg3.txt",unpack=True)
    lab = F
    names = {np.mean(T):'Temperatur',np.mean(WV):'Wettervorhersage',np.mean(LF):'Luftfeuchtigkeit',np.mean(W):'Wind'}

    attr = T
    plot(lab,attr,'<=',names[np.mean(attr)])
    attr = WV
    plot(lab,attr,'==',names[np.mean(attr)])
    attr = LF
    plot(lab,attr,'<=',names[np.mean(attr)])
    attr = W
    plot(lab,attr,'==',names[np.mean(attr)])





if __name__ == '__main__':
    aufg3()
