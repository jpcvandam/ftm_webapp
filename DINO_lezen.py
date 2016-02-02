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

import os
import pandas as pd
from dateutil import parser
from pandas.tslib import parse_date

os.chdir("/home/john/Documenten/Afstuderen_Acacia_water/Data/dino_gedeelte_NZV/Grondwaterstanden_Put")
infile = "B07A0112001_1.csv" #bestandsnaam met eventueel een pad ervoor

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

df = pd.read_csv(infile, skiprows=overslaan,index_col=[2], parse_dates=True, usecols={2,4})
print(df)

df.dropna(how='any')
print df['Stand (cm t.o.v. MV)']


               
