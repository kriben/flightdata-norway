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
from flightinfo.airlinefactory import AirlineFactory


airlines_xml = open("../tests/testdata/airlinenames.xml").read()
airlines = AirlineParser.parse_airlines(airlines_xml)
airline_factory = AirlineFactory(airlines)


airport = AirPort("TRD", "Trondheim")
query = Query(airport)

url = "http://flydata.avinor.no/XmlFeed.asp?" + \
  FlightInformationService.generate_query_string(query)

response = urllib2.urlopen(url)
xml = response.read()


flights = FlightParser.parse_flights(xml, airline_factory)
for f in flights:
    print f


print xml
