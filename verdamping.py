#een simpel script om de verdamping te berekenen op basis van de voorspellingen van NOAA
#auteur: John van Dam
#datum: 25 januari 2016

import numpy as np

def ET0(DELTA, Rn, G, GAMMA, T, e_s, e_a, u2):
    ET0=(0.408*DELTA*(Rn - G) + GAMMA * (900.0/(T + 273.0)) * u2 * (e_s - e_a))/(DELTA + GAMMA *(1.0 + 0.34* u2))
    return(ET0)

def u2(uz, z):
    u2 = uz * (4.87/(np.log(67.8*z - 5.42)))
    return(u2)

def DELTA(T):
    DELTA = (4098.0*(0.6108*np.exp((17.27*T)/(T + 237.3))))/((T + 237.3)**2)
    return(DELTA)
