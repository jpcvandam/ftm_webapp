#een simpel script om de verdamping te berekenen op basis van de voorspellingen van NOAA
#auteur: John van Dam
#datum: 25 januari 2016

import numpy as np

def ET0(DELTA, Rn, G, GAMMA, T, e_s, e_a, u2): #verdamping volgens Pennman-Montheit
    ET0=(0.408*DELTA*(Rn - G) + GAMMA * (900.0/(T + 273.0)) * u2 * (e_s - e_a))/(DELTA + GAMMA *(1.0 + 0.34* u2))
    return(ET0)


def u2(uz, z): #de windsnelheid op 2 m boven maaiveld als functie van de windsnelheid op een andere hoogte en die hoogte, met uz in [m/s] en z in [m]
    u2 = uz * (4.87/(np.log(67.8*z - 5.42)))
    return(u2)


def DELTA(T): #de helling van de dampspanningskromme als functie van de temperatuur in [graden C]
    DELTA = (4098.0*(0.6108*np.exp((17.27*T)/(T + 237.3))))/((T + 237.3)**2)
    return(DELTA)


def eT(T): #dampspanningskromme als functie van T in [graden C]
    eT = 0.6108 * np.exp((17.27 * T)/(T + 237.3))
    return eT


def e_ad(Tdew): #actuele dampspanning als functie van het dauwpunt in [graden C]
    e_a = 0.6108 * np.exp((17.27 * Tdew)/(Tdew + 237.3))
    return e_a

