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

#dit script is de Python variant van het FTM door Jaco van der Gaast in Pascal
#Auteur: John van Dam
#Datum: 17 augustus 2015
#voor het laatst bijgewerkt op 8 september 2015


 

def maak_plotje(x2, y2):
    nummer_meteostation = 310
    bestandspad='/home/john/ftm/ftm/ftm/data/'
    bestandspad_plot='/home/john/ftm/ftm/ftm/static/'

    x= str(x2)
    y= str(y2)

###################################################################
#hier begint dan het programma

#voorbewerkte meteo inlezen in een pandas dataframe en dan wegschrijven naar een numpy array
    for i in [nummer_meteostation]:
        meteobestand_in = bestandspad + 'Waterbalans_METEO'+str(i)+'.csv'
        dfNettoNeerslag = pd.read_csv(meteobestand_in, header=None, skiprows=1, names = ['datum', 'NN1', 'NN2' ], delimiter =',', parse_dates=[0])
    array_neerslagoverschot = dfNettoNeerslag['NN1'].values
    lengte = len(array_neerslagoverschot) #arrays die je samen wilt gebruiken in een tijdserie moeten even lang zijn, anders gaat er van alles mis


#bodemdata afkomstig uit de QGIS puntenwolk inlezen in een pandas dataframe en dan wegschrijven naar een numpy arrays
    #dfBodem=pd.read_csv(bodembestand, header=None, delimiter =',', names = ['#runn', 'al', 'hgem', 'drainw', 'berg', 'qbot' ])
    array_bergingscoefficient = np.array([float(raster_q(bestandspad + "bergcoef-nzv.tif", x, y))])
    array_drainweerstand = np.array([float(raster_q(bestandspad + "drainw-nzv.tif", x, y))])
    array_qbot = np.array([float(raster_q(bestandspad + "kwel-nzv.tif", x, y))])
    array_hgem = np.array([float(raster_q(bestandspad + "ontwbas-nzv.tif", x, y))*-1.0])


#array grondwaterstand voorbereiden en vullen met nullen, zodoende begint de berekening altijd op 0 cm-mv en gaat python niet klagen over de positieaanduiding in een nog niet bestaande array
    array_grondwaterstand = np.zeros(shape = (2, lengte), order='C')

#door de functie gws_op_t uit het rekenhart aan te roepen en met behulp van een for loop uit te voeren wordt voor iedere dag de grondwaterstand berekend met de netto neerslag en de bodemdata, tegelijk wordt de oppervlakkige afstroming berekend, maar dit laatste is nog in ontwikkeling
    for i in range(1,lengte):
        array_grondwaterstand[0,i] = gws_op_t(array_bergingscoefficient[0], array_drainweerstand[0], array_grondwaterstand[0, (i-1)], array_qbot[0], array_hgem[0], array_neerslagoverschot[i])[0]
        array_grondwaterstand[1,i] = gws_op_t(array_bergingscoefficient[0], array_drainweerstand[0], array_grondwaterstand[0, (i-1)], array_qbot[0], array_hgem[0], array_neerslagoverschot[i])[1]


###################################################################
#hieronder wordt het outputbestand met de grondwaterstanden en de oppervlakkige afstroming gemaakt

#startdatum en dates zijn variabelen die in het verloop van het programma gebruikt worden om een array of serie om te kunnen zetten naar een dataframe met datums
    startdatum = dfNettoNeerslag.ix[0, 'datum']
    dates = pd.date_range(startdatum, periods=lengte)
    
#dfGWS en serafstroming worden met behulp van pd.Series omgezet in een tijdserie waarbij de grondwaterstanden en afstroming een datum hebben
    dfGWS = pd.Series(array_grondwaterstand[0], index=dates)
    serafstroming = pd.Series(array_grondwaterstand[1], index=dates)
    
#de net gemaakte tijdseries worden omgezet in een dataframe, dat is gemakkelijker met pandas te hanteren voor wegschrijven naar csv en plotten
    dfGrondwaterstanden = dfGWS.to_frame(name = 'Grondwaterstanden')
    dfAfstroming = serafstroming.to_frame(name = 'Afstroming')
#het grondwaterframe en het afstromingsframe worden samengevoegd tot een dataframe, waardoor beide series in een csv-bestand weggezet kunnen worden
#print str(datetime.now()) + 'dataframes samenvoegen en wegschrijven naar een csv'
    dfOutput = pd.merge(dfGrondwaterstanden, dfAfstroming,how='inner', on=None, left_on=None, right_on=None, left_index=True, right_index=True)
