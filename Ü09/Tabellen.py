import numpy as np

def Tabelle(spalten,errors=None,pfad="",headline="",caption="",label="",form=""):
    if pfad == "":
        pfad = "Tabelle.txt"
        print("Kein Pfad gegeben")
        print("Tabelle wird gespeichert in Tabelle.txt")
        print("!!!!!!!!!!!!!!!!")
    if errors == None:
        errors = np.zeros([len(spalten),len(spalten[0])])
    #Umgebung
    s = "\\begin{table}"
    s = s + "\n\\caption{" + caption + ".}"
    s = s + "\n\\centering"
    s = s + "\n\\label{" + label + "}"
    #Spaltenformat
    s = s + "\n\\begin{tabular}{ "
    for i in range(len(spalten)):
        if i < len(form) and form[i]!="":
            s = s + form[i]
        else:
            s = s + "S"
    s = s + "}"
    #Überschriften
    s = s + "\n\\toprule\n"
    for i in range(len(spalten)):
        if i < len(headline):
            s = s + headline[i]
        if i < len(spalten)-1:
            s = s + "&\t"
        elif i == len(spalten)-1:
            s = s + "\\\\"
    #Inhalt
    s = s + "\n\\midrule"
    for i in range(len(spalten[0])):
        s = s + "\n"
        for j in range(len(spalten)):
        #    if not np.isnan(spalten[j][i]): #NaN durch leere Felder ersetzen
            s = s  + str(spalten[j][i])
            if errors[j][i] != 0:   #Fehler hinzufügen
                s = s + "(" + str(int(errors[j][i])) + ")"
            if j < len(spalten)-1:
                s = s + "&\t"
            elif j == len(spalten)-1:
                s = s + "\\\\"
    s = s + "\n\\bottomrule\n\\end{tabular}\n\\end{table}"
    txt = open(pfad,"w")
    txt.write(s)
    txt.close()

def cut_decimal(alt): #benötigt numpy array
    neu = []
    for i in range(len(alt)):
        if np.isnan(alt[i]):
            neu = neu + [np.nan]
        else:
            neu = neu + [int(alt[i])]
    return neu
