
class AirlineFactory(object):
    def __init__(self, airlines):
        self.mapping = {}
        for a in airlines:
            self.mapping[a.code] = a


    def getAirlineByCode(self, code):
        return self.mapping[code]
