#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.position import Position
from math import fabs


class TestPosition(unittest.TestCase):
    def testBasic(self):
        latitude = 12.3
        longitude = 156.09
        p = Position(latitude, longitude)

        self.assertEqual(latitude, p.latitude)
        self.assertEqual(longitude, p.longitude)

    def testPositionToSamePositionDistance(self):
        positions = [ Position(0.0, 0.0), 
                      Position(100.0, 50.9), 
                      Position(140.0, -134.0) ]

        for p in positions:
            self.assertAlmostEqual(0.0, p.compute_distance_to(p))

    def testPositionToPositionDistance(self):
        positions = [ 
            (Position(63.430487, 10.395061), 
             Position(59.912726, 10.746092), 392.033),
            (Position(62.098502, 10.541898), 
             Position(63.430487, 10.395061), 148.023)]

        for p in positions:
            # check that computing both ways give the same result
            delta = 3
            self.assertTrue(fabs(p[0].compute_distance_to(p[1]) - p[2]) < delta)
            self.assertTrue(fabs(p[1].compute_distance_to(p[0]) - p[2]) < delta)
            
    def testPositionExample(self):
        # Test data from http://williams.best.vwh.net/avform.htm
        lax = Position(33.942522, -118.407161)
        jfk = Position(40.639751, -73.778926)

        # fr
        meters = 2149.0 * 1.852
        delta = 10.0
        self.assertTrue(fabs(lax.compute_distance_to(jfk) - meters) < delta) 
        self.assertTrue(fabs(jfk.compute_distance_to(lax) - meters) < delta)


if __name__ == '__main__':
    unittest.main()
