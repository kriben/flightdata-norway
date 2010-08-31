import urllib
from query import Query

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
            conversion = { Query.Directions.DEPARTURE : "D",
                           Query.Directions.ARRIVAL : "A" }
            data["direction"] = conversion[query.direction]

        return urllib.urlencode(data)
