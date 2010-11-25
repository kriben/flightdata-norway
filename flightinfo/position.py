from math import sin, cos, radians, atan2, sqrt, asin

class Position(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def compute_distance_to(self, p):

        # geometric mean from wikipeda
        earth_radius = 6371.0

        # convert degrees to radians
        p1 = (radians(self.latitude),
              radians(self.longitude))
        p2 = (radians(p.latitude),
              radians(p.longitude))

        diff = (p1[0] - p2[0], p1[1] - p2[1])
        d = 2 * asin(sqrt((sin(diff[0] / 2.0))**2 + 
                          cos(p1[0]) * cos(p2[0]) * 
                          (sin(diff[1] / 2.0))**2))
   
        return earth_radius * d
        
    
