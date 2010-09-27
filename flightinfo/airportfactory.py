
class AirPortFactory(object):
    def __init__(self, airports):
        self.mapping = {}
        for a in airports:
            self.mapping[a.code] = a

    def get_airport_by_code(self, code):
        return self.mapping[code]
