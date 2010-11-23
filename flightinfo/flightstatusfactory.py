import copy


class FlightStatusFactory(object):
    def __init__(self, statuses):
        self.mapping = {}
        for s in statuses:
            self.mapping[s.code] = s


    def get_flight_status_by_code(self, code):
        return copy.deepcopy(self.mapping[code])
