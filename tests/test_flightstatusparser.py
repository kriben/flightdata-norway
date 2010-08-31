#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.flightstatus import FlightStatus
from flightinfo.flightstatusparser import FlightStatusParser

class TestFlightStatusParser(unittest.TestCase):
    def testXml(self):
        xml_data = open("testdata/flightStatuses.xml").read()
        
        statuses = FlightStatusParser.parseStatuses(xml_data)
        self.assertEqual(5, len(statuses))
        
        expected = [ ("N", "New info"),
                     ("E", "New time"),
                     ("D", "Departed"),
                     ("A", "Arrived"),
                     ("C", "Cancelled"), ] 

        for e, s in zip(expected, statuses):
            self.assertEqual(e[0], s.code)
            self.assertEqual(e[1], s.text)


if __name__ == '__main__':
    unittest.main()
