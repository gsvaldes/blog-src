Mapping New Haven Neighborhoods
###############################

:date: 2016-11-14 7:32
:tags: random
:category: about
:slug: new-haven-neighborhoods
:lang: en
:authors: Geoffrey Valdes
:summary: Generating GeoJson for New Haven neighborhood boundaries
:javascripts: https://unpkg.com/leaflet@1.0.1/dist/leaflet.js, nh_map.js
:stylesheets: https://unpkg.com/leaflet@1.0.1/dist/leaflet.css, map.css

I moved to New Haven a few months ago.  As part of getting to know the city, I want to know the different neighborhoods and represent them on a web-based map.  To do that I'd like to have the neighborhood boundaries represented as GeoJson.  

The City of Austin, TX provides most of it's GIS shp files free online.  The City of New Haven does not appear to do the same.  It does, however have a map that shows the census tracts that correspond to each neighborhood

http://www.cityofnewhaven.com/Library/maps/neighborhoods.gif

As noted in the above link, "Neighborhood boundaries are approximate and adjusted to coincide with the Census tracts.  There are no official neighborhood boundaries."

With the above information, I can now download the shp files of the Census tracts for the State of Connecticut, map a subset of them to the corresponding New Haven neighborhoods, and then convert that to a GeoJson file

The University of Connnecticut provides GIS data for the state
http://magic.lib.uconn.edu/connecticut_data.html

Spefically, from the Census - 2010 Boundary Files section I downloaded the Shapefiles for Connecticut Tracts and then opened this in qQIS.

In the qGIS layers panel, it displays as
tractct_37800__0000_2010_s100_census_shp_wgs85wgs

Opening up the attribute table for this layer, I could see that the NAME10 column contained the census tract number that corresponds to the tract numbers listed in the neighborhood map above.

Make a csv file with two columns

============== ========
Nbrs           NAME10
-------------- --------
Amity          1412
West Rock      1413
Wooster Square 1421
Wooster Square 1422
 ...           ...
============== ========

.. note::  The rest of the steps to come soon
   But see the map below.

.. raw:: html 

  <div id="mapid"></div>

