#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airline import Airline
from flightinfo.airlinefactory import AirlineFactory


class TestAirlineFactory(unittest.TestCase):
    def testGetAirlines(self):

        in_airlines = [ Airline("SK", "Scandinavian"),
                        Airline("DY", "Norwegian") ]
        
        factory = AirlineFactory(in_airlines)

        sas = factory.get_airline_by_code("SK")
        norwegian = factory.get_airline_by_code("DY")

        self.assertEqual(sas.code, "SK")
        self.assertEqual(norwegian.code, "DY")

if __name__ == '__main__':
    unittest.main()
