from django.db import connection
from django.http import HttpResponse

cursor = connection.cursor()

def respond_with_a_raster(request):
    # Write some SELECT query on raster data
    cursor.execute("SELECT ST_AsGDALRaster(rast, 'GTiff') FROM my_rasters")

     # Get a list of buffer objects out
     result = [
         row[0] for row in cursor.fetchall()
     ]

    # If expecting just one raster, unwrap until a buffer is found
    while type(result) != buffer:
        result = result[0]

    response = HttpResponse(result, content_type='image/tiff')
    response['Content-Disposition'] = 'attachment; filename=Bergingscoefficient.tiff')
    return response
