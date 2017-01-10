import numpy as np
import matplotlib.pyplot as plt
import root_numpy as rn
import root_pandas as rp


#Einlesen der Datensätze
Sig = rp.read_root("NeutrinoMC.root", "Signal_MC_Akzeptanz", columns = ['x','y','AnzahlHits'])
Bkg = rp.read_root("NeutrinoMC.root", "Untergrund_MC", columns = ['x','y','AnzahlHits'])


#Bestimmen der Trainingsdatensätze
Tr = np.concatenate((Sig[100:150],Bkg[200:250]),0)

#Generieren der Testdatensätze
Test = np.concatenate((Sig[0:100],Bkg[0:200]),0)

def Abstand(Train,Test, k):#Mitgabewerte sind der Trainings und Testdatensatz, sowie die Anzahl gesuchter nächster Nachbarn
    dall= np.zeros([Test.size, Train.size/3]) #Abstandsmatrix
    i = 0
    for T in Test:#Elementweises befüllen der Abstandsmatrix, durch berechnen der Abstände in den einzelnen Komponeneten.
        dall[3*i] = np.absolute(Train[:,0]-T[0])
        dall[3*i+1] = np.absolute(Train[:,1]-T[1])
        dall[3*i+2] = np.absolute(Train[:,2]-T[2])
        i += 1
    #print(i)
    dalli = np.argsort(dall) #Zeigt die Indizes aller Nachbarn an
    #print(dalli)
    dalli = np.delete(dalli, np.s_[k:len(dalli)], 1) #reduziert auf die k nächsten Nachbarn
    return dalli

def Einordnung(Train,Test, dalli):
    #print(pop)
    popN = np.zeros(Test.size)
    l = 0
    for j in dalli:
        if np.sum(j < Train.size/6) > np.sum(j >Train.size/6):
            popN[l] = 0 #Sig
        else:
            popN[l] = 1 #Bkg
        l += 1
    return popN


def kNN(Train,Test, k):
    return Einordnung(Train, Test, Abstand(Train, Test, k))


x = kNN(Tr, Test, 10)
print(x)
#print(Tr.size)
#print(Tr[:,0])
#print(3*len(Test[0]))
