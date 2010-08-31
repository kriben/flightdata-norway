#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.flightstatus import FlightStatus

class TestFlightStatus(unittest.TestCase):
    def testBasic(self):
        code = "E"
        text = "New time"
        s = FlightStatus(code, text)
        self.assertEqual(s.code, code)
        self.assertEqual(s.text, text)

if __name__ == '__main__':
    unittest.main()
