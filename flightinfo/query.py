
class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

class Query(object):
    Directions = Enum(["DEPARTURE", "ARRIVAL"])

    def __init__(self, airport):
        self.airport = airport
        self.time_from = None
        self.time_to = None
        self.last_update = None
        self.direction = None

