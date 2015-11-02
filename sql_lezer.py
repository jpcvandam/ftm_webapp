#dit script haalt data uit de MySQL databank met meteogegevens en zet ze in een numpy array
#auteur: John van Dam
#datum: 02-11-2015

from django.db import connection, models
from dateutil import parser
from knmi_database.models import MeteoData
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
	qs = MeteoData.objects.get(datum__gt=datetime.date(startdatum), nummer__gt=nummerstation) 
	#.get haalt in dit geval teveel op en dat moet ook, maar mag niet van Django, datum__gt werkt in elk geval en daar was het om te doen
	vlqs - qs.values_list()
	rij = np.core.records.fromrecords (vlqs, names=[f.name for f in MeteoData._meta.fields])
	print rij
	