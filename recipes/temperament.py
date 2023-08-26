"""
    Author: João Ventura <flatangleweb@gmail.com>
    
    
    This recipe shows sample code for computing 
    the temperament protocol.

"""

from FlatlibAstroSidereal import const
from FlatlibAstroSidereal.chart import Chart
from FlatlibAstroSidereal.datetime import Datetime
from FlatlibAstroSidereal.geopos import GeoPos
from FlatlibAstroSidereal.protocols.temperament import Temperament


# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos)

# Temperament
temperament = Temperament(chart)

# Print temperament factors
factors = temperament.getFactors()
for factor in factors:
    print(factor)
    
# Print temperament modifiers
modifiers = temperament.getModifiers()
for modifier in modifiers:
    print(modifier)
    
# Print temperament scores
score = temperament.getScore()
print(score)