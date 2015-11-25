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
from FTM_module import maak_plotje2
from django.template.context_processors import request
from StringIO import StringIO
from raster import raster_q
from ftm.settings import DATA_ROOT


def index(request):
    'Display map'
    x = 6.5108
    y = 53.3847
    bestandspad = DATA_ROOT
    x = str(x)
    y = str(y)
    bergingscoefficient = float(raster_q(bestandspad + "bergcoef-nzv.tif", x, y))
    drainweerstand = float(raster_q(bestandspad + "drainw-nzv.tif", x, y))
    qbot = float(raster_q(bestandspad + "kwel-nzv.tif", x, y))
    ontwateringsbasis = (float(raster_q(bestandspad + "ontwbas-nzv.tif", x, y))*-1.0)
    return render_to_response('ftm/index.html',{'x':x, 'y':y, 'bergingscoefficient': bergingscoefficient, 'drainweerstand':drainweerstand, 'qbot':qbot, 'ontwateringsbasis':ontwateringsbasis})


###################################################################
#hier komt dan het ftm
   
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
    startdatum = data[4]
    einddatum = data[5]
    bergingscoefficient = data[6]
    drainweerstand = data[7]
    qbot =data[8]
    ontwateringsbasis = data[9]
    return render_to_response("ftm/grafiek.html", { 'x':x, 'y':y, 'plotje': plotje, 'ghg':ghg, 'glg':glg, 'gt' :gt, 'startdatum':startdatum, 'einddatum':einddatum,'bergingscoefficient': bergingscoefficient, 'drainweerstand':drainweerstand, 'qbot':qbot, 'ontwateringsbasis':ontwateringsbasis})


def series_as_csv(series, x, y, start, eind):
    naam = 'grondwaterstanden_x' + str(x) + '_y' + str(y) + str(start) + 'tm' + str(eind)
    filename = slugify(naam) + '.csv'
    buffer = StringIO()
    series.to_csv(buffer, encoding='utf-8') 
    csv = buffer.getvalue()
    resp = HttpResponse(csv, content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename=%s' % filename   
    return resp

def download_reeks(request):
    'Download de berekende reeks'
    x = request.GET.get('x')
    y = request.GET.get('y')
    startdatum = request.GET.get('startdatum')
    einddatum = request.GET.get('einddatum')
    GWS = maak_plotje2(x, y, startdatum, einddatum, 'csv')[0]
    startdatum = maak_plotje2(x, y, startdatum, einddatum, 'csv')[1]
    einddatum = maak_plotje2(x, y, startdatum, einddatum, 'csv')[2]
    return series_as_csv(GWS, x, y, startdatum, einddatum)

def page_not_found(request):
    return render(request, "404.html")
