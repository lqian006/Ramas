from airSpace import *

#---Para mostrar el grafo---#

airspace = LoadAirSpace("Cat_nav.txt", "Cat_seg.txt", "Cat_aer.txt")
PlotAirSpace(airspace)
PlotNode(airspace, "LEVC")
PlotReachable(airspace, "LEBL")
PlotShortestPathSimple(airspace, "MARTA", "GODOX")