#dit script is het rekenhart voor de Python variant van het FTM door Jaco van der Gaast in Pascal
#Auteur: John van Dam
#Datum: 8 september 2015

import numpy as np


def delta(bergingscoefficient, drainageweerstand) :
    delta = np.exp(-1.0 /( bergingscoefficient * drainageweerstand))
    return(delta)


def omega(drainageweerstand, bergingscoefficient): 
    omega = drainageweerstand * (1.0 - delta(bergingscoefficient, drainageweerstand))
    return(omega)


def cw(drainageweerstand, qbot, hgem):
    cw = ((drainageweerstand * (qbot/10.0))*1) + hgem
    return(cw)

	
def test():
	print ("test")
	


def gws_op_t(bergingscoefficient, drainageweerstand, ht_dt,  qbot, hgem, Pt) :
    delta = np.exp(-1.0 /( bergingscoefficient * drainageweerstand))
    omega = drainageweerstand * (1.0 - np.exp(-1.0 /(bergingscoefficient * drainageweerstand)))
    cw = ((drainageweerstand * (qbot/10))*1) + hgem
    ht = cw + (delta * (ht_dt - cw)) + (omega * (Pt/100)) #de fout zou wel eens in de cw kunnen zitten, uitgaande van een vast oppervlaktewaterpeil moet voor cw of c gewoon de hgem genomen worden
    if ht<0:
	ht = ht
	afstroming = 0
    else: 
	ht =0
	afstroming = Pt/100
    return ht, afstroming, delta, omega, cw

def gws(float(bergingscoefficient), float(drainageweerstand), float(ht_dt),  float(qbot), float(hgem), float(p)):
    ht = cw(float(drainageweerstand), float(qbot), float(hgem)) + delta(float(bergingscoefficient), float(drainageweerstand))*(float(ht_dt)-cw(float(drainageweerstand), float(qbot), float(hgem)) + omega(float(drainageweerstand), float(bergingscoefficient))*(float(p)/100)
    if ht<0:
	ht = ht
	afstroming = 0
    else: 
	ht =0
	afstroming = p/100
    return ht, afstroming

