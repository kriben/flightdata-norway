#!/usr/bin/python
# -*- coding: latin-1 -*-

import sys
sys.path.append('../') 
import urllib2
from optparse import OptionParser
from flightinfo.airlinefactory import AirlineFactory
from flightinfo.airlineparser import AirlineParser
from flightinfo.airport import AirPort
from flightinfo.airportfactory import AirPortFactory
from flightinfo.airportparser import AirPortParser
from flightinfo.flight import Flight
from flightinfo.flightinformationservice import FlightInformationService
from flightinfo.flightparser import FlightParser
from flightinfo.query import Query

parser = OptionParser()
parser.add_option("--departures", action="store_true", dest="departures_only", 
                  help="Print information about only departures.", 
                  default=False)
parser.add_option("--arrivals", action="store_true", dest="arrivals_only", 
                  help="Print information about only arrivals.", default=False)


(options, args) = parser.parse_args()
airportname = args[0]


airports_xml = FlightInformationService.download_airport_xml()
airports = AirPortParser.parse_airports(airports_xml)
airport_factory = AirPortFactory(airports)

airlines_xml = FlightInformationService.download_airline_xml()
airlines = AirlineParser.parse_airlines(airlines_xml)
airline_factory = AirlineFactory(airlines)

airport = airport_factory.get_airport_by_code(airportname)
query = Query(airport)
xml = FlightInformationService.download_flight_xml(query)

flights = FlightParser.parse_flights(xml, airline_factory, airport_factory)

def is_departure(flight):
    return flight.direction == Flight.Directions.DEPARTURE

def is_arrival(flight):
    return flight.direction == Flight.Directions.ARRIVAL

print "Flight information for %s (%s)" % (airport.name, airport.code)

if not options.arrivals_only:
    print "\nDepartures:"
    for f in filter(is_departure, flights):
        print f

if not options.departures_only:
    print "\nArrivals:"
    for f in filter(is_arrival, flights):
        print f


