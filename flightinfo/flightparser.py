""" FlightParser: Utility for parsing flights from XML """
import xml.etree.ElementTree as ET 
import datetime
import pytz
#from pytz import timezone

from flight import Flight

class FlightParser(object):
    """
    Utility for parsing flights from XML.

    """

    @staticmethod 
    def parse_flights(xml_file, airline_factory, airport_factory):
        """ 
        Parses the flights from the given xml.

        Returns a list of flights.

        """

        tree = ET.XML(xml_file)
        flights = []
        for node in tree.getiterator('flight'):
            unique_id = node.attrib.get("uniqueID")
            flight_id = node.find("flight_id").text
            airline_code = node.find("airline").text
            airport_code = node.find("airport").text
            schedule_time_string = node.find("schedule_time").text
            schedule_time = pytz.utc.localize(
                datetime.datetime.strptime(schedule_time_string, 
                                           "%Y-%m-%dT%H:%M:%S"))
            arr_dep_string = node.find("arr_dep").text
            arr_dep_mapping = { "A" : Flight.Directions.ARRIVAL,
                                "D" : Flight.Directions.DEPARTURE }
            direction = arr_dep_mapping[arr_dep_string]

            ## Optional arguments
            args = [ "belt", "check_in", "gate" ]
            optionals = {}
            for a in args:
                anode = node.find(a)
                if anode != None:
                    optionals[a] = anode.text

            airline = airline_factory.get_airline_by_code(airline_code)
            airport = airport_factory.get_airport_by_code(airport_code)
            flight = Flight(unique_id, flight_id, airline, airport, 
                            schedule_time, direction, **optionals)
            flights.append(flight)

        return flights