#variabele bestandsnaam voor het grondwaterstandenbestand, deze is afhankelijk van het meteostationsnummer om bij verschillende tijdseries niet over de vorige heen te schrijven
    #GWSbestand_uit = 'GWS_out_'+str(nummer_meteostation)+'.csv'
    #dfOutput.to_csv(GWSbestand_uit,  index=True, sep=',')
#print str(datetime.now()) + 'GxG berekenen'
#met behulp van de module GxG.py worden de GHG en GLG berekend en voor het plotten in een dataframe met datums gestopt, anders kan er geen horizontale lijn voor een getal geplot worden
    GHG = GHG_berekening(dfGWS, dates, array_neerslagoverschot, nummer_meteostation)[0]
    GLG = GLG_berekening(dfGWS, dates, array_neerslagoverschot, nummer_meteostation)[0]
    dfGHGs = GHG_berekening(dfGWS, dates, array_neerslagoverschot, nummer_meteostation)[1]
    dfGLGs = GLG_berekening(dfGWS, dates, array_neerslagoverschot, nummer_meteostation)[1]
    
    gt = GT(GHG[0],GLG[0])[1]

#print str(datetime.now()) + 'plotten'
###################################################################
#plotje maken van de grondwaterstanden en opslaan

    return plot_buf(dfGWS, dfGHGs, dfGLGs, gt, nummer_meteostation, x2, y2), gt, GHG[0], GLG[0]
#print str(datetime.now()) + 'print de gt'
#via de terminal de grondwatertrap en het nummer van die grondwatertrap printen
    #print GT(GHG[0],GLG[0])
    #print str(datetime.now()) + 'einde'




def FTM(opdrachtparameters, meteo, naam):
    spam = subprocess.check_output(["./FTM", opdrachtparameters, meteo, naam])
    return spam


def supersnel_ftm(x2, y2): #gebruikmakend van Jaco's ftm in Pascal
    #varabelen
    werkdirectory = '/home/john/ftm/ftm/ftm/data'
    bestandspad_plot='/home/john/ftm/ftm/ftm/static/'
    naam = str(x2)+'_'+str(y2)
    meteobestand = 'METEO280.txt'

    os.chdir(werkdirectory)

    output_file = open(naam + 'invoer.txt', 'w')
    line = '%s\n' % ("#runn        al     hgem  drainw    berg    qbot  ")
    unicode_line = line.encode('utf-8')
    output_file.write(unicode_line)
    runn = 1
    al = 365
    hgem = float(raster_q("/home/john/ftm/ftm/ftm/data/ontwbas-nzv.tif", x2, y2)) * -1
    drainw = float(raster_q("/home/john/ftm/ftm/ftm/data/drainw-nzv.tif", x2, y2))
    berg = float(raster_q("/home/john/ftm/ftm/ftm/data/bergcoef-nzv.tif", x2, y2))# f['bergcoef10'] / 100
    qbot = float(raster_q("/home/john/ftm/ftm/ftm/data/kwel-nzv.tif", x2, y2)) #f['kwel10'] / 10
    line = '%8.0f%8.0f%8.0f%8.0f%8.3f%8.3f\n' % (runn,al,hgem,drainw,berg,qbot)
    unicode_line = line.encode('utf-8')
    output_file.write(unicode_line)    
    output_file.close()

    FTM(naam + 'invoer.txt', meteobestand, naam)


    # GHG en GLG uit textbestand halen 
    fileinput = open(naam + 'gwlstatistics.txt', 'r')
    fileinput.readline()
    fileinput.readline()
    #for line in fileinput:
    #print fileinput.read(4),
    fileinput.read(4),
    GHG = fileinput.read(8)
    fileinput.readline()
    fileinput.readline()
    fileinput.read(4),
    GLG = fileinput.read(8)
    fileinput.close()


    fileinput = open(naam + 'gwl.txt', 'r')
    #print(fileinput.readline()),
    #print(fileinput.readline())
    fileinput.readline()
    fileinput.readline()

    #print fileinput.readline(8),
    dagList = [] 
    maandList = []
    jaarList = []
    datumList = []
    gwstList = []
    GHGList = []
    GLGList = []
    for line in fileinput:
         dagList.append(int(line[0:2]))

         if int(line[6:8]) < 20:
             jaarList.append(int(line[6:8])+2000)
         else:
            jaarList.append(int(line[6:8])+1900)
         if int(line[6:8]) < 20:
             datum = date(int(line[6:8])+2000,int(line[3:5]),int(line[0:2]))         
         else:
             datum = date(int(line[6:8])+1900,int(line[3:5]),int(line[0:2]))
         datumList.append(datum)
         gwstList.append(float(line[9:16]))
         GHGList.append(float(GHG))
         GLGList.append(float(GLG))
    fileinput.close()

    #print gwstList
    # x and y definieren
    x = datumList
    ygrwst = gwstList
    yGHG = GHGList
    yGLG = GLGList
    
    # Create plots with pre-defined labels. gebruik makend van matplotlib pyplot
    plt.plot(x, ygrwst, 'b', label='Grondwaterstand')
    plt.plot(x, yGHG, 'r', label='GHG')
    plt.plot(x, yGLG, 'g', label='GLG')

    plt.legend(loc='lower center', shadow=True, fontsize='x-large')

