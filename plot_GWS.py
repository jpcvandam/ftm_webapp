#module grondwaterstanden plotten
#Auteur: John van Dam
#Datum: 8 september 2015

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab


def plot(dfGWS, dfGHGs, dfGLGs, gt, nummer_meteostation, bestandspad, x2, y2):
    #plotje maken van de grondwaterstanden en opslaan
    # Create plots with pre-defined labels. Gebruik makend van de pandas series plot wrapper
    dfGWS.plot(label='Grondwaterstand')
    dfGHGs.plot(label='GHG')
    dfGLGs.plot(label='GLG')
	#dit zou de manier zijn met alleen matplotlib, de datums komen dan alleen heel vreemd uit de bus
	#plt.plot(dfGWS, label='Grondwaterstand')
    #plt.plot(dfGHGs, label='GHG')
    #plt.plot(dfGLGs, label='GLG')
    #aangeven dat er een legenda in moet en hoe die eruit moet zien
    plt.legend(loc='upper center', shadow=True, fontsize='x-large')
    #labels voor de assen en de grafiek declareren
    ax = pylab.gca()
    ax.set_ylabel('$cm-mv$')
    ax.text(2, 6,  gt, fontsize=15)
    plt.xlabel('Tijd')
    plt.title('Tijdstijghoogtelijn')
    #grafiek wegschrijven en pylab netjes afsluiten
    plotnaam='Grondwaterstanden_'+str(nummer_meteostation)+'_'+str(x2)+'_'+str(y2)+'.png'
    pylab.savefig(bestandspad + plotnaam, bbox_inches='tight')
    pylab.close()
    return plotnaam    

