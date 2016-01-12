#Auteur: John van Dam
#Datum: 12 januari 2016
#Doel: Dit script moet de harmonie verwachtingen van het KNMI binnenhalen en bewerken tot bruikbare data
#URL data: https://data.knmi.nl/download/harmonie_p1/0.2/noversion/0000/00/00/harm36_v1_ned_surface_06.tgz

import urllib
import os

os.chdir("/home/john/Downloads")

harmonie_data = urllib.URLopener()
harmonie_data.retrieve("https://data.knmi.nl/download/harmonie_p1/0.2/noversion/0000/00/00/harm36_v1_ned_surface_06.tgz", "voorspelling.tgz")