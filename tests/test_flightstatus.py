#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
import datetime
import pytz

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

    def testTime(self):
        s = FlightStatus("A", "eagle flown")
        time = datetime.datetime.now(pytz.utc)
        s.set_time(time)

        self.assertEqual(s.get_time(), time)
        self.assertEqual(s.get_local_time(),
                         time.astimezone(pytz.timezone("Europe/Oslo")))


if __name__ == '__main__':
    unittest.main()
