    
class Flight(object):
    def __init__(self, unique_id, flight_id, airline, airport):
        self.unique_id = unique_id
        self.flight_id = flight_id
        self.airline = airline
        self.airport = airport

    def __str__(self):
        return "%s - %s: -%s" % (self.flight_id, 
                                 self.airline.name.encode('utf-8'),
                                 self.airport.name.encode('utf-8'))

    
