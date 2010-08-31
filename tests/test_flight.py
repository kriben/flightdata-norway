#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airline import Airline
from flightinfo.flight import Flight

class TestFlight(unittest.TestCase):
    def testBasic(self):
        unique_id = "12345434"
        flight_id = "SK123"
        airline = Airline("WF", "Widerøe")
        f = Flight(unique_id, flight_id, airline)
        
        self.assertEqual(unique_id, f.unique_id)
        self.assertEqual(flight_id, f.flight_id)
        self.assertEqual(airline, f.airline)

if __name__ == '__main__':
    unittest.main()
