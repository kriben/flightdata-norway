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
                 direction, **kwargs):
        self.unique_id = unique_id
        self.flight_id = flight_id
        self.airline = airline
        self.airport = airport
        self.schedule_time = schedule_time
        self.direction = direction
        
        for (name, attribute) in kwargs.iteritems():
            self.__setattr__(name, attribute) 

        
    def get_local_schedule_time(self):
        oslo_tz = timezone('Europe/Oslo')
        local_schedule_time = self.schedule_time.astimezone(oslo_tz)
        return local_schedule_time

    def __getattr__(self, name):
        return None


    def __str__(self):

            
        
        new_info = []
        if self.direction == Flight.Directions.DEPARTURE:
            if self.gate:
                new_info.append("Gate: %s" % (self.gate))
            if self.check_in:
                new_info.append("Check in: %s" % (self.check_in))
        else:
            if self.belt:
                new_info.append("Belt: %s" % self.belt)

        if self.status:
            new_info.append("Info: %s %s" % (self.status[0].text, self.status[1]))


        return "%s - %s: %s (%s) %s" % (self.flight_id, 
                                        self.airport.name.encode('utf-8'),
                                        self.get_local_schedule_time().strftime("%H:%M"),
                                        self.airline.name.encode('utf-8'),
                                        " ".join(new_info))

    
