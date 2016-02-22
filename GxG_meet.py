#deze module zorgt dat de data voor de GHG en GLG op de juiste manier uit het dataframe met grondwaterstanden gehaald wordt 
#Auteur: John van Dam
#Datum: 8 september 2015
#datum laatste wijziging: 08 februari 2016

import pandas as pd
import numpy as np

###################################################################
#GLG uit het dataframe dfGWS halen
def GLG_berekening(dfGWS): #input wordt wordt hier wel dataframe genoemd, maar het werkt alleen met een pandas Series
    dfGLG = dfGWS[((dfGWS.index.month == 4)  # 
                    | (dfGWS.index.month == 5) 
                    | (dfGWS.index.month == 6) 
                    | (dfGWS.index.month == 7) 
                    | (dfGWS.index.month == 8) 
                    | (dfGWS.index.month == 9))]  #
#print dfGLG.mean()
#onderstaande code aanpassen, zodat een dag die niet bestaat verschoven kan worden
    try:
        dfGLG = dfGWS[((dfGWS.index.month == 4) & (14 == dfGWS.index.day)  # 
                        | (dfGWS.index.month == 4) & (dfGWS.index.day == 28)
                        | (dfGWS.index.month == 5) & (dfGWS.index.day == 14)
                        | (dfGWS.index.month == 5) & (dfGWS.index.day == 28)
                        | (dfGWS.index.month == 6) & (dfGWS.index.day == 14)
                        | (dfGWS.index.month == 6) & (dfGWS.index.day == 28)
                        | (dfGWS.index.month == 7) & (dfGWS.index.day == 28)
                        | (dfGWS.index.month == 7) & (dfGWS.index.day == 14)
                        | (dfGWS.index.month == 8) & (dfGWS.index.day == 28)
                        | (dfGWS.index.month == 8) & (dfGWS.index.day == 14)
                        | (dfGWS.index.month == 9) & (dfGWS.index.day == 14)
                        | (dfGWS.index.month == 9) & (dfGWS.index.day == 28))]
    except IndexError:
        print "jammer, niet gelukt"
    #tot hier het experiment
    grouped_l = dfGLG.groupby(lambda x: x.year)
    extremen_l = grouped_l.nsmallest(3).to_frame(name='extremen_l')
    GLG = extremen_l.mean()
    return GLG

###################################################################
#GHG uit het dataframe dfGWS halen

def GHG_berekening(dfGWS): #input wordt wordt hier wel dataframe genoemd, maar het werkt alleen met een pandas Series
    dfGHG = dfGWS[((dfGWS.index.month == 10)# 
                    | (dfGWS.index.month == 11)
                    | (dfGWS.index.month == 12)
                    | (dfGWS.index.month == 1)
                    | (dfGWS.index.month == 2)
                    | (dfGWS.index.month == 3))]  #
    grouped_h = dfGHG.groupby(lambda x: x.year)
    extremen_h = grouped_h.nlargest(3).to_frame(name='extremen_h')
    GHG = extremen_h.mean()
    return GHG
###################################################################

def GVG_berekening(dfGWS, dates, lengte):
    dfGVG = dfGWS[((dfGWS.index.month == 3) & (14 == dfGWS.index.day)  # 
                    | (dfGWS.index.month == 3) & (dfGWS.index.day == 28)
                    | (dfGWS.index.month == 4) & (dfGWS.index.day == 14))]
    GVG = dfGVG.mean()
    array_GVG = np.full((1, lengte), GVG, order='C') #maak een array met de uiteindelijke GHG om die later te kunnen plotten
    dfGVGs = pd.Series(array_GVG[0], index=dates) #array converteren naar pandas dataframe, omdat dat makkelijker plot
    return GVG, dfGVGs
