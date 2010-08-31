import unittest
from test_airport import TestAirPort
from test_airline import TestAirline
from test_flight import TestFlight
from test_flightstatus import TestFlightStatus
from test_query import TestQuery

from test_flightparser import TestFlightParser
from test_airlineparser import TestAirlineParser
from test_flightstatusparser import TestFlightStatusParser
from test_flightinformationservice import TestFlightInformationService

def suite():
    """ This defines all the tests of a module"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAirPort))
    suite.addTest(unittest.makeSuite(TestAirline))
    suite.addTest(unittest.makeSuite(TestFlight))
    suite.addTest(unittest.makeSuite(TestFlightStatus))
    suite.addTest(unittest.makeSuite(TestQuery))
    suite.addTest(unittest.makeSuite(TestFlightParser))
    suite.addTest(unittest.makeSuite(TestFlightStatusParser))
    suite.addTest(unittest.makeSuite(TestFlightInformationService))
    suite.addTest(unittest.makeSuite(TestAirlineParser))

    return suite

if __name__ == '__main__':
   unittest.TextTestRunner(verbosity=3).run(suite())
