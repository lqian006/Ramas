from airSpace import *


a = AirSpace()
A = LoadAirSpace(a, "Cat")
'''for point in a.navPoints:
    print(point.name)
for segment in a.navSegments:
    print(segment.__dict__)
for air in a.navAirports:
    print(air.SID, air.STAR)

PlotAirSpace(a)
PlotNavPoint(a, "GODOX")'''
p = FindShortestPath(a, "LEGE", "LEZG")
PlotPath(a, p)
print(p.cost)