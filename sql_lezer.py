#dit script haalt data uit de MySQL databank met meteogegevens en zet ze in een numpy array
#auteur: John van Dam
#datum: 02-11-2015

from django.db import connection, models
from dateutil import parser
from knmi_database.models import MeteoData, NeerslagStation
import numpy as np
from datetime import datetime



def meteo_lezen(nummer_station, startdatum, einddatum):
	cursor = connection.cursor()
	startdatum = parser.parse(startdatum)
	einddatum = parser.parse(einddatum)
	#print startdatum, einddatum
	sql = """SELECT * FROM  knmi_database_meteodata WHERE datum >=\" """ + str(startdatum) +  """\" AND datum<= \"""" + str(einddatum) + """\" AND nummer= """ + str(nummer_station)+";"
	#sql="""SELECT * FROM  knmi_database_meteodata WHERE datum >= "1992-01-05 00:00:00" AND datum<= "1992-01-14 00:00:00" AND nummer= 344;"""
	#print sql
	cursor.execute(sql)
	rows = cursor.fetchall()
	print rows


def meteo_query(nummerstation, startdatum, einddatum):
	startdatum = parser.parse(startdatum)
	einddatum = parser.parse(einddatum)
	q = MeteoData.objects.filter(nummer=nummerstation)
	q = q.filter(datum__gte=startdatum)
	q = q.filter(datum__lte=einddatum)	
	datumlijst = q.values_list('datum', flat=True)
	neerslag = q.values_list('rh', flat=True)
	verdamping = q.values_list('ev24', flat=True)
	return datumlijst, neerslag, verdamping
	