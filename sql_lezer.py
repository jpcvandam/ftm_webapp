#dit script haalt data uit de MySQL databank met meteogegevens en zet ze in een numpy array
#auteur: John van Dam
#datum: 02-11-2015

from django.db import connection, models
from dateutil import parser
from knmi_database.models import MeteoData, NeerslagStation
import numpy as np
from datetime import datetime




def meteo_query(nummerstation, startdatum, einddatum):
	startdatum = parser.parse(startdatum)
	einddatum = parser.parse(einddatum)
	q = MeteoData.objects.filter(nummer=nummerstation)
	q = q.filter(datum__gte=startdatum)
	q = q.filter(datum__lte=einddatum)	
	datumlijst = q.values_list('datum', flat=True)
	neerslag = q.values_list('rh', flat=True)
	verdamping = q.values_list('ev24', flat=True)
	print datumlijst, neerslag, verdamping
	return datumlijst, neerslag, verdamping
	