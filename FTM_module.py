#deze module wordt aangeroepen vanuit het views.py bestand
#auteur: John van Dam
#datum: 9 november 2015


##imports om te rekenen
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
from datetime import datetime, timedelta, date
import subprocess
import os
import matplotlib.dates as mdates
from FTM_rekenhart import *
from GxG import *
from GT import GT
from plot_GWS import *
from raster import raster_q
from sql_lezer import meteo_query
from ftm.settings import DATA_ROOT, STATIC_ROOT

#dit script is de Python variant van het FTM door Jaco van der Gaast in Pascal
#Auteur: John van Dam
#Datum: 17 augustus 2015
#voor het laatst bijgewerkt op 8 september 2015


 
def maak_plotje2(x2, y2, startdatum, einddatum, resultaat):
    nummer_meteostation = 280
    bestandspad= DATA_ROOT 
    
    x= str(x2)
    y= str(y2)
    
    startdatum = str(startdatum) #'2015-01-01'
    einddatum = str(einddatum)#'2015-11-08'

    ###################################################################
    #hier begint dan het programma
    datum=meteo_query(nummer_meteostation, startdatum, einddatum)[0]
    neerslag=meteo_query(nummer_meteostation, startdatum, einddatum)[1]
    verdamping=meteo_query(nummer_meteostation, startdatum, einddatum)[2]
    lengte = len(neerslag) #arrays die je samen wilt gebruiken in een tijdserie moeten even lang zijn, anders gaat er van alles mis
    array_neerslag1 = np.array(neerslag) 
    array_verdamping1 = np.array(verdamping) #np.zeros(shape = (1, lengte), order='C')
    datum_array = np.array(datum)
    array_neerslagoverschot = np.zeros(shape = (1, lengte), order='C')
    
    startdatum = datum_array[0]
    einddatum = datum_array[lengte-1]
    
    for i in range(0, lengte):
        array_neerslagoverschot[0][i] = int(array_neerslag1[i]) - int(array_verdamping1[i])
    

    #voorbewerkte meteo inlezen in een pandas dataframe en dan wegschrijven naar een numpy array
   

    #bodemdata afkomstig uit de QGIS puntenwolk inlezen in een pandas dataframe en dan wegschrijven naar een numpy arrays
    
    array_bergingscoefficient = np.array([float(raster_q(bestandspad + "bergcoef-nzv.tif", x, y))])
    array_drainweerstand = np.array([float(raster_q(bestandspad + "drainw-nzv.tif", x, y))])
    array_qbot = np.array([float(raster_q(bestandspad + "kwel-nzv.tif", x, y))])
    array_hgem = np.array([float(raster_q(bestandspad + "ontwbas-nzv.tif", x, y))*-1.0])


    #array grondwaterstand voorbereiden en vullen met nullen, zodoende begint de berekening altijd op 0 cm-mv en gaat python niet klagen over de positieaanduiding in een nog niet bestaande array
    array_grondwaterstand = np.zeros(shape = (2, lengte), order='C')
    
    #door de functie gws_op_t uit het rekenhart aan te roepen en met behulp van een for loop uit te voeren wordt voor iedere dag de grondwaterstand berekend met de netto neerslag en de bodemdata, tegelijk wordt de oppervlakkige afstroming berekend, maar dit laatste is nog in ontwikkeling
    for i in range(1,lengte):
        array_grondwaterstand[0,i] = gws_op_t(array_bergingscoefficient[0], array_drainweerstand[0], array_grondwaterstand[0, (i-1)], array_qbot[0], array_hgem[0], array_neerslagoverschot[0][i])[0]
        array_grondwaterstand[1,i] = gws_op_t(array_bergingscoefficient[0], array_drainweerstand[0], array_grondwaterstand[0, (i-1)], array_qbot[0], array_hgem[0], array_neerslagoverschot[0][i])[1]

    
    ###################################################################
    #hieronder wordt het outputbestand met de grondwaterstanden en de oppervlakkige afstroming gemaakt

    #startdatum en dates zijn variabelen die in het verloop van het programma gebruikt worden om een array of serie om te kunnen zetten naar een dataframe met datums
    #startdatum = dfNettoNeerslag.ix[0, 'datum']
    dates = datum_array #pd.date_range(startdatum, periods=lengte)
    
    #dfGWS en serafstroming worden met behulp van pd.Series omgezet in een tijdserie waarbij de grondwaterstanden en afstroming een datum hebben
    dfGWS = pd.Series(array_grondwaterstand[0], index=dates)
    serafstroming = pd.Series(array_grondwaterstand[1], index=dates)
    
    #de net gemaakte tijdseries worden omgezet in een dataframe, dat is gemakkelijker met pandas te hanteren voor wegschrijven naar csv en plotten
    dfGrondwaterstanden = dfGWS.to_frame(name = 'Grondwaterstanden')
    dfAfstroming = serafstroming.to_frame(name = 'Afstroming')
    #het grondwaterframe en het afstromingsframe worden samengevoegd tot een dataframe, waardoor beide series in een csv-bestand weggezet kunnen worden

    dfOutput = pd.merge(dfGrondwaterstanden, dfAfstroming,how='inner', on=None, left_on=None, right_on=None, left_index=True, right_index=True)
    #variabele bestandsnaam voor het grondwaterstandenbestand, deze is afhankelijk van het meteostationsnummer om bij verschillende tijdseries niet over de vorige heen te schrijven
    

    #met behulp van de module GxG.py worden de GHG en GLG berekend en voor het plotten in een dataframe met datums gestopt, anders kan er geen horizontale lijn voor een getal geplot worden
    GHG = GHG_berekening(dfGWS, dates, lengte)[0]
    GLG = GLG_berekening(dfGWS, dates, lengte)[0]
    dfGHGs = GHG_berekening(dfGWS, dates, lengte)[1]
    dfGLGs = GLG_berekening(dfGWS, dates, lengte)[1]
    
    gt = GT(GHG[0],GLG[0])[1]

    ###################################################################
    #plotje maken van de grondwaterstanden en opslaan
    if resultaat == 'plot':
        return plot_buf(dfGWS, dfGHGs, dfGLGs, gt, nummer_meteostation, x2, y2), gt, GHG[0],GLG[0], startdatum.date(), einddatum.date()
    elif resultaat == 'csv':
        return dfGrondwaterstanden, startdatum, einddatum
