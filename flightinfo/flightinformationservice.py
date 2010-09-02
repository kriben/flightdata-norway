import urllib
from query import Query


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
            conversion = { Query.Directions.DEPARTURE : "D",
                           Query.Directions.ARRIVAL : "A" }
            data["direction"] = conversion[query.direction]

        return urllib.urlencode(data)
