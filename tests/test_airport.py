#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airport import AirPort
from flightinfo.position import Position

class TestAirPort(unittest.TestCase):
    def testBasic(self):
        code = "TRD"
        name = 'Trondheim - Værnes'
        a = AirPort(code, name)

        self.assertEqual(a.code, code)
        self.assertEqual(a.name, name)

    def testPosition(self):
        a = AirPort("EVE", "Evenes - Harstad/Narvik")
        latitude = 68.49111
        longitude = 16.68057
        a.position = Position(latitude, longitude)
        
        self.assertEqual(latitude, a.position.latitude)
        self.assertEqual(longitude, a.position.longitude)

if __name__ == '__main__':
    unittest.main()
