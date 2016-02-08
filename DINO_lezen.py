#dit pythonscript gaat de dino bestanden selectief inlezen.
#dat gaat het doen doordat de bestanden en hun headers uit blokken bestaan die met behulp van witregels gescheiden zijn.
#auteur: John van Dam
#datum: 01-02-2016

#opbouw bestanden
#blok 1: titel en andere meuk, 6 regels, 1 witregel
#blok 2: verklaring woorden, 3 regels, 1 witregel
#blok 3: Beschrijving filters, variabel aantal regels, 2 witregels
#blok 4: de tijdreeks, variabele lengte DIT WIL IK INLEZEN


#oplossing 1: tel het aantal regels tot aan de werkelijke tijdreeks en laat pandas het werk doen.

#de bestandjes met *_0.csv als extensie bevatten alleen de stand ten opzichte van maaiveld, die gebruiken.
#De opbouw van deze jongens is:
#blok 1, algemene informatie over de aanvraag, gevolgd door twee witregels
#blok 2, variabel aantal regels over herinmetingen van de peilbuis + de coordinaten van de peilbuis, gevolgd door een witregel
#blok 3, de tijdserie


import os, sys
import pandas as pd
from dateutil import parser
from pandas.tslib import parse_date
import matplotlib.pyplot as plt
import pylab
from GxG_meet import GLG_berekening, GHG_berekening

bestandspad = "/home/john/Documenten/Afstuderen_Acacia_water/Data/dino_gedeelte_NZV/Grondwaterstanden_Put/"
os.chdir(bestandspad)
infile = "B07A0112001_1.csv" #bestandsnaam met eventueel een pad ervoor

infiles = ["B03D0016001_1.csv", "B03D0016001_1.csv", "B03D0071001_1.csv", "B03G0090001_1.csv", "B03G0091001_1.csv", "B07A0021001_1.csv", "B07A0108001_1.csv", "B07A0112001_1.csv", "B07A0112002_1.csv", "B07A0120001_1.csv", "B07A0121001_1.csv", "B07A0122001_1.csv", "B07A0124001_1.csv", "B07A0125001_1.csv", "B07A0127001_1.csv", "B07A0128001_1.csv", "B07A0130001_1.csv", "B07A0131001_1.csv", "B07A0133001_1.csv", "B07A0134001_1.csv", "B07A0135001_1.csv", "B07A0136001_1.csv", "B07A0140001_1.csv", "B07A0142001_1.csv", "B07A0147001_1.csv", "B07A0924001_1.csv", "B07A0945001_1.csv", "B07A0945002_1.csv", "B07A0946001_1.csv", "B07A0947001_1.csv", "B07A0948002_1.csv", "B07A0949001_1.csv", "B07A0956001_1.csv", "B07A0957001_1.csv", "B07A0981001_1.csv", "B07A0982001_1.csv", "B07B0019001_1.csv", "B07B0019002_1.csv", "B07B0056001_1.csv", "B07B0119001_1.csv", "B07B0130001_1.csv", "B07B0131001_1.csv", "B07B0133001_1.csv", "B07B0135001_1.csv", "B07B0136001_1.csv", "B07B0137001_1.csv", "B07B0138001_1.csv", "B07B0139001_1.csv", "B07B0141001_1.csv", "B07B1108001_1.csv", "B07B1109001_1.csv", "B07E0029001_1.csv", "B07E0030001_1.csv", "B07E0042001_1.csv", "B07E0084001_1.csv", "B07E0085001_1.csv", "B07E0087001_1.csv", "B07E0088001_1.csv", "B07E0089001_1.csv",  "B07E0094001_1.csv", "B07E0095001_1.csv", "B07E0097001_1.csv", "B07E0098001_1.csv", "B07E0101001_1.csv", "B07E1137001_1.csv", "B03D0071001_1.csv", "B03G0090001_1.csv", "B03G0091001_1.csv", "B07A0021001_1.csv", "B07A0108001_1.csv", "B07A0112001_1.csv", "B07A0112002_1.csv", "B07A0120001_1.csv", "B07A0121001_1.csv", "B07A0122001_1.csv", "B07A0124001_1.csv", "B07A0125001_1.csv", "B07A0127001_1.csv", "B07A0128001_1.csv", "B07A0130001_1.csv", "B07A0131001_1.csv", "B07A0133001_1.csv", "B07A0134001_1.csv", "B07A0135001_1.csv", "B07A0136001_1.csv", "B07A0140001_1.csv", "B07A0142001_1.csv", "B07A0147001_1.csv", "B07A0924001_1.csv", "B07A0945001_1.csv", "B07A0945002_1.csv", "B07A0946001_1.csv", "B07A0947001_1.csv", "B07A0948002_1.csv", "B07A0949001_1.csv", "B07A0956001_1.csv", "B07A0957001_1.csv", "B07A0981001_1.csv", "B07A0982001_1.csv", "B07B0019001_1.csv", "B07B0019002_1.csv", "B07B0056001_1.csv", "B07B0119001_1.csv", "B07B0130001_1.csv", "B07B0131001_1.csv", "B07B0133001_1.csv", "B07B0135001_1.csv", "B07B0136001_1.csv", "B07B0137001_1.csv", "B07B0138001_1.csv", "B07B0139001_1.csv", "B07B0141001_1.csv", "B07B1108001_1.csv", "B07B1109001_1.csv", "B07E0029001_1.csv", "B07E0030001_1.csv",  "B07E0042001_1.csv", "B07E0084001_1.csv", "B07E0085001_1.csv", "B07E0087001_1.csv", "B07E0088001_1.csv", "B07E0089001_1.csv", "B07E0094001_1.csv", "B07E0095001_1.csv", "B07E0097001_1.csv", "B07E0098001_1.csv", "B07E0101001_1.csv", "B07E1137001_1.csv", "B07E0031001_1.csv", "B07E0031001_1.csv", "B07E0092001_1.csv", "B07E0092001_1.csv"]



