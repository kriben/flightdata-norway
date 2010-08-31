#!/usr/bin/python
# -*- coding: latin-1 -*-

import urllib2
import urllib
import unittest
import datetime
from pytz import timezone
import pytz





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

class Airline(object):
    def __init__(self, code, name):
        self.code = code
        self.name = name

class TestAirline(unittest.TestCase):
    def testBasic(self):
        code = "WF"
        name =  "Widerøe"
        a = Airline(code, name)
        self.assertEqual(a.code, code)
        self.assertEqual(a.name, name)

class FlightStatus(object):
    def __init__(self, code, text):
        self.code = code
        self.text = text
    
class TestFlightStatus(unittest.TestCase):
    def testBasic(self):
        code = "E"
        text =  "New time"
        s = FlightStatus(code, text)
        self.assertEqual(s.code, code)
        self.assertEqual(s.text, text)


class Flight:
    def __init__(self, unique_id, flight_id, airline):
        self.unique_id = unique_id
        self.flight_id = flight_id
        self.airline = airline

class TestFlight(unittest.TestCase):
    def testBasic(self):
        unique_id = "12345434"
        flight_id = "SK123"
        airline = Airline("WF", "Widerøe")
        f = Flight(unique_id, flight_id, airline)
        
        self.assertEqual(unique_id, f.unique_id)
        self.assertEqual(flight_id, f.flight_id)
        self.assertEqual(airline, f.airline)


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

import xml.etree.ElementTree as ET 

class AirlineFactory(object):
    def __init__(self):
        pass

    def getAirlineByCode(self, code):
        return Airline("WF", "Wideroe")


class MockAirlineFactory(AirlineFactory):
    
    def getAirlineByCode(self, code):
        if code == "BGT":
            return Airline("BGT", "Bergen Air Transport")
        else:
            return Airline("SK", "SAS")


class FlightParser(object):
    @staticmethod 
    def parseFlights(xml_file, airline_factory):
        tree = ET.XML(xml_file)

        flights = []

        for node in tree.getiterator('flight'):
            unique_id = node.attrib.get("uniqueID")
            flight_id = node.find("flight_id").text
            airline_code = node.find("airline").text
            schedule_time_string = node.find("schedule_time").text
            schedule_time = datetime.datetime.strptime(schedule_time_string, "%Y-%m-%dT%H:%M:%S" )

            print schedule_time.tzname()
            oslo_tz = timezone('Europe/Oslo')

            local_schedule_time = oslo_tz.localize(schedule_time)
            print ("UTC: %s") %  schedule_time
            print ("LOCAL: %s") % local_schedule_time

            airline = airline_factory.getAirlineByCode(airline_code)
            flight = Flight(unique_id, flight_id, airline)
#            for child in node.getchildren():
#                if child.text:
#                    print child.tag + ": " + child.text
            flights.append(flight)

        return flights


class TestFlightParser(unittest.TestCase):

    def testTrondheimData(self):
        xml_data = open("testdata/trondheimflights.xml").read()
        
        flights = FlightParser.parseFlights(xml_data, MockAirlineFactory())
        self.assertEqual(2, len(flights))

        flight1 = flights[0]
        self.assertEqual("1170765", flight1.unique_id) 
        self.assertEqual("BGT073", flight1.flight_id)
        self.assertEqual("BGT", flight1.airline.code)

        flight2 = flights[1]
        self.assertEqual("1176338", flight2.unique_id)
        self.assertEqual("SK381", flight2.flight_id)
        self.assertEqual("SK", flight2.airline.code)
        
class AirlineParser(object):
    @staticmethod 
    def parseAirlines(xml_file):
        tree = ET.XML(xml_file)

        airlines = []
        for node in tree.getiterator('airlineName'):
            code = node.attrib.get("code")
            name = node.attrib.get("name")
            airlines.append(Airline(code, name))

        return airlines

class TestAirlineParser(unittest.TestCase):
    def testTrondheimData(self):
        xml_data = open("testdata/shortairlinelist.xml").read()
        
        airlines = AirlineParser.parseAirlines(xml_data)
        self.assertEqual(3, len(airlines))
        
        expected = [ ("AA", "American Airlines"),
                     ("DL","Delta Airlines"),
                     ("DY", "Norwegian") ]

        for e, a in zip(expected, airlines):
            self.assertEqual(e[0], a.code)
            self.assertEqual(e[1], a.name)

    def testRealisticData(self):
        xml_data = open("testdata/airlinenames.xml").read()
        
        airlines = AirlineParser.parseAirlines(xml_data)
        self.assertEqual(709, len(airlines))


class FlightStatusParser(object):
    @staticmethod 
    def parseStatuses(xml_file):
        tree = ET.XML(xml_file)

        statuses = []
        for node in tree.getiterator('flightStatus'):
            code = node.attrib.get("code")
            text = node.attrib.get("statusTextEn")
            statuses.append(FlightStatus(code, text))

        return statuses


class TestFlightStatusParser(unittest.TestCase):
    def testXml(self):
        xml_data = open("testdata/flightStatuses.xml").read()
        
        statuses = FlightStatusParser.parseStatuses(xml_data)
        self.assertEqual(5, len(statuses))
        
        expected = [ ("N", "New info"),
                     ("E", "New time"),
                     ("D", "Departed"),
                     ("A", "Arrived"),
                     ("C", "Cancelled"), ] 

        for e, s in zip(expected, statuses):
            self.assertEqual(e[0], s.code)
            self.assertEqual(e[1], s.text)



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



