class NavPoint:
    def __init__(self, ident, name, lat, lon):
        self.ident = int(ident)
        self.name = str(name)
        self.lat = float(lat)
        self.lon = float(lon)
        self.neighbors = []