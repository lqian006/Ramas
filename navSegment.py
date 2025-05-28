class NavSegment:
    def __init__(self, origin, destination, dist):
        self.origin = origin
        self.destination = destination
        self.dist = float(dist)

#NavSegment.dist isn't an "inputable" argument because it's given to us in the segments lists.