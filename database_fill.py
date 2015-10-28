#database filler and reader
#purpose: fill and maintain a meteodatabase for the FTM and make fast data searching and slicing in dateranges possible
#Author: John van Dam
#Date: 28 October 2015

import sqlite3 as lite
import sys

def meteo_lezen(nummer_weerstation):
	fileinput = open('data/METEO'+ str(nummer_meteostation) + '.csv', 'r')
	fileinput.readline (19)
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


def meteo_in_database(nummer_meteostation, data):
	for i in range(1, len(data)):
		stationsnamen[i].replace('\n', ' ').replace('\r\n', '')
		meteo=stationsnummers[i], stationsnamen[i], stationslong[i], stationslat[i]
		tuple(meteo) 
		print meteo
		with con:
			cur = con.cursor()
			#STN,YYYYMMDD,   DR,   RH,  RHX, RHXH,EV24 = DR,   RH, EV24
			cur.executemany("INSERT INTO meteostations VALUES(?, ?, ?, ?)", (meteo,))
	print stations

con = None

try:
    con = lite.connect('data/meteo.db')
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data                
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()

con = lite.connect('data/test.db')

fileinput = open('data/weerstations_NLD.txt', 'r')
print fileinput.readlines ()[1:18]
print 'nu een regel'
print fileinput.readline ()

#stations = []
#fileinput.readline ()
#stationsnummers=[]
#stationsnamen=[]
#stationslong=[]
#stationslat=[]
#for line in fileinput:
#	stationsnummers.append(int(line[2:5]))
#	stationslong.append(float(line[15:20]))
#	stationslat.append (float(line[27:33]))
#	stationsnamen.append (str(line[46:70]))
	
fileinput.close()
#print stations
#print stationsnummers
#print stationsnamen
#print stationslong
#print stationslat

#for i in range(1, len(stationsnummers)):
#	stationsnamen[i].replace('\n', ' ').replace('\r\n', '')
#	stations=stationsnummers[i], stationsnamen[i], stationslong[i], stationslat[i]
#	tuple(stations)
#	print stations
#	with con:
#		cur = con.cursor()
#		cur.executemany("INSERT INTO meteostations VALUES(?, ?, ?, ?)", (stations,))
#	print stations

	
   
#    cur.execute("CREATE TABLE meteostations(Id INT, Naam TEXT, Long FLOAT, Lat FLOAT)")


print 'nu rij ophalen'

#with con:    
    
#    cur = con.cursor()    
#    cur.execute("SELECT * FROM meteostations")

#    rows = cur.fetchall()

#    for row in rows:
#        print row

#with con:
#	cur = con.cursor()
#	cur.execute("CREATE TABLE i(Id INT, Naam TEXT, Long FLOAT, Lat FLOAT)")