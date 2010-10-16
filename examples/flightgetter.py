#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 
import urllib2

from flightinfo.airlinefactory import AirlineFactory
from flightinfo.airlineparser import AirlineParser
from flightinfo.airport import AirPort
from flightinfo.airportfactory import AirPortFactory
from flightinfo.airportparser import AirPortParser
from flightinfo.flight import Flight
from flightinfo.flightinformationservice import FlightInformationService
from flightinfo.flightparser import FlightParser
from flightinfo.query import Query


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

def is_departure(flight):
    return flight.direction == Flight.Directions.DEPARTURE

def is_arrival(flight):
    return flight.direction == Flight.Directions.ARRIVAL

print "\nDepartures:"
for f in filter(is_departure, flights):
    print f

print "\nArrivals:"
for f in filter(is_arrival, flights):
    print f


