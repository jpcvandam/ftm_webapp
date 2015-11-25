#deze module zorgt dat de data voor de GHG en GLG op de juiste manier uit het dataframe met grondwaterstanden gehaald wordt 
#Auteur: John van Dam
#Datum: 8 september 2015

import pandas as pd
import numpy as np

###################################################################
#GLG uit het dataframe dfGWS halen
def GLG_berekening(dfGWS, dates, lengte):
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
    array_GLG = np.full((1, lengte), GLG, order='C') #maak een array met de uiteindelijke GLG om die later te kunnen plotten
    dfGLGs = pd.Series(array_GLG[0], index=dates) #array converteren naar pandas dataframe, omdat dat makkelijker plot
    return GLG, dfGLGs

###################################################################
#GHG uit het dataframe dfGWS halen

def GHG_berekening(dfGWS, dates, lengte):
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
    array_GHG = np.full((1, lengte), GHG, order='C') #maak een array met de uiteindelijke GHG om die later te kunnen plotten
    dfGHGs = pd.Series(array_GHG[0], index=dates) #array converteren naar pandas dataframe, omdat dat makkelijker plot
    return GHG, dfGHGs
###################################################################
