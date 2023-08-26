"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for computing 
    the almutem protocol.

"""

from FlatlibAstroSidereal import const
from FlatlibAstroSidereal.chart import Chart
from FlatlibAstroSidereal.datetime import Datetime
from FlatlibAstroSidereal.geopos import GeoPos
from FlatlibAstroSidereal.protocols import almutem


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Print almutem scores
alm = almutem.compute(chart)
for k, v in alm['Score'].items():
    print(k, v)  # Mercury scores 40