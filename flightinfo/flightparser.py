""" FlightParser: Utility for parsing flights from XML """
import xml.etree.ElementTree as ET 
import datetime
from flight import Flight
from flightstatus import FlightStatus
from airline import Airline
from airport import AirPort

try:
    from pytz.gae import pytz
except:
    import pytz

class FlightParser(object):
    """
    Utility for parsing flights from XML.

    """

    @staticmethod 
    def convert_to_utc(time_string):
        pattern = "%Y-%m-%dT%H:%M:%S"
        return pytz.utc.localize(datetime.datetime.strptime(time_string,
                                                            pattern))

    @staticmethod
    def parse_flights(xml_file, airline_factory, airport_factory, 
                      flight_status_factory):
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
            schedule_time = FlightParser.convert_to_utc(schedule_time_string)
            
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

            ## Status 
            status_node = node.find("status")
            if status_node != None:
                status_code = status_node.attrib.get("code")
                status_time = status_node.attrib.get("time")
                
                flight_status = flight_status_factory.get_flight_status_by_code(status_code)
                if status_time != None:
                    flight_status.set_time(FlightParser.convert_to_utc(status_time))
                optionals["status"] = flight_status
                
            try:
                airline = airline_factory.get_airline_by_code(airline_code)
            except KeyError:
                airline = Airline(airline_code, "Unknown airline")

            try:
                airport = airport_factory.get_airport_by_code(airport_code)
            except KeyError:
                airport = AirPort(airport_code, "Unknown airport")

            flight = Flight(unique_id, flight_id, airline, airport, 
                            schedule_time, direction, **optionals)
            flights.append(flight)

        return flights
