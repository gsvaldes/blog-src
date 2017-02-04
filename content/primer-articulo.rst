Hacer un mapa de los barrios de New Haven
#########################################

:date: 2016-10-31 7:32
:modified: 2016-12-17 12:30
:tags: random
:category: about
:slug: new-haven-neighborhoods
:lang: es
:authors: Geoffrey Valdes
:summary: Generating GeoJson for New Haven neighborhood boundaries
:javascripts: https://unpkg.com/leaflet@1.0.1/dist/leaflet.js, nh_map.js
:stylesheets: https://unpkg.com/leaflet@1.0.1/dist/leaflet.css, map.css

Me mudé a New Haven hace unos meses.  Como parte de conocer la ciudad, quiero saber cuáles son los distintos barrios y mostrarlos en un mapa web usando Leaflet.  Para hacer eso, necesito tener la descripción los límites de los barrios en el formato GeoJSON. 

Para New Haven, es probable que `Data Haven <http://www.ctdatahaven.org/>`_  ya tiene estos datos en un formato limpiado, pero quiero mostrar los pasos para hacer eso en otros lugares.

En términos generales, los pasos son

* Descubrir como se define los barrios

* Conseguir un conjunto de datos geoespaciales que corresponde a la definición de los barrios

* Convertor el conjunto de datos geoepaciales al formato GeoJSON

* Dibujar los barrios en un mapa web usando el GeoJSON y Leaflet, una biblioteca de 

La ciudad de Austin, TX proporciona la gran parte de sus datos SIG, incluyendo los del formato shapefile, en línea y gratis.  No parece que la ciduad de New Haven hace lo mismo.  Pero si tiene un plan de la ciudad que muestra las secciones censales que corresponde a cada barrio:

http://www.cityofnewhaven.com/cityplan/pdfs/PlanningPrograms/Demographics.pdf

Como se nota en otra página de la ciudad, "Los límites de los vecindarios son aproximados y ajustados para coincidir con las secciones censales.  No hay límites oficiales de los vecindarios"

Con la información anterior, ahora puedo descargar los shapefiles de las secciones censales para el Estado de Connecticut, mapear un subconjunto de ellos a los vecindarios correspondientes de New Haven, y luego convertirlo en un archivo GeoJson.

La Universidad de Connnecticut proporciona datos SIG para el estado
http://magic.lib.uconn.edu/connecticut_data.html

Especificamente, de la sección 'Census - 2010 Boundary Files' se puede descargar los shapefiles de Connecticut Tracts y abrirlos en qGIS.

En el panel de capas(Layers), se muestra como
``tractct_37800__0000_2010_s100_census_shp_wgs85wgs``

Abriendo la tabla de atributos para esta capa, se ve que la columna NAME10 contiene el número de sección censal que corresponde a los
números de seccion enumerados en el mapa vecindal anterior.

A partir de aquí hice un archivo csv con dos columnas

============== ========
Nbrs           NAME10
-------------- --------
Amity          1412
West Rock      1413
Wooster Square 1421
Wooster Square 1422
 ...           ...
 ...           ... 
============== ========


.. note::  Vienen pronto los pasos restantes.
   Pero en la mientras ve el mapa abajo.

.. raw:: html 

  <div id="mapid"></div>   