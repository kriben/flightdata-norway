import xml.etree.ElementTree as ET 
from flightstatus import FlightStatus

class FlightStatusParser(object):
    @staticmethod 
    def parseStatuses(xml_file):
        tree = ET.XML(xml_file)

        statuses = []
        for node in tree.getiterator('flightStatus'):
            code = node.attrib.get("code")
            text = node.attrib.get("statusTextEn")
            statuses.append(FlightStatus(code, text))

        return statuses
