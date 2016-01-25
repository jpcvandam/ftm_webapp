#een simpel script om de verdamping te berekenen op basis van de voorspellingen van NOAA
#auteur: John van Dam
#datum: 25 januari 2016

import numpy as np

def u2(uz, z): #de windsnelheid op 2 m boven maaiveld als functie van de windsnelheid op een andere hoogte en die hoogte, met uz in [m/s] en z in [m]
    u2 = uz * (4.87/(np.log(67.8*z - 5.42)))
    return(u2)


def DELTA(T): #de helling van de dampspanningskromme als functie van de temperatuur in [graden C]
    DELTA = (4098.0*(0.6108*np.exp((17.27*T)/(T + 237.3))))/((T + 237.3)**2)
    return(DELTA)


def eT(T): #dampspanningskromme als functie van T in [graden C]
    eT = 0.6108 * np.exp((17.27 * T)/(T + 237.3))
    return eT


def e_a(Tdew): #actuele dampspanning als functie van het dauwpunt in [graden C]
    e_a = 0.6108 * np.exp((17.27 * Tdew)/(Tdew + 237.3))
    return e_a


def e_s(Tmin, Tmax):
    e_s = (eT(Tmax)-eT(Tmin))/2
    return e_s


def e_aRhminmax (RH_mean, Tmin, Tmax): #actuele dampspanning als functie van gemiddelde luchtvochtigheid [%], maximum en minimum temperatuur in [graden C] 
    e_a = RH_mean/100.0*((eT(Tmax)-eT(Tmin))/2)
    return e_a


def Rn(dswrfsfc, dlwrfsfc, uswrfsfc, ulwrfsfc):
    #'dswrfsfc', # surface downward short-wave radiation flux [w/m^2]
    #'dlwrfsfc', # surface downward long-wave rad. flux [w/m^2]
    #'uswrfsfc', # surface upward short-wave radiation flux [w/m^2] 
    #'ulwrfsfc', # surface upward long-wave rad. flux [w/m^2]
    Rn = dswrfsfc + dlwrfsfc - uswrfsfc - ulwrfsfc
    return Rn


def ET0(dswrfsfc, dlwrfsfc, uswrfsfc, ulwrfsfc, T, Tmin, Tmax, Tdew, uz, z): #verdamping volgens Pennman-Montheit
    ET0=(0.408*DELTA(T-273.15)*(Rn(dswrfsfc, dlwrfsfc, uswrfsfc, ulwrfsfc) - 0) + 0.066 * (900.0/(T -273.15 + 273.0)) * u2(uz, z) * (e_s(Tmin, Tmax) - e_a(Tdew - 273.15)))/(DELTA(T) + 0.066 *(1.0 + 0.34* u2(uz, z)))
    return(ET0)


