import urllib
from query import Query
from flight import Flight
import urllib2

class FlightInformationService(object):
    """
    Utility for converting a Query object into a query string (part of the url).

    """

    @staticmethod 
    def generate_query_string(query):
        """
        Generates the query part of the url.

        """

        data = {}
        data["airport"] = query.airport.code
        if query.time_from:
            data["timeFrom"] = query.time_from

        if query.time_to:
            data["timeTo"] = query.time_to

        if query.direction:
            conversion = { Flight.Directions.DEPARTURE : "D",
                           Flight.Directions.ARRIVAL : "A" }
            data["direction"] = conversion[query.direction]

        return urllib.urlencode(data)


    @staticmethod
    def download_xml(url):
        response = urllib2.urlopen(url)
        return response.read()


    @staticmethod
    def download_flight_xml(query):
        url = "http://flydata.avinor.no/XmlFeed.asp?" + \
            FlightInformationService.generate_query_string(query)
        return FlightInformationService.download_xml(url)
    
    @staticmethod 
    def download_airline_xml():
        url = "http://flydata.avinor.no/airlineNames.asp" 
        return FlightInformationService.download_xml(url)

    @staticmethod 
    def download_airport_xml():
        url = "http://flydata.avinor.no/airportNames.asp" 
        return FlightInformationService.download_xml(url)

    
    
