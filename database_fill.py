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


def meteo_in_database(nummer_meteostation, data, con, yyyymmdd, dr, rh, rhx, ev24):
	for i in [235]:
		stationsnamen[i].replace('\n', ' ').replace('\r\n', '')
		meteodata=yymmdd[i], dr[i], rh[i], rhx[i], ev24[i]
		tuple(meteodata) 
		print meteodata
		with con:
			cur = con.cursor()
			cur.execute("CREATE TABLE"+[i]+"(yyyymmdd TEXT, dr INT, rh INT, rhx INT, ev24 INT)")
			cur.executemany("INSERT INTO meteostations VALUES(?, ?, ?, ?, ?)", (meteodata,))
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
print fileinput.readlines ()[1:17]
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
print meteo_lezen(235), 'meteo lezen'
