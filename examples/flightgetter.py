#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 
import urllib2

from flightinfo.query import Query
from flightinfo.airport import AirPort
from flightinfo.flightinformationservice import FlightInformationService
from flightinfo.flightparser import FlightParser
from flightinfo.airlineparser import AirlineParser
from flightinfo.airportparser import AirPortParser
from flightinfo.airlinefactory import AirlineFactory
from flightinfo.airportfactory import AirPortFactory


airports_xml = FlightInformationService.download_airport_xml()
airports = AirPortParser.parse_airports(airports_xml)
airport_factory = AirPortFactory(airports)

airlines_xml = FlightInformationService.download_airline_xml()
airlines = AirlineParser.parse_airlines(airlines_xml)
airline_factory = AirlineFactory(airlines)

airport = AirPort("TRD", "Trondheim")
query = Query(airport)
xml = FlightInformationService.download_flight_xml(query)

flights = FlightParser.parse_flights(xml, airline_factory, airport_factory)
for f in flights:
    print f

print xml
