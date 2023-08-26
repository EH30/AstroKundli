"""
    Author: João Ventura <flatangleweb@gmail.com>


    This recipe shows sample code for creating a chart
    with sidereal zodiac

"""

from FlatlibAstroSidereal import const
from FlatlibAstroSidereal.chart import Chart
from FlatlibAstroSidereal.datetime import Datetime
from FlatlibAstroSidereal.geopos import GeoPos

# Build a chart for a date and location
date = Datetime('2015/03/13', '17:00', '+00:00')
pos = GeoPos('38n32', '8w54')
chart = Chart(date, pos, mode=const.AY_KRISHNAMURTI)

# Get objects and houses from the chart
sun = chart.get(const.SUN)
house3 = chart.get(const.HOUSE3)
