from pytz import timezone
import datetime

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

class Flight(object):
    Directions = Enum(["DEPARTURE", "ARRIVAL"])

    def __init__(self, unique_id, flight_id, airline, airport, schedule_time,
                 direction):
        self.unique_id = unique_id
        self.flight_id = flight_id
        self.airline = airline
        self.airport = airport
        self.schedule_time = schedule_time
        self.direction = direction
        
    def get_local_schedule_time(self):
        oslo_tz = timezone('Europe/Oslo')
        local_schedule_time = self.schedule_time.astimezone(oslo_tz)
        return local_schedule_time


    def __str__(self):
        return "%s - %s: %s (%s)" % (self.flight_id, 
                                   self.airport.name.encode('utf-8'),
                                   self.get_local_schedule_time().strftime("%H:%M"),
                                   self.airline.name.encode('utf-8'))

    
