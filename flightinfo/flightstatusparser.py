import xml.etree.ElementTree as ET 
from flightstatus import FlightStatus

class FlightStatusParser(object):
    """
    Utility for parsing messages from a given XML file.

    """

    @staticmethod 
    def parse_statuses(xml_file):
        """
        Parses the status messages from a given XML file.
        
        Returns a list of the statuses.
        """

        tree = ET.XML(xml_file)

        statuses = []
        for node in tree.getiterator('flightStatus'):
            code = node.attrib.get("code")
            text = node.attrib.get("statusTextEn")
            statuses.append(FlightStatus(code, text))

        return statuses
