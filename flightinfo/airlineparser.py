import xml.etree.ElementTree as ET 
from airline import Airline

class AirlineParser(object):
    """
    Utility for parsing airline information from an XML files.

    """

    @staticmethod 
    def parse_airlines(xml_file):
        """ 
        Parses airline information from an XML file.
        
        Returns a list of airlines.
        """

        tree = ET.XML(xml_file)
        airlines = []
        for node in tree.getiterator('airlineName'):
            code = node.attrib.get("code")
            name = node.attrib.get("name")
            airlines.append(Airline(code, name))

        return airlines
