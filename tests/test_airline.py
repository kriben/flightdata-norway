#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 

import unittest
from flightinfo.airline import Airline


class TestAirline(unittest.TestCase):
    def testBasic(self):
        code = "WF"
        name =  "Widerøe"
        a = Airline(code, name)
        self.assertEqual(a.code, code)
        self.assertEqual(a.name, name)


if __name__ == '__main__':
    unittest.main()
