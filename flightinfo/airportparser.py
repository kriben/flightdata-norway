import xml.etree.ElementTree as ET 
from airport import AirPort

class AirPortParser(object):
    """
    Utility for parsing airport information from an XML files.

    """

    @staticmethod 
    def parse_airports(xml_file):
        """ 
        Parses airport information from an XML file.
        
        Returns a list of airports.
        """

        tree = ET.XML(xml_file)
        airports = []
        for node in tree.getiterator('airportName'):
            code = node.attrib.get("code")
            name = node.attrib.get("name")
            airports.append(AirPort(code, name))

        return airports
