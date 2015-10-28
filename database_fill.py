#database filler and reader
#purpose: fill and maintain a meteodatabase for the FTM and make fast data searching and slicing in dateranges possible
#Author: John van Dam
#Date: 28 October 2015

import sqlite3 as lite
import sys

def meteo_lezen(nummer_meteostation):
	yyyymmdd=[]
	dr=[]
	rh=[]
	rhx=[]
	ev24=[]
	with open('data/METEO'+ str(nummer_meteostation) + '.TXT', 'r') as fileinput:
	    for _ in xrange(20):
			next(fileinput)
	    for line in fileinput:
			yyyymmdd.append(str(line[6:14]))
			#print line[6:14]
			dr.append(int(line[16:20]))
			#print line[16:20]
			rh.append (int(line[22:26]))
			#print line[22:26]
			rhx.append (int(line[27:32]))
			#print line[27:32]
			ev24.append (int(line[51:56]))
			#print line[51:56]
	fileinput.close()
	return yyyymmdd, dr, rh, rhx, ev24


def meteo_in_database(nummer_meteostation, con, yyyymmdd, dr, rh, rhx, ev24):
    with con:
		cur = con.cursor()
		cur.execute("DROP TABLE IF EXISTS station235;")
		cur.execute("CREATE TABLE station235 (yyyymmdd TEXT, dr INT, rh INT, rhx INT, ev24 INT)")
		for i in range(1, len(yyyymmdd)):
			meteodata=yyyymmdd[i], dr[i], rh[i], rhx[i], ev24[i]
			tuple(meteodata)
			#print meteodata 
			with con:
				cur = con.cursor()
				cur.executemany("INSERT INTO station235 VALUES(?, ?, ?, ?, ?)", (meteodata,))
			#print meteodata
			#con.close()
	
###############################################################################	
#variabelen
nummer_meteostation=235
#connectie met databank declareren
con = lite.connect('data/meteo.db')
###############################################################################	

#meteostations in heel Nederland inlezen 
fileinput = open('data/weerstations_NLD.txt', 'r')
stations = []
fileinput.readline ()
stationsnummers=[]
stationsnamen=[]
stationslong=[]
stationslat=[]
for line in fileinput:
	stationsnummers.append(int(line[2:5]))
	stationslong.append(float(line[15:20]))
	stationslat.append (float(line[27:33]))
	stationsnamen.append (str(line[46:70]))	
fileinput.close()

#even een check of de stations juist zijn ingelezen
print stations
print stationsnummers
print stationsnamen
print stationslong
print stationslat

#meteostations in heel Nederland in de tabel meteostations zetten
with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS meteostations;")
	cur.execute("CREATE TABLE meteostations(Id INT, Naam TEXT, Long FLOAT, Lat FLOAT)")
for i in range(1, len(stationsnummers)):
	stationsnamen[i].replace('\n', ' ').replace('\r\n', '')
	stations=stationsnummers[i], stationsnamen[i], stationslong[i], stationslat[i]
	tuple(stations)
	print stations
	with con:
		cur = con.cursor()
		cur.executemany("INSERT INTO meteostations VALUES(?, ?, ?, ?)", (stations,))
	print stations #print om te checken
#con.close()
	
   
#    cur.execute("CREATE TABLE meteostations(Id INT, Naam TEXT, Long FLOAT, Lat FLOAT)")

###############################################################################	
#hieronder worden de tabellen voor de meteodata aangemaakt, de eerste tabel (met de meteostations) vormt de sleutel tot deze tabellen
print 'nu rijen ophalen uit een bestaande tabel'

#with con:    
    
#    cur = con.cursor()    
#    cur.execute("SELECT * FROM station235")

#    rows = cur.fetchall()

#    for row in rows:
#        print row


print 'we gaan de meteo nu eens lezen'
#print meteo_lezen(nummer_meteostation), 'meteo lezen'
yyyymmdd =  meteo_lezen(nummer_meteostation)[0]
dr = meteo_lezen(nummer_meteostation)[1]
rh = meteo_lezen(nummer_meteostation)[2]
rhx = meteo_lezen(nummer_meteostation)[3]
ev24 = meteo_lezen(nummer_meteostation)[4]
print 'we gaan de database vullen'
#meteodata in de database stoppen
meteo_in_database(nummer_meteostation, con, yyyymmdd, dr, rh, rhx, ev24)

print 'nu rijen ophalen uit de net gemaakte tabel'

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM station235")

    rows = cur.fetchall()

    for row in rows:
        print row
con.close()		
