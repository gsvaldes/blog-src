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

* Dibujar los barrios en un mapa web usando el GeoJSON y Leaflet, una biblioteca de JavaScript

.. note::  Ya mero viene la traducción.
   Pero en la mientras ve el mapa abajo.

.. raw:: html 

  <div id="mapid"></div>   