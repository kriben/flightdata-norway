#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airlineparser import AirlineParser
from flightinfo.airline import Airline


class TestAirlineParser(unittest.TestCase):
    def testTrondheimData(self):
        xml_data = open("testdata/shortairlinelist.xml").read()
        
        airlines = AirlineParser.parse_airlines(xml_data)
        self.assertEqual(3, len(airlines))
        
        expected = [ ("AA", "American Airlines"),
                     ("DL","Delta Airlines"),
                     ("DY", "Norwegian") ]

        for e, a in zip(expected, airlines):
            self.assertEqual(e[0], a.code)
            self.assertEqual(e[1], a.name)

    def testRealisticData(self):
        xml_data = open("testdata/airlinenames.xml").read()
        
        airlines = AirlineParser.parse_airlines(xml_data)
        self.assertEqual(709, len(airlines))