# Titels definieren
    plt.xlabel('Tijd')
    plt.ylabel('Grondwaterstand (cm t.o.v. mv)')
    plt.title('Tijdstijghoogtelijn')
    plt.grid(True)
# without the line below, the figure won't show
    plotnaam='Grondwaterstanden_'+str(x2)+'_'+str(y2)+'.png'
    pylab.savefig(bestandspad_plot + plotnaam, bbox_inches='tight')
    pylab.close()
    ploatje=plotnaam

    return ploatje, x2, y2



def maak_plotje2(x2, y2, startdatum, einddatum, resultaat):
    nummer_meteostation = 280
    bestandspad='/home/john/ftm/ftm/ftm/data/'
    bestandspad_plot='/home/john/ftm/ftm/ftm/static/'
    
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
    dates = pd.date_range(startdatum, periods=lengte)
    
    #dfGWS en serafstroming worden met behulp van pd.Series omgezet in een tijdserie waarbij de grondwaterstanden en afstroming een datum hebben
    dfGWS = pd.Series(array_grondwaterstand[0], index=dates)
    serafstroming = pd.Series(array_grondwaterstand[1], index=dates)
    #print str(datetime.now()) + 'frames maken van grondwaterstanden en afstroming'
    #de net gemaakte tijdseries worden omgezet in een dataframe, dat is gemakkelijker met pandas te hanteren voor wegschrijven naar csv en plotten
    dfGrondwaterstanden = dfGWS.to_frame(name = 'Grondwaterstanden')
    dfAfstroming = serafstroming.to_frame(name = 'Afstroming')
    #het grondwaterframe en het afstromingsframe worden samengevoegd tot een dataframe, waardoor beide series in een csv-bestand weggezet kunnen worden

    dfOutput = pd.merge(dfGrondwaterstanden, dfAfstroming,how='inner', on=None, left_on=None, right_on=None, left_index=True, right_index=True)
    #variabele bestandsnaam voor het grondwaterstandenbestand, deze is afhankelijk van het meteostationsnummer om bij verschillende tijdseries niet over de vorige heen te schrijven
    #GWSbestand_uit = 'GWS_out_'+str(nummer_meteostation)+'.csv'
    #dfOutput.to_csv(GWSbestand_uit,  index=True, sep=',')

    #met behulp van de module GxG.py worden de GHG en GLG berekend en voor het plotten in een dataframe met datums gestopt, anders kan er geen horizontale lijn voor een getal geplot worden
    GHG = GHG_berekening(dfGWS, dates, array_neerslagoverschot, nummer_meteostation)[0]
    GLG = GLG_berekening(dfGWS, dates, array_neerslagoverschot, nummer_meteostation)[0]
    dfGHGs = GHG_berekening(dfGWS, dates, array_neerslagoverschot, nummer_meteostation)[1]
    dfGLGs = GLG_berekening(dfGWS, dates, array_neerslagoverschot, nummer_meteostation)[1]
    
    gt = GT(GHG[0],GLG[0])[1]

    ###################################################################
    #plotje maken van de grondwaterstanden en opslaan
    if resultaat == 'plot':
        return plot_buf(dfGWS, dfGHGs, dfGLGs, gt, nummer_meteostation, x2, y2), gt, GHG[0],GLG[0]
    elif resultaat == 'csv':
        return dfGrondwaterstanden
