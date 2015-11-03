Author John van Dam
Date November 3rd 2015
Language Dutch

De bestanden in deze repository zijn voor de ftm webapplicatie die ik ontwikkel voor mijn afstuderen.
Ftm betekent fysische tijdreeksmodellering en in deze casus heeft deze fysische tijdreeksmodellering betrekking op het berekenen van freatische grondwaterstanden.
De modellering wordt enerzijds gedaan aan de hand van bodemgegevens (drainageweerstand, bergingscoëfficiënt, kwel/wegzijging en ontwateringsbasis) en anderzijds aan de hand van tijdreeksen met neerslag en verdamping.
Op het moment van schrijven (3 november 2015) kan het model alleen nog maar de berekening doen voor de grondwaterstanden tot aan gisteren, de ambitie is om aan de hand van weersvoorspellingen van het KNMI ook de grondwaterstand van morgen en overmorgen te berekenen.
Het voorspellen moet mogelijk worden door vanaf de website van het KNMI de benodigde data te halen en die door het model te sturen, qua code zal er aan het rekenhart niets veranderen.

Het project heeft bepaalde vaste elementen uit Django. Deze elementen zijn __init__.py, models.py, settings.py, wsgi.py en views.py. Daarnaast maakt Django een map aan met de naam 'migrations', daarin worden migraties en aanpassingen van de databank geregeld.
In views.py worden alle zelfgemaakte modules aan elkaar gelinkt. Er is voor deze modulaire opzet gekozen, omdat eventuele fouten daardoor gemakkelijker te repareren zijn en goede modules hergebruikt kunnen worden.
Als er een request komt aan het adres van het ftm, leest een proceduren uit views.py eerst de meteogegevens uit een csv in een pandas dataframe, en maakt daar vervolgens een numpy array van om later in het programma te kunnen rekenen.
Vervolgens wordt uit de tif-rasters in het mapje data bodemdata gelezen door het aanroepen van de functie raster_q uit de module lees_raster.py. Het resultaat daarvan wordt van string naar float geconverteerd en opgeslagen in een set numpy arrays. Deze conversie is nodig, omdat het ftm anders niet kan rekenen, strings zijn voor de computer gewoon tekst waar niet mee te rekenen is.
Nu kan er gerekend worden en dat gebeurt dan ook doormiddel van een for-loop die de net voorbereide gegevens door het rekenhart heen jast en in een array stopt  

Todo voor in de komende periode:
#MySQL databank gebruiken voor neerslaggegevens, naar verwachting verbeterd dit de snelheid van de webapplicatie.
	* de app 'knmi_database' in de repository naast de 'ftm' repository kan het dichtstbijzijnde neerslagstation opzoeken gegeven een set coordinaten, dit wordt onderdeel van de MySQL query.
	* het ophalen van de meteodata van gisteren en eergisteren kan en gaat nu automatisch met een crontab, het bijwerken van de databank moet nog worden geautomatiseerd. 
#Mogelijkheid inbouwen om een rekenperiode te selecteren, hangt samen met het gebruik van MySQL, omdat hierbij door een query precies die data opgehaald wordt die nodig is om de gevraagde periode door te rekenen.
#Voorspellen van grondwaterstanden aan de hand van weersvoorspellingen van het KNMI.
#Resultaten plotten met behulp van een javascript in de browser van de gebruiker in plaats van een pythonscript waarvan vervolgens de plot geserveerd wordt.
#Website mooier maken, onder andere door hem geschikt te maken voor mobiele browsers. De twitter-bootstrap-api wordt hier waarschijnlijk voor gebruikt.
#Mogelijkheid inbouwen om met de ontwateringsbasis te spelen, het rekenhart moet hiervoor wel veranderd worden, omdat een variabele ontwateringsbasis een net iets andere formule gebruikt. 


######################################################################################
An English translation of this Readme will folow in the (near) future


Please send any questions or remarks to jpcvandam@gmail.com 