#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airport import AirPort
from flightinfo.query import Query


class TestQuery(unittest.TestCase):
    def testBasic(self):
        airport = AirPort("OSL", "Gardermoen Oslo")
        query = Query(airport)
        
        self.assertEqual(query.airport, airport)                         
        self.assertEqual(query.time_from, None)
        self.assertEqual(query.time_to, None)
        self.assertEqual(query.last_update, None)
        self.assertEqual(query.direction, None)
        
    def testTime(self):
        airport = AirPort("EVE", "Evenes")
        query = Query(airport)
        query.time_from = 2
        query.time_to = 20
        
        self.assertEqual(query.time_from, 2)
        self.assertEqual(query.time_to, 20)


if __name__ == '__main__':
    unittest.main()
