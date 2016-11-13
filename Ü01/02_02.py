import ROOT as r
import numpy as np
import matplotlib.pyplot as plt
# Make a directory for plots
import os
if not os.path.exists("./build"):
    os.makedirs("./build")




#Daten einlesen
d, m = np.genfromtxt("Daten.txt", unpack = True)

#Canvas initialisieren
myCan = r.TCanvas("myCan","myCan",800,600)
myCan.Divide(2,3)

myCan2 = r.TCanvas("myCan2","myCan2",800,600)

#Hist einlesen
myHist1 = r.TH2F("myHist1","myHist1",nbinsx=5,nbinsy=5)
myHist2 = r.TH2F("myHist2","myHist2",nbinsx=10,nbinsy=10)
myHist3 = r.TH2F("myHist3","myHist3",nbinsx=15,nbinsy=15)
myHist4 = r.TH2F("myHist4","myHist4",nbinsx=20,nbinsy=20)
myHist5 = r.TH2F("myHist5","myHist5",nbinsx=30,nbinsy=30)
myHist6 = r.TH2F("myHist6","myHist6",nbinsx=50,nbinsy=50)


for i in r.shape[0]:
    myHist1.Fill(d[i],m[i])
    myHist2.Fill(d[i],m[i])
    myHist3.Fill(d[i],m[i])
    myHist4.Fill(d[i],m[i])
    myHist5.Fill(d[i],m[i])
    myHist6.Fill(d[i],m[i])

#Draw Canvas
myCan.cd(1,1)
myHist1.Draw()
myCan.cd(1,2)
myHist2.Draw()
myCan.cd(1,3)
myHist3.Draw()
myCan.cd(2,1)
myHist4.Draw()
myCan.cd(2,2)
myHist5.Draw()
myCan.cd(2,3)
myHist6.Draw()
myCan.Update()
myCan.Draw()
myCan.SaveAs("./build/2a.png")
myCan.Close()


##############
# Aufgabenteil c
#############
myCan2 = r.TCanvas("myCan2","myCan2",800,600)
myCan2.Divide(2,3)

cHist1 = r.TH1F("cHist1","cHist1",5)
cHist2 = r.TH1F("cHist2","cHist2",10)
cHist3 = r.TH1F("cHist3","cHist3",15)
cHist4 = r.TH1F("cHist4","cHist4",20)
cHist5 = r.TH1F("cHist5","cHist5",30)
cHist6 = r.TH1F("cHist6","cHist6",50)

#random numbers
random_generator = r.TRandom3()
random_numbers = [random_generator.Integer(100) for i in range(10000)]

for random_number in random_numbers:
    cHist1.Fill(np.log(random_number))
    cHist2.Fill(np.log(random_number))
    cHist3.Fill(np.log(random_number))
    cHist4.Fill(np.log(random_number))
    cHist5.Fill(np.log(random_number))
    cHist6.Fill(np.log(random_number))

myCan2.cd(1,1)
cHist1.Draw()
myCan2.cd(1,2)
cHist2.Draw()
myCan2.cd(1,3)
cHist3.Draw()
myCan2.cd(2,1)
cHist4.Draw()
myCan2.cd(2,2)
cHist5.Draw()
myCan2.cd(2,3)
cHist6.Draw()

myCan2.Draw()
myCan2.SaveAs("./build/2c.png")
myCan2.Close()
