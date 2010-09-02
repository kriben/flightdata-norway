""" FlightParser: Utility for parsing flights from XML """
import xml.etree.ElementTree as ET 
#import datetime
#from pytz import timezone

from flight import Flight
#from airlinefactory import AirlineFactory

class FlightParser(object):
    """
    Utility for parsing flights from XML.

    """

    @staticmethod 
    def parse_flights(xml_file, airline_factory):
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
#            schedule_time_string = node.find("schedule_time").text
#            schedule_time = datetime.datetime.strptime(schedule_time_string, 
#            "%Y-%m-%dT%H:%M:%S" )

#            print schedule_time.tzname()
#            oslo_tz = timezone('Europe/Oslo')

#            local_schedule_time = oslo_tz.localize(schedule_time)
#            print ("UTC: %s") %  schedule_time
#            print ("LOCAL: %s") % local_schedule_time

            airline = airline_factory.getAirlineByCode(airline_code)
            flight = Flight(unique_id, flight_id, airline)
            flights.append(flight)

        return flights
