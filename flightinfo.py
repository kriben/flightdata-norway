#!/usr/bin/python
# -*- coding: latin-1 -*-

import urllib2
import urllib
import unittest

class AirPort(object):
    def __init__(self, code, name):
        self.code = code
        self.name = name

class TestAirPort(unittest.TestCase):
    def testBasic(self):
        code = "TRD"
        name = 'Trondheim - Værnes'
        a = AirPort(code, name)

        self.assertEqual(a.code, code)
        self.assertEqual(a.name, name)


class Flight:
    def __init__(self, unique_id, flight_id):
        self.unique_id = unique_id
        self.flight_id = flight_id

class TestFlight(unittest.TestCase):
    def testBasic(self):
        unique_id = "12345434"
        flight_id = "SK123"
        f = Flight(unique_id, flight_id)
        
        self.assertEqual(unique_id, f.unique_id)
        self.assertEqual(flight_id, f.flight_id)


class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError



Directions = Enum(["DEPARTURE", "ARRIVAL"])

class Query(object):
    def __init__(self, airport):
        self.airport = airport
        self.time_from = None
        self.time_to = None
        self.last_update = None
        self.direction = None

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

class FlightInformationService(object):

    @staticmethod 
    def generateQueryString(query):
        data = {}
        data["airport"] = query.airport.code
        if query.time_from:
            data["timeFrom"] = query.time_from

        if query.time_to:
            data["timeTo"] = query.time_to

        if query.direction:
            conversion = { Directions.DEPARTURE : "D",
                           Directions.ARRIVAL : "A" }
            data["direction"] = conversion[query.direction]

        return urllib.urlencode(data)


class TestFlightInformationService(unittest.TestCase):
    def setUp(self):
        airport = AirPort("OSL", "Gardermoen Oslo")
        self.query = Query(airport)

    def testSimpleQueryString(self):
        v = FlightInformationService.generateQueryString(self.query)
        self.assertEqual(v, "airport=OSL")

    def testTimeBoxQueryString(self):
        self.query.time_to = 3
        v = FlightInformationService.generateQueryString(self.query)
        self.assertEqual(v, "airport=OSL&timeTo=3")

    def testDirectionDepartureQueryString(self):
        self.query.direction = Directions.DEPARTURE
        v = FlightInformationService.generateQueryString(self.query)
        self.assertEqual(v, "airport=OSL&direction=D")

    def testDirectionArrivalQueryString(self):
        self.query.direction = Directions.ARRIVAL
        v = FlightInformationService.generateQueryString(self.query)
        self.assertEqual(v, "airport=OSL&direction=A")

        

#data = {}
#data['airport'] = 'TRD'
#data['direction'] = 'D'
#url_values = urllib.urlencode(data)

#print url_values

#url = "http://flydata.avinor.no/XmlFeed.asp"
#full_url = url + '?' + url_values

#response = urllib2.urlopen(full_url)

#xml = response.read()





#print xml

if __name__ == '__main__':
    unittest.main()



