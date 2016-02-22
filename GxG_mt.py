#deze module zorgt dat de data voor de GHG en GLG op de juiste manier uit het dataframe met grondwaterstanden gehaald wordt 
#Auteur: John van Dam
#Datum: 8 september 2015
#datum laatste wijziging: 25 november 2015

import pandas as pd
import numpy as np

###################################################################
#GLG uit het dataframe dfGWS halen
def GLG_berekening(dfGWS):
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
                    | (dfGWS.index.month == 9) & (dfGWS.index.day == 28))]  #
#print dfGLG.mean()
    grouped_l = dfGLG.groupby(lambda x: x.year)
    extremen_l = grouped_l.nsmallest(3).to_frame(name='extremen_l')
    GLG = extremen_l.mean()
    return GLG


###################################################################
#GHG uit het dataframe dfGWS halen

def GHG_berekening(dfGWS):
    dfGHG = dfGWS[((dfGWS.index.month == 10) & (14 == dfGWS.index.day)  # 
                    | (dfGWS.index.month == 10) & (dfGWS.index.day == 28)
                    | (dfGWS.index.month == 11) & (dfGWS.index.day == 14)
                    | (dfGWS.index.month == 11) & (dfGWS.index.day == 28)
                    | (dfGWS.index.month == 12) & (dfGWS.index.day == 14)
                    | (dfGWS.index.month == 12) & (dfGWS.index.day == 28)
                    | (dfGWS.index.month == 1) & (dfGWS.index.day == 28)
                    | (dfGWS.index.month == 1) & (dfGWS.index.day == 14)
                    | (dfGWS.index.month == 2) & (dfGWS.index.day == 28)
                    | (dfGWS.index.month == 2) & (dfGWS.index.day == 14)
                    | (dfGWS.index.month == 3) & (dfGWS.index.day == 14)
                    | (dfGWS.index.month == 3) & (dfGWS.index.day == 28))]  #
    grouped_h = dfGHG.groupby(lambda x: x.year)
    extremen_h = grouped_h.nlargest(3).to_frame(name='extremen_h')
    GHG = extremen_h.mean()
    return GHG
###################################################################

def GVG_berekening(dfGWS):
    dfGVG = dfGWS[((dfGWS.index.month == 3) & (14 == dfGWS.index.day)  # 
                    | (dfGWS.index.month == 3) & (dfGWS.index.day == 28)
                    | (dfGWS.index.month == 4) & (dfGWS.index.day == 14))]
    GVG = dfGVG.mean()   
    return GVG
