import xml.etree.ElementTree as ET 
from airline import Airline

class AirlineParser(object):
    @staticmethod 
    def parseAirlines(xml_file):
        tree = ET.XML(xml_file)

        airlines = []
        for node in tree.getiterator('airlineName'):
            code = node.attrib.get("code")
            name = node.attrib.get("name")
            airlines.append(Airline(code, name))

        return airlines
