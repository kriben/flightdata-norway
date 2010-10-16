from pytz import timezone

class Flight(object):
    def __init__(self, unique_id, flight_id, airline, airport, schedule_time):
        self.unique_id = unique_id
        self.flight_id = flight_id
        self.airline = airline
        self.airport = airport
        self.schedule_time = schedule_time
        
    def get_local_schedule_time(self):
        oslo_tz = timezone('Europe/Oslo')
        local_schedule_time = self.schedule_time.astimezone(oslo_tz)
        return local_schedule_time


    def __str__(self):
        return "%s - %s: %s Time: %s" % (self.flight_id, 
                                 self.airline.name.encode('utf-8'),
                                 self.airport.name.encode('utf-8'),
                                 self.get_local_schedule_time())

    
