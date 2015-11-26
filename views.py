#datum laatste wijziging: 25 november 2015

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
from FTM_module import maak_plotje2, maak_plotje_aangepast
from django.template.context_processors import request
from StringIO import StringIO
from raster import raster_q
from ftm.settings import DATA_ROOT

def bodem_query(x,y):
    bestandspad = DATA_ROOT
    x = str(x)
    y = str(y)
    bergingscoefficient = float(raster_q(bestandspad + "bergcoef-nzv.tif", x, y))
    drainweerstand = float(raster_q(bestandspad + "drainw-nzv.tif", x, y))
    qbot = float(raster_q(bestandspad + "kwel-nzv.tif", x, y))
    ontwateringsbasis = (float(raster_q(bestandspad + "ontwbas-nzv.tif", x, y))*-1.0)
    return bergingscoefficient, drainweerstand, qbot, ontwateringsbasis

def index(request):
    'Display map'
    x = 6.5108
    y = 53.3847
    return render_to_response('ftm/index.html',{'x':x, 'y':y})


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


def ftm_aangepast(request):
    'aangepast'
    x = request.GET.get('x')
    y = request.GET.get('y')
    startdatum = request.GET.get('startdatum')
    einddatum = request.GET.get('einddatum')
    bergc = request.GET['berg']
    drainc = request.GET['drain']
    qbot1 = request.GET['qbot']
    ontwbas1 = request.GET['ontwbas']
    data = maak_plotje_aangepast(x, y, startdatum, einddatum, 'plot', bergc, drainc, qbot1, ontwbas1)
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
    o_data = bodem_query(x,y)
    o_bergingscoefficient = o_data[0]
    o_drainweerstand = o_data[1]
    o_qbot = o_data[2]
    o_ontwateringsbasis = o_data[3] 
    return render_to_response("ftm/aangepaste_grafiek.html", { 'x':x, 'y':y, 'plotje': plotje, 'ghg':ghg, 'glg':glg, 'gt' :gt, 'startdatum':startdatum, 'einddatum':einddatum,'bergingscoefficient': bergingscoefficient, 'drainweerstand':drainweerstand, 'qbot':qbot, 'ontwateringsbasis':ontwateringsbasis, 'o_bergingscoefficient':o_bergingscoefficient, 'o_drainweerstand': o_drainweerstand, 'o_qbot':o_qbot, 'o_ontwateringsbasis':o_ontwateringsbasis})


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

def aangepaste_series_as_csv(series, x, y, start, eind):
    naam = 'aangepaste_grondwaterstanden_x' + str(x) + '_y' + str(y) + str(start) + 'tm' + str(eind)
    filename = slugify(naam) + '.csv'
    buffer = StringIO()
    series.to_csv(buffer, encoding='utf-8') 
    csv = buffer.getvalue()
    resp = HttpResponse(csv, content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename=%s' % filename   
    return resp

def download_aangepaste_reeks(request):
    'Download de berekende aangepaste reeks'
    x = request.GET.get('x')
    y = request.GET.get('y')
    startdatum = request.GET.get('startdatum')
    einddatum = request.GET.get('einddatum')
    bergc = request.GET['berg']
    drainc = request.GET['drain']
    qbot1 = request.GET['qbot']
    ontwbas1 = request.GET['ontwbas']
    GWS = maak_plotje_aangepast(x, y, startdatum, einddatum, 'csv', bergc, drainc, qbot1, ontwbas1)[0]
    startdatum = maak_plotje_aangepast(x, y, startdatum, einddatum, 'csv', bergc, drainc, qbot1, ontwbas1)[1]
    einddatum = maak_plotje_aangepast(x, y, startdatum, einddatum, 'csv', bergc, drainc, qbot1, ontwbas1)[2]
    return aangepaste_series_as_csv(GWS, x, y, startdatum, einddatum)


def page_not_found(request):
    return render(request, "404.html")
