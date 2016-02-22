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
from GxG_mt import GLG_berekening, GHG_berekening

bestandspad = "/home/john/Documenten/Afstuderen_Acacia_water/Data/Noorderzijlvest-gegevens/Noorderzijlvest/DINO/Uitgepakt/Grondwaterstanden_Put/" #"/home/john/Documenten/Afstuderen_Acacia_water/Data/dino_gedeelte_NZV/Grondwaterstanden_Put/"
os.chdir(bestandspad)

if len(sys.argv) == 2:
    lijst_infiles = sys.argv[1]
    command = 'dummy'
elif len(sys.argv) == 3:
    lijst_infiles = str(sys.argv[1])
    command = sys.argv[2]
else:
    print "gebruik, ", sys.argv[0], " lijst_infiles [plot]"

infiles = []

with open(lijst_infiles, 'r') as fileinput:
    for line in fileinput:
        infiles.append(str(line.rstrip('\r\n')))
fileinput.close()

#infiles = ["B07A0969001_1.csv", "B03D0321001_1.csv", "B12A1810001_1.csv", "B12B1649001_1.csv", "B03D0320001_1.csv", "B03D0322001_1.csv", "B03D0323001_1.csv", "B12A1811001_1.csv", "B12B1640001_1.csv", "B12B1642001_1.csv", "B07D1894001_1.csv", "B12C1594001_1.csv", "B12A1795001_1.csv", "B07C1717001_1.csv", "B03C0262001_1.csv", "B12A1747001_1.csv", "B07C0267001_1.csv", "B12A0213001_1.csv", "B07C1722001_1.csv", "B07D1893001_1.csv", "B12A1801001_1.csv", "B12C1542001_1.csv", "B12C1598001_1.csv", "B07D1895001_1.csv", "B07C1710001_1.csv", "B07A0967001_1.csv", "B12A0120001_1.csv", "B07C1705001_1.csv", "B12A1808001_1.csv", "B12C1602001_1.csv", "B12A1760001_1.csv", "B12A1814001_1.csv", "B12C0056001_1.csv", "B12A1812001_1.csv", "B12C1596001_1.csv", "B12A1756001_1.csv", "B07B1136001_1.csv", "B07D2561001_1.csv", "B07B1137001_1.csv", "B07B1138001_1.csv", "B07A0966001_1.csv", "B12A1794001_1.csv", "B03C0264001_1.csv", "B12C1605001_1.csv", "B07C1712001_1.csv", "B07C1721001_1.csv", "B07C1728001_1.csv", "B12B1650001_1.csv", "B07C1729001_1.csv", "B12A1767001_1.csv", "B12B1643001_1.csv", "B12A1798001_1.csv", "B07C1713001_1.csv", "B12A1759001_1.csv", "B12B1652001_1.csv", "B12C1601001_1.csv", "B12A1750001_1.csv", "B07C1724001_1.csv", "B12B1724001_1.csv", "B07B1148001_1.csv", "B07A0965001_1.csv", "B07D1892001_1.csv", "B07C1709001_1.csv", "B07D1891001_1.csv", "B07C1714001_1.csv", "B07C1739001_1.csv", "B07C1736001_1.csv", "B07C1726001_1.csv", "B12B1644001_1.csv", "B07C1718001_1.csv", "B07C1715001_1.csv", "B12B1651001_1.csv", "B07C1716001_1.csv", "B07C1720001_1.csv", "B12B1647001_1.csv", "B07C1735001_1.csv", "B07C1711001_1.csv", "B07C1725001_1.csv", "B07D0242001_1.csv", "B06H1500001_1.csv", "B06H1501001_1.csv", "B07D0497001_1.csv", "B12A1734001_1.csv", "B12A1766001_1.csv", "B12A1763001_1.csv", "B07D2567001_1.csv", "B07B1139001_1.csv", "B07D2562001_1.csv", "B07D2566001_1.csv", "B07C1708001_1.csv", "B12C1604001_1.csv", "B03C0265001_1.csv", "B12A1752001_1.csv", "B12A1762001_1.csv", "B12A1738001_1.csv", "B12B1648001_1.csv", "B07D2563001_1.csv", "B07C1719001_1.csv", "B12C1603001_1.csv", "B07C1706001_1.csv", "B07C1811001_1.csv", "B06H1502001_1.csv", "B12A1754001_1.csv", "B07D2559001_1.csv", "B07D2565001_1.csv", "B07D2560001_1.csv", "B07D2564001_1.csv", "B06H0176001_1.csv", "B06H1503001_1.csv", "B07C1727001_1.csv", "B12A1764001_1.csv", "B06H0175001_1.csv", "B07C1723001_1.csv", "B12B0342001_1.csv", "B12A1749001_1.csv", "B12A1809001_1.csv", "B12C1595001_1.csv", "B07C1808001_1.csv", "B07C1707001_1.csv", "B12C1599001_1.csv", "B12B1645001_1.csv", "B07A0971001_1.csv", "B07A0973001_1.csv", "B07B1142001_1.csv", "B07A0978001_1.csv", "B03D0317001_1.csv", "B03C0263001_1.csv", "B07A0972001_1.csv", "B07A0962001_1.csv", "B07A0976001_1.csv", "B03D0318001_1.csv", "B07B1150001_1.csv", "B03D0316001_1.csv", "B07B1152001_1.csv", "B07A0975001_1.csv", "B07B1149001_1.csv", "B07A0961001_1.csv", "B07B1145001_1.csv", "B07B1144001_1.csv", "B03D0319001_1.csv", "B07A0964001_1.csv", "B07B1147001_1.csv", "B07B1151001_1.csv", "B07B1140001_1.csv", "B07B1141001_1.csv", "B07A0970001_1.csv", "B07A0963001_1.csv", "B06H1504001_1.csv", "B06H1505001_1.csv", "B12A1736001_1.csv", "B07A0974001_1.csv", "B12B1646001_1.csv", "B12A1737001_1.csv", "B12C1600001_1.csv", "B12A1733001_1.csv", "B12B1790001_1.csv"]

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


of = open("/home/john/Documenten/Afstuderen_Acacia_water/Data/Noorderzijlvest-gegevens/Noorderzijlvest/DINO/Uitgepakt/Grondwaterstanden_Put/statistiek.txt", 'w')
of.write("Locatie, GLG_meting, GHG_meting, GLG_berekend, GHG_berekend\n")

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
    #print 'GLG en GHG metingen:', GLG_berekening(ser_meet), GHG_berekening(ser_meet)
    ser_berekend = pd.Series(df2['Grondwaterstanden'], index = df2.index)
    #print 'GLG en GHG berekening:', GLG_berekening(ser_berekend), GHG_berekening(ser_berekend)
    Locatie = i 
    GLG_meting = GLG_berekening(ser_meet)
    GHG_meting = GHG_berekening(ser_meet)
    GLG_berekend = GLG_berekening(ser_berekend)
    GHG_berekend = GHG_berekening(ser_berekend)
    of.write("%s, %f, %f, %f, %f\n" % (Locatie, GLG_meting, GHG_meting, GLG_berekend, GHG_berekend))
    if command == 'plot':
        plot(df*-1, bestandspad, i)
        plot2(df*-1, df2, bestandspad, berekend)

of.close()

               
