#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
import datetime
import pytz
from flightinfo.airline import Airline
from flightinfo.airport import AirPort
from flightinfo.flight import Flight

class TestFlight(unittest.TestCase):
    def testBasic(self):
        unique_id = "12345434"
        flight_id = "SK123"
        airline = Airline("WF", "Widerøe")
        airport = AirPort("TRD", "Trondheim")
        schedule_time = datetime.datetime.now()
        direction = Flight.Directions.ARRIVAL
        f = Flight(unique_id, flight_id, airline, airport, schedule_time, 
                   direction)
        
        self.assertEqual(unique_id, f.unique_id)
        self.assertEqual(flight_id, f.flight_id)
        self.assertEqual(airline, f.airline)
        self.assertEqual(airport, f.airport)
        self.assertEqual(schedule_time, f.schedule_time)
        self.assertEqual(direction, f.direction)

    def testLocalTime(self):
        unique_id = "12345434"
        flight_id = "SK123"
        airline = Airline("WF", "Widerøe")
        airport = AirPort("TRD", "Trondheim")
        schedule_time = datetime.datetime.now(pytz.utc)
        direction = Flight.Directions.DEPARTURE
        f = Flight(unique_id, flight_id, airline, airport, schedule_time,
                   direction)

        self.assertEqual(schedule_time, f.get_local_schedule_time())




if __name__ == '__main__':
    unittest.main()
