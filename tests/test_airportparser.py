#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airportparser import AirPortParser
from flightinfo.airport import AirPort


class TestAirPortParser(unittest.TestCase):

    def testRealisticData(self):
        xml_data = open("testdata/airportNames.xml").read()
        
        airports = AirPortParser.parse_airports(xml_data)
        self.assertEqual(1932, len(airports))
