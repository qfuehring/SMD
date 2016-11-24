def aufg1_c():

    #aufgabenteil c (nach der Anleitung aus der VL)

    #erzeuge gleichverteilte u_1 und u_2
    u_1 = np.random.rand()
    u_2 = np.random.rand()

    #umformen und summieren
    v_1 = 2 * u_1 - 1
    v_2 = 2 * u_2 - 1
    s = v_1 **2 + v_2 **2

    #die s mit Betrag < 1 auswählen
    if s >= 0:
        pass

    #bilde x_1 und x_2
    x_1 = np.sqrt(s) * np.cos(np.arctan(v_2/v_1)) * np.sqrt((-2/s) * np.log(s))
    x_2 = np.sqrt(s) * np.sin(np.arctan(v_2/v_1)) * np.sqrt((-2/s) * np.log(s))

    #Normalverteilung auf Energien übertragen
    #Anzahl Hits N in Normalverteilung = Energie (E) * Standardabweichung (2 * E) + Erwartungswert (10 * E)
    #Aussortieren und Runden auf 0 Nachkommastellen

    N = 2 * (E**2) + 10 * E
    if N < 0:
        pass
    round(N, 0)
