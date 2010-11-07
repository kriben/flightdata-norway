
class AirPortFactory(object):
    def __init__(self, airports):
        self.mapping = {}
        for a in airports:
            self.mapping[a.code] = a

    def get_airport_by_code(self, code):
        return self.mapping[code]

    def get_norwegian_airports(self):
        norwegian_codes = [ "ALF",
                            "ANX",
                            "BDU",
                            "BGO",
                            "BJF",
                            "BNN",
                            "BOO",
                            "BVG",
                            "EVE",
                            "FDE",
                            "FRO",
                            "HAA",
                            "HAU",
                            "HFT",
                            "HOV",
                            "HVG",
                            "KKN",
                            "KRS",
                            "KSU",
                            "LKL",
                            "LKN",
                            "LYR",
                            "MEH",
                            "MJF",
                            "MOL",
                            "MQN",
                            "NVK",
                            "OSL",
                            "OSY",
                            "RET",
                            "RRS",
                            "RVK",
                            "SDN",
                            "SKN",
                            "SOG",
                            "SOJ",
                            "SSJ",
                            "SVG",
                            "SVJ",
                            "TOS",
                            "TRD",
                            "VAW",
                            "VDB",
                            "VDS",
                            "VRY" ]
        airports = []
        for i in norwegian_codes:
            try:
                airports.append(self.get_airport_by_code(i))
            except KeyError:
                pass
        return airports
