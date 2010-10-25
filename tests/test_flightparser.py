#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airline import Airline
from flightinfo.airlinefactory import AirlineFactory
from flightinfo.airportfactory import AirPortFactory
from flightinfo.airport import AirPort
from flightinfo.flight import Flight
from flightinfo.flightparser import FlightParser
from flightinfo.flightstatusfactory import FlightStatusFactory
from flightinfo.flightstatus import FlightStatus

class MockAirlineFactory(AirlineFactory):
    def __init__(self):
        pass
    
    def get_airline_by_code(self, code):
        if code == "BGT":
            return Airline("BGT", "Bergen Air Transport")
        else:
            return Airline("SK", "SAS")

class MockAirPortFactory(AirPortFactory):
    def __init__(self):
        pass

    def get_airport_by_code(self, code):
        if code == "OSL":
            return AirPort("OSL", "Gardermoen")
        else:
            return AirPort("BNN", "Bergen")
        
class MockFlightStatusFactory(FlightStatusFactory):
    def __init__(self):
        pass
    
    def get_flight_status_by_code(self, code):
        if code == "D":
            return FlightStatus("D", "Departed")
        else:
            return FlightStatus("E", "New time")
        
    


class TestFlightParser(unittest.TestCase):

    def testTrondheimData(self):
        xml_data = open("testdata/trondheimflights.xml").read()
        
        flights = FlightParser.parse_flights(xml_data, 
                                             MockAirlineFactory(),
                                             MockAirPortFactory(),
                                             MockFlightStatusFactory())
        self.assertEqual(2, len(flights))

        flight1 = flights[0]
        self.assertEqual("1170765", flight1.unique_id) 
        self.assertEqual("BGT073", flight1.flight_id)
        self.assertEqual("BGT", flight1.airline.code)
        self.assertEqual("BNN", flight1.airport.code)
        self.assertEqual(Flight.Directions.ARRIVAL, flight1.direction)
        self.assertEqual("3", flight1.belt)
        self.assertEqual("E", flight1.status[0].code)

        flight2 = flights[1]
        self.assertEqual("1176338", flight2.unique_id)
        self.assertEqual("SK381", flight2.flight_id)
        self.assertEqual("SK", flight2.airline.code)
        self.assertEqual("OSL", flight2.airport.code)
        self.assertEqual(Flight.Directions.DEPARTURE, flight2.direction)
        self.assertEqual("EF", flight2.check_in)
        self.assertEqual("32", flight2.gate)
        self.assertEqual("D", flight2.status[0].code)

if __name__ == '__main__':
    unittest.main()