def ruw_csv(infile): #tel hoeveel regels de header van het dino csv-file heeft, zodat deze overgeslagen kunnen worden
    cntwhite = 0
    cntline = 0

    while not cntwhite ==4:
        with open(infile, 'r') as fileinput:
            for line in fileinput:     
                if line == "\r\n" and cntwhite <= 4:
                    cntwhite+=1 #als er een lege regel aangetroffen is, betekend dit dat er een blok voorbij is wat eigenlijk ingelezen moet worden
                elif len(line)>= 1 and cntwhite <= 3:
                    cntline+=1
                elif cntwhite <= 4 or cntline <= 20:
                    overslaan = cntwhite + cntline
                    print overslaan
                    fileinput.close()
                    break
    return overslaan        

def plot(df, bestandspad, plotnaam): #plot alleen de gemeten reeks
    df.plot()
    plt.xlabel('Tijd')
    plt.title('Tijdstijghoogtelijn' + plotnaam)
    pylab.savefig(bestandspad + plotnaam + '.png')#, bbox_inches='tight')
    ax = pylab.gca()
    ax.set_ylabel('$cm-mv$')
    ax.text(2, 6,  plotnaam, fontsize=15)
    pylab.close()


def plot2(df, df2, bestandspad, plotnaam): #plot zowel de gemeten als de met het FTM berekende reeks
    ax = df2.plot(label='berekend', color = 'g')
    df.plot(ax=ax, label='gemeten', color = 'b') #df2.plot(label='berekend')
    #df.plot(label='gemeten')
    plt.xlabel('Tijd')
    plt.title('Tijdstijghoogtelijn ' + plotnaam[9:])
    pylab.savefig(bestandspad + plotnaam + 'f.png')#, bbox_inches='tight')
    ax = pylab.gca()
    ax.set_ylabel('$cm-mv$')
    ax.text(2, 6,  plotnaam, fontsize=15)
    pylab.close()


if len(sys.argv) == 2:
    command = sys.argv[1]
else:
    command = 'dummy'

for i in infiles:
    infile = i
    print i
    berekend = "berekend/" + infile[0:8] + ".csv"
    print berekend
    overslaan = ruw_csv(infile)
    print overslaan 
    df = pd.read_csv(infile, skiprows=overslaan,index_col=[2], parse_dates=True, usecols={2,4})
    #print(df)
    df2 = pd.read_csv(berekend, index_col=[0], parse_dates=True)
    df.dropna(how='any')
    #print df['Stand (cm t.o.v. MV)']
    #df*-1
    ser_meet = pd.Series(df['Stand (cm t.o.v. MV)']*-1, index = df.index)
    print 'GLG en GHG metingen:', GLG_berekening(ser_meet), GHG_berekening(ser_meet)
    ser_berekend = pd.Series(df2['Grondwaterstanden'], index = df2.index)
    print 'GLG en GHG berekening:', GLG_berekening(ser_berekend), GHG_berekening(ser_berekend)
    if command == 'plot':
        plot(df*-1, bestandspad, i)
        plot2(df*-1, df2, bestandspad, berekend)

               
