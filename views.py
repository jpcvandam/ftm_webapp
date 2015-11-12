from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render_to_response#, 
from django.template.loader import render_to_string 
#import simplejson

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
from FTM_module import maak_plotje, supersnel_ftm, maak_plotje2



def index(request):
    'Display map'
    
    return render_to_response('ftm/index.html')








###################################################################
#hier komt dan het ftm
def ftm(request):
    'Grondwaterstand'
    x = request.GET.get('x')
    y = request.GET.get('y')
    data = maak_plotje(x, y)
    plotje = data[0]
    gt = data[1]
    ghg = data[2]
    glg = data[3]
    return render_to_response("ftm/grafiek.html", { 'x':x, 'y':y, 'plotje': plotje, 'ghg':ghg, 'glg':glg, 'gt' :gt})
    #return render_to_response('ftm/index.html', {
     #   'waypoints': waypoints,
      #  'content': render_to_response('ftm/grafiek.html', {plotje=plotje, x=x, y=y}),
    #})


def ftmsnel(request):
    'Grondwaterstandsnel'
    x = request.GET.get('x')
    y = request.GET.get('y')
    plotje = supersnel_ftm(x, y)[0]
    return render_to_response("ftm/grafiek.html", { 'x':x, 'y':y, 'plotje': plotje})

    
def ftmsql(request):
    'Grondwaterstand-sql'
    x = request.GET.get('x')
    y = request.GET.get('y')
    startdatum = request.GET.get('startdatum')
    einddatum = request.GET.get('einddatum')
    data = maak_plotje2(x, y, startdatum, einddatum)
    plotje = data[0]
    gt = data[1]
    ghg = data[2]
    glg = data[3]
    return render_to_response("ftm/grafiek.html", { 'x':x, 'y':y, 'plotje': plotje, 'ghg':ghg, 'glg':glg, 'gt' :gt})#, 'datum_array':datum_array, 'array_neerslag':array_neerslag, 'array_verdamping':array_verdamping})


