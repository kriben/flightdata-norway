try:
    from pytz.gae import pytz
except:
    import pytz

class FlightStatus(object):
    def __init__(self, code, text):
        self.code = code
        self.text = text
        self.time = None

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def get_local_time(self):
        oslo_tz = pytz.timezone('Europe/Oslo')
        local_time = self.time.astimezone(oslo_tz)
        return local_time
