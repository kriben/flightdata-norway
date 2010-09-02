    
class Flight(object):
    def __init__(self, unique_id, flight_id, airline):
        self.unique_id = unique_id
        self.flight_id = flight_id
        self.airline = airline

    def __str__(self):
        return "%s - %s" % (self.flight_id, self.airline.name.encode('utf-8'))

    
