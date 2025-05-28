import math
class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.lon = x
        self.lat = y
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
    distx = float(n2.lon) - float(n1.lon)
    disty = float(n2.lat) - float(n1.lat)
    dist = math.sqrt(distx**2+disty**2)
    redond = round(dist,2)
    return redond