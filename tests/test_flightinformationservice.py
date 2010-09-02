#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.flightinformationservice import FlightInformationService
from flightinfo.airport import AirPort
from flightinfo.query import Query

class TestFlightInformationService(unittest.TestCase):
    def setUp(self):
        airport = AirPort("OSL", "Gardermoen Oslo")
        self.query = Query(airport)

    def testSimpleQueryString(self):
        v = FlightInformationService.generate_query_string(self.query)
        self.assertEqual(v, "airport=OSL")

    def testTimeBoxQueryString(self):
        self.query.time_to = 3
        v = FlightInformationService.generate_query_string(self.query)
        self.assertEqual(v, "airport=OSL&timeTo=3")

    def testDirectionDepartureQueryString(self):
        self.query.direction = Query.Directions.DEPARTURE
        v = FlightInformationService.generate_query_string(self.query)
        self.assertEqual(v, "airport=OSL&direction=D")

    def testDirectionArrivalQueryString(self):
        self.query.direction = Query.Directions.ARRIVAL
        v = FlightInformationService.generate_query_string(self.query)
        self.assertEqual(v, "airport=OSL&direction=A")


if __name__ == '__main__':
    unittest.main()
