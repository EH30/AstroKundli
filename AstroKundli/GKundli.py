import datetime
from FlatlibAstroSidereal.datetime import Datetime
from FlatlibAstroSidereal.geopos import GeoPos
from FlatlibAstroSidereal.chart import Chart, const

class GKundli:
    def __init__(self, year:int, month:int, day:int, hour:int, minute:int, utc:str, latitude:float, longitude:float, ayan="lahiri", useasc=True):
        """
        year: Birth Year
        month: Birth Month
        day: Birth Day
        house: Birth Hour
        minute: Birth Minute
        utc: Country UTC
        latitude: latitude
        longitude: longitude
        ayan: ayanamsa 
        useasc: const.ASC for first house if set to True else it will use const.HOUSE1
        Example: kundli = GKundli(1971,6, 28, 0, 0,"2:00", 25.7479, 28.2293)
        """
        self.year       = year
        self.month      = month
        self.day        = day
        self.hour       = hour
        self.minute     = minute
        self.utc        = utc
        self.latitude   = latitude
        self.longitude  = longitude
        self.ayan       = ayan.lower()
        self.usesasc    = useasc
        self.sign_names = {
            "aries": 1, "taurus": 2, "gemini": 3, "cancer": 4, "leo": 5, "virgo": 6, 
            "libra": 7, "scorpio": 8, "sagittarius": 9, "capricorn": 10, "aquarius": 11, "pisces":12
        }
        self.planets_name = {
            "<Sun":"Su", "<Moon":"Mo", "<Mars":"Ma", "<Jupiter":"Ju", "<Mercury":"Me", "<Saturn":"Sa",
            "<Venus":"Ve","<North":"Ra","<South":"Ke","<Pluto":"Pl","<Neptune":"Ne","<Uranus":"Ur",
        }
    
    def get_ayan(self):
        if self.ayan == "lahiri":
            return const.AY_LAHIRI
        elif self.ayan == "krishnamurti":
            return const.AY_KRISHNAMURTI
        elif self.ayan == "raman":
            return const.AY_RAMAN
        elif self.ayan == "fagan_bradley":
            return const.AY_FAGAN_BRADLEY
        elif self.ayan == "deluce":
            return const.AY_DELUCE
        elif self.ayan == "sassanian":
            return const.AY_SASSANIAN
        elif self.ayan == "aldebaran_1stau":
            return const.AY_ALDEBARAN_15TAU
        elif self.ayan == "galcenter_55ag":
            return const.AY_GALCENTER_5SAG
    
    def get_retrograde_planets_lagna(self):
        date = Datetime([self.year, self.month, self.day], ['+',self.hour, self.minute,0], "+"+self.utc)
        pos = GeoPos(self.latitude, self.longitude)
        chart = Chart(date, pos, IDs=const.LIST_OBJECTS, mode=self.get_ayan())
        planets = {
            "SUN":chart.get(const.SUN).isRetrograde(), "MOON":chart.get(const.MOON).isRetrograde(), "MARS":chart.get(const.MARS).isRetrograde(), "JUPITER":chart.get(const.JUPITER).isRetrograde(),
            "MERCURY":chart.get(const.MERCURY).isRetrograde(), "SATURN":chart.get(const.SATURN), "VENUS":chart.get(const.VENUS).isRetrograde(), "NORTH_NODE":chart.get(const.NORTH_NODE).isRetrograde(),
            "SOUTH_NODE":chart.get(const.SOUTH_NODE).isRetrograde(), "PLUTO":chart.get(const.PLUTO).isRetrograde(), "NEPTUNE":chart.get(const.NEPTUNE).isRetrograde(), "URANUS":chart.get(const.URANUS).isRetrograde()
        }
        output = []
        for planet in planets:
            if planets[planet] == True:
                output.append(planet)
        return output

    def lagnaChart(self):
        date = Datetime([self.year, self.month, self.day], ['+',self.hour, self.minute,0], "+"+self.utc)
        pos = GeoPos(self.latitude, self.longitude)
        chart = Chart(date, pos, IDs=const.LIST_OBJECTS, mode=self.get_ayan())
        ascendant  = str(chart.get(const.ASC)).split(" ")[2]
        kundli = {
            "1": {"sign_num":self.sign_names[str(chart.get(const.HOUSE1)).split(" ")[1].lower()], "asc":ascendant, "planets":{}},
            "2": {"sign_num":0, "planets":{}},
            "3": {"sign_num":0, "planets":{}},
            "4": {"sign_num":0, "planets":{}},
            "5": {"sign_num":0, "planets":{}},
            "6": {"sign_num":0, "planets":{}},
            "7": {"sign_num":0, "planets":{}},
            "8": {"sign_num":0, "planets":{}},
            "9": {"sign_num":0, "planets":{}},
            "10": {"sign_num":0, "planets":{}},
            "11": {"sign_num":0, "planets":{}},
            "12": {"sign_num":0, "planets":{}},
        }
        temp = self.sign_names[str(chart.get(const.ASC)).split(" ")[1].lower()]
        if not self.usesasc:
            temp = self.sign_names[str(chart.get(const.HOUSE1)).split(" ")[1].lower()]
        for i in range(2, 13):
            temp += 1
            if temp > 12:
                temp = 1
            kundli[str(i)]["sign_num"] = temp

        planets = [
            str(chart.get(const.SUN)).split(" "), str(chart.get(const.MOON)).split(" "), str(chart.get(const.MARS)).split(" "), str(chart.get(const.JUPITER)).split(" "),
            str(chart.get(const.MERCURY)).split(" "), str(chart.get(const.SATURN)).split(" "), str(chart.get(const.VENUS)).split(" "), str(chart.get(const.NORTH_NODE)).split(" "),
            str(chart.get(const.SOUTH_NODE)).split(" "), str(chart.get(const.PLUTO)).split(" "), str(chart.get(const.NEPTUNE)).split(" "), str(chart.get(const.URANUS)).split(" ")
        ]
        planets[7][1] = planets[7][2]
        planets[8][1] = planets[8][2] 
        for planet_item in planets:
            for house in kundli:
                if kundli[house]["sign_num"] == self.sign_names[planet_item[1].lower()]:
                    p_name = self.planets_name[planet_item[0]]
                    if p_name == "Ra" or p_name == "Ke":
                        kundli[house]["planets"][p_name] = planet_item[3]
                    else:
                        kundli[house]["planets"][p_name] = planet_item[2]
                    break
        
        return kundli
    
    def transitChart(self, kundli):
        houses = {
            "1": {"sign_num": 0, "asc": None, "planets": {}},
            "2": {"sign_num": 0, "asc": None, "planets": {}},
            "3": {"sign_num": 0, "asc": None, "planets": {}},
            "4": {"sign_num": 0, "asc": None, "planets": {}},
            "5": {"sign_num": 0, "asc": None, "planets": {}},
            "6": {"sign_num": 0, "asc": None, "planets": {}},
            "7": {"sign_num": 0, "asc": None, "planets": {}},
            "8": {"sign_num": 0, "asc": None, "planets": {}},
            "9": {"sign_num": 0, "asc": None, "planets": {}},
            "10": {"sign_num": 0, "asc": None, "planets": {}},
            "11": {"sign_num": 0, "asc": None, "planets": {}},
            "12": {"sign_num": 0, "asc": None, "planets": {}},
        }
        for item in kundli:
            houses[item]["sign_num"] = kundli[item]["sign_num"]
        
        transit = GKundli(
            int(datetime.datetime.now().strftime("%Y")), int(datetime.datetime.now().strftime("%m")), int(datetime.datetime.now().strftime("%d")), int(datetime.datetime.now().strftime("%H")),
              int(datetime.datetime.now().strftime("%M")), self.utc, self.latitude, self.longitude, self.ayan).lagnaChart()
        for house in transit:
            if house == "1" and len(transit[house]["asc"]) != 0:
                for item in houses:
                    if houses[item]["sign_num"] == transit[house]["sign_num"]:
                        houses[item]["asc"] = transit[house]["asc"] 
                        break
            
            if len(transit[house]["planets"]) != 0:
                for item in houses:
                    if houses[item]["sign_num"] == transit[house]["sign_num"]:
                        for planet in transit[house]["planets"]:
                            houses[item]["planets"][planet] = transit[house]["planets"][planet]
        return houses

