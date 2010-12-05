#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airport import AirPort
from flightinfo.airportfactory import AirPortFactory
from flightinfo.position import Position

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

    def testGetNorwegianAirportsSorted(self):
        in_airports = [ AirPort("TRD", "Trondheim"),
                        AirPort("OSL", "Oslo"),
                        AirPort("OSY", "Namsos"),
                        AirPort("VDB", "Fagernes"),
                        AirPort("TRF", "Sandefjord") ]
        
        factory = AirPortFactory(in_airports)

        airports = factory.get_norwegian_airports()
        self.assertEqual(5, len(airports))

        # Should be sorted by the name (not the code)
        self.assertEqual(airports[0].code, "VDB")
        self.assertEqual(airports[1].code, "OSY")
        self.assertEqual(airports[2].code, "OSL")
        self.assertEqual(airports[3].code, "TRF")
        self.assertEqual(airports[4].code, "TRD")
        

                        
    def testGetClosestNorwegianAirport(self):
        
        trd = AirPort("TRD", "Trondheim")
        trd.position = Position(63.45943, 10.92621)

        eve = AirPort("EVE", "Harstad")
        eve.position = Position(68.49111, 16.68057)

        in_airports = [ trd, eve ]
         
        factory = AirPortFactory(in_airports)
        a = factory.get_closest_norwegian_airport(Position(63.41330, 10.35962))
        self.assertTrue("TRD", a.code)
        
    def testGetClosestNorwegianAirportEmptyList(self):
        in_airports = []
        factory = AirPortFactory(in_airports)

        a = factory.get_closest_norwegian_airport(Position(0.0, 1.0))
        self.assertTrue(a is None)


if __name__ == '__main__':
    unittest.main()
