#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airport import AirPort
from flightinfo.airportfactory import AirPortFactory

def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for item in seq:
        if f(item): 
            return item

class TestAirPortFactory(unittest.TestCase):
    def testGetNorwegianAirports(self):

        in_airports = [ AirPort("TRD", "Trondheim"),
                        AirPort("CPH", "Copenhagen") ]
        
        factory = AirPortFactory(in_airports)

        airports = factory.get_norwegian_airports() 
        
        self.assertEqual(1, len(airports))
        
        self.assertTrue(find(lambda a: a.code == 'TRD', airports))
        self.assertFalse(find(lambda a: a.code == 'CPH', airports))
        

if __name__ == '__main__':
    unittest.main()
