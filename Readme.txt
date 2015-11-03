Author John van Dam
Date November 3rd 2015
Language Dutch

De bestanden in deze repository zijn voor de ftm webapplicatie die ik ontwikkel voor mijn afstuderen.
Ftm betekent fysische tijdreeksmodellering en in deze casus heeft deze fysische tijdreeksmodellering betrekking op het berekenen van freatische grondwaterstanden.
De modellering wordt enerzijds gedaan aan de hand van bodemgegevens (drainageweerstand, bergingscoëfficiënt, kwel/wegzijging en ontwateringsbasis) en anderzijds aan de hand van tijdreeksen met neerslag en verdamping.
Op het moment van schrijven (3 november 2015) kan het model alleen nog maar de berekening doen voor de grondwaterstanden tot aan gisteren, de ambitie is om aan de hand van weersvoorspellingen van het KNMI ook de grondwaterstand van morgen en overmorgen te berekenen.
Het voorspellen moet mogelijk worden door vanaf de website van het KNMI de benodigde data te halen en die door het model te sturen, qua code zal er aan het rekenhart niets veranderen.

Todo voor in de komende periode:
#MySQL databank gebruiken voor neerslaggegevens, naar verwachting verbeterd dit de snelheid van de webapplicatie.
#Mogelijkheid inbouwen om een rekenperiode te selecteren, hangt samen met het gebruik van MySQL, omdat hierbij door een query precies die data opgehaald wordt die nodig is om de gevraagde periode door te rekenen.
#Voorspellen van grondwaterstanden aan de hand van weersvoorspellingen van het KNMI.
#Resultaten plotten met behulp van een javascript in de browser van de gebruiker in plaats van een pythonscript waarvan vervolgens de plot geserveerd wordt.
#Website mooier maken, onder andere door hem geschikt te maken voor mobiele browsers. De twitter-bootstrap-api wordt hier waarschijnlijk voor gebruikt.
#Mogelijkheid inbouwen om met de ontwateringsbasis te spelen, het rekenhart moet hiervoor wel veranderd worden, omdat een variabele ontwateringsbasis een net iets andere formule gebruikt. 


######################################################################################
An English translation of this Readme will folow in the (near) future


Please send any questions or remarks to jpcvandam@gmail.com 