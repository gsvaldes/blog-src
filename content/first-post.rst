Mapping New Haven Neighborhoods
###############################

:date: 2016-11-14 7:32
:modified: 2016-12-17 12:30
:tags: random
:category: about
:slug: new-haven-neighborhoods
:lang: en
:authors: Geoffrey Valdes
:summary: Generating GeoJson for New Haven neighborhood boundaries
:javascripts: https://unpkg.com/leaflet@1.0.1/dist/leaflet.js, nh_map.js
:stylesheets: https://unpkg.com/leaflet@1.0.1/dist/leaflet.css, map.css

I moved to New Haven a few months ago.  As part of getting to know the city, I want to know the different neighborhoods and show them on a web-based map using Leaflet.  To do that I need to have the description of the neighborhood boundaries in the GeoJson format.  

For New Haven, this data is probably already available from `Data Haven <http://www.ctdatahaven.org/>`_ in a cleaned format, but I want to show the steps to do this for other locations.

Broadly, the steps are

* Find out how the neighborhoods are defined.

* Get a geospatial dataset that corresponds to the neighborhood definition.

* Convert the geospatial data to GeoJSON.

* Display the GeoJSON on a map using the Leaflet JavaScript Library.

The City of Austin, TX provides most of it's GIS shp files free online.  The City of New Haven does not appear to do the same.  It does, however have a city plan that shows the census tracts that correspond to each neighborhood: 

http://www.cityofnewhaven.com/cityplan/pdfs/PlanningPrograms/Demographics.pdf

As noted on another City of New Haven page, "Neighborhood boundaries are approximate and adjusted to coincide with the Census tracts.  There are no official neighborhood boundaries."

With the above information, I can now download the shp files of the Census tracts for the State of Connecticut, map a subset of them to the corresponding New Haven neighborhoods, and then convert that to a GeoJson file

The University of Connnecticut provides GIS data for the state
http://magic.lib.uconn.edu/connecticut_data.html

Spefically, from the Census - 2010 Boundary Files section you can download the Shapefiles for Connecticut Tracts and open this in qGIS.

In the qGIS layers panel, it displays as
``tractct_37800__0000_2010_s100_census_shp_wgs85wgs``

Opening up the attribute table for this layer, you could see that the NAME10 column contained the census tract number that corresponds to the tract numbers listed in the neighborhood map above.

From here I made a csv file with two columns

Make a csv file with two columns

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

.. note::  The rest of the steps to come soon
   But see the map below.

.. raw:: html 

  <div id="mapid"></div>

