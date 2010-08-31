#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airport import AirPort

class TestAirPort(unittest.TestCase):
    def testBasic(self):
        code = "TRD"
        name = 'Trondheim - Værnes'
        a = AirPort(code, name)

        self.assertEqual(a.code, code)
        self.assertEqual(a.name, name)

if __name__ == '__main__':
    unittest.main()
