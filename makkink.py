#module om de Makkink referentieverdamping te berekenen
#Auteur: John van Dam
#Datum: 05/01/2016

import numpy as np

def verzadigingsdampspanning(T):
    e_s = 0.61*np.exp(17.3*T/(237+T))
    return e_s


def hellingVerzadigingsdampspanning(T):
    s = (4100*verzadigingsdampspanning(T))/(237+T)**2
    return s


def makkink():