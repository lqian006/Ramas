import math
class Node:
    def __init__(self):
        self.name = ""
        self.coordx = 0.0
        self.coordy = 0.0
        self.neighbors = []

def AddNeighbor(n1,n2):
    i = 0
    encontrado = False
    while i < len(n1.neighbors) and encontrado == False:
        if n2.name == n1.neighbors[i].name:
            encontrado = True
        else:
            i += 1
    if encontrado == True:
        return False
    else:
        n1.neighbors.append(n2)
        return True

def Distance(n1,n2):
    distx = float(n2.coordx) - float(n1.coordx)
    disty = float(n2.coordy) - float(n1.coordy)
    dist = math.sqrt(distx**2+disty**2)
    return dist