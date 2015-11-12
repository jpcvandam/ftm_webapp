from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection
from django.shortcuts import render_to_response#, 
from django.template.loader import render_to_string 
from django.utils.text import slugify
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
from django.template.context_processors import request



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
    data = maak_plotje2(x, y, startdatum, einddatum, 'plot')
    plotje = data[0]
    gt = data[1]
    ghg = data[2]
    glg = data[3]
    return render_to_response("ftm/grafiek.html", { 'x':x, 'y':y, 'plotje': plotje, 'ghg':ghg, 'glg':glg, 'gt' :gt})


def series_as_csv(series):
    filename = slugify(series) + '.csv'
    csv = series.to_csv()
    resp = HttpResponse(csv, content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename=%s' % filename   
    return resp

def download_reeks(request):
    'Download de berekende reeks'
    x = request.GET.get('x')
    y = request.GET.get('y')
    startdatum = request.GET.get('startdatum')
    einddatum = request.GET.get('einddatum')
    data = maak_plotje2(x, y, startdatum, einddatum, 'csv')
    GWS=data[0]    
    return render_to_response(series_as_csv(GWS))
