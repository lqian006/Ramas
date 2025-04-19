from node import *
from segment import *
import matplotlib.pyplot as plt
import math

class Graph:
    def __init__(self):
        self.nodes = []
        self.segments = []

def AddNode(g,n):
    i = 0
    encont = False
    while i < len(g.nodes) and encont == False:
        if n.coordx == g.nodes[i].coordx and n.coordy == g.nodes[i].coordy:
            encont = True
        else:
            i += 1
    if encont == True:
        return False
    else:
        g.nodes.append(n)
        return True

def AddSegment  (g, nameOriginNode, nameDestinationNode):
    g.segments.append(segment("segment",nameOriginNode,nameDestinationNode))
    r = AddNeighbor(nameOriginNode, nameDestinationNode)
    if r == True:
        return True

    found1 = False
    found2 = False
    n = (0)
    while n < len(g.nodes) and (found1 == False or found2 == False):
        if nameOriginNode.name == g.nodes[n].name:
            found1 = True
        elif nameDestinationNode.name == g.nodes[n].name:
            found2 = True
        n += 1
    if found1 == False:
        return False
    if found2 == False:
        return False

def GetClosest (g,x,y):
    min = 9999999999999.9
    men = 0
    for node in g.nodes:
        dist = math.sqrt((node.coordx - x) ** 2 + (node.coordy - y) ** 2)
        if dist < min:
            min = dist
            men = node.name
    return men


#plt.plot([nameOriginNode.coordx,nameDestinationNode.coordx],[nameOriginNode.coordy,nameDestinationNode.coordy])