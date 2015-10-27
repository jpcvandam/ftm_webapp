#deze module zorgt dat de data voor de GHG en GLG op de juiste manier uit het dataframe met grondwaterstanden gehaald wordt 
#Auteur: John van Dam
#Datum: 8 september 2015

import pandas as pd
import numpy as np

def waterbalans_in(nummer_meteostation):
    for i in [nummer_meteostation]:
        meteobestand_in = 'Waterbalans_METEO'+str(i)+'.csv'
        dfNettoNeerslag = pd.read_csv(meteobestand_in, header=False, skiprows=1, names = ['datum', 'NN1', 'NN2' ], delimiter =',', parse_dates=[0])
    return dfNettoNeerslag



