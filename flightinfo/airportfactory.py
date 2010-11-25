from flightinfo.position import Position

class AirPortFactory(object):
    def __init__(self, airports):
        self.mapping = {}
        for a in airports:
            self.mapping[a.code] = a

        self.norwegian_airports = self._init_norwegian_airports()

    def get_airport_by_code(self, code):
        return self.mapping[code]

    def get_norwegian_airports(self):
        return self.norwegian_airports

    def _init_norwegian_airports(self):

        norwegian_codes = [
            ("ALF", Position(69.976111, 23.371667)),
            ("ANX", Position(69.292500, 16.144167)),
            ("BDU", Position(69.055758, 18.540356)),
            ("BGO", Position(60.293386, 5.218142)),
            ("BJF", Position(70.600278, 29.692500)),
            ("BNN", Position(65.461111, 12.217500)),
            ("BOO", Position(67.269167, 14.365278)),
            ("BVG", Position(70.871389, 29.034167)),
            ("EVE", Position(68.491300, 16.678108)),
            ("FDE", Position(61.391111, 5.756944)),
            ("FRO", Position(61.583611, 5.024722)),
            ("HAA", Position(70.486675, 22.139744)),
            ("HAU", Position(59.345267, 5.208364)),
            ("HFT", Position(70.679722, 23.668889)),
            ("HOV", Position(62.183, 6.067)),
            ("HVG", Position(71.009722, 25.983611)),
            ("KKN", Position(69.725781, 29.891295)),
            ("KRS", Position(58.204214, 8.085369)),
            ("KSU", Position(63.111781, 7.824522)),
            ("LKL", Position(70.068814, 24.973489)),
            ("LKN", Position(68.152500, 13.609444)),
            ("LYR", Position(78.246111, 15.465556)),
            ("MEH", Position(71.029167, 27.826111)),
            ("MJF", Position(65.783997, 13.214914)),
            ("MOL", Position(62.744722, 7.262500)),
            ("MQN", Position(66.363889, 14.301389)),
            ("NVK", Position(68.436111, 17.385833)),
            ("OSL", Position(60.193917, 11.100361)),
            ("OSY", Position(64.467, 11.583)),
            ("RET", Position(67.527778, 12.103333)),
            ("RRS", Position(62.578411, 11.342347)),
            ("RVK", Position(64.838333, 11.146111)),
            ("SDN", Position(61.830000, 6.109444)),
            ("SKN", Position(68.580833, 15.026111)),
            ("SOG", Position(61.156111, 7.136614)),
            ("SOJ", Position(69.786839, 20.959444)),
            ("SSJ", Position(65.956828, 12.468944)),
            ("SVG", Position(58.876778, 5.637856)),
            ("SVJ", Position(68.243333, 14.669167)),
            ("TOS", Position(69.683333, 18.918919)),
            ("TRD", Position(63.457556, 10.924250)),
            ("TRF", Position(59.186703, 10.258628)),
            ("VAW", Position(70.355392, 31.044889)),
            ("VDB", Position(61.015556, 9.288056)),
            ("VDS", Position(70.065278, 29.844722)),
            ("VRY", Position(67.689444, 12.681944)) ]

        airports = []
        for (code, position) in norwegian_codes:
            try:
                airport = self.get_airport_by_code(code)
                airport.position = position
                airports.append(airport)
            except KeyError:
                pass
        return airports


    def get_closest_norwegian_airport(self, pos):
        airports = self.get_norwegian_airports()
        if not airports:
            return None

        return min(airports, key=lambda a: pos.compute_distance_to(a.position))
