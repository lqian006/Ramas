import matplotlib.pyplot as plt
import heapq
from itertools import count

from navPoint import *
from navSegment import *
from navAirport import *
from node import *
from path import *
from graph import *

class AirSpace:
    def __init__(self):
        self.navPoints = []
        self.navSegments = []
        self.navAirports = []

def LoadAirSpace(airspace, region):
    F = open(region+"_nav.txt", "r")
    linea = F.readline()
    while linea != "":
        partes = linea.split()
        airspace.navPoints.append(NavPoint(int(partes[0]), str(partes[1]), float(partes[2]), float(partes[3])))
        linea = F.readline()
    F.close()

    F2 = open(region+"_seg.txt", "r")
    lineas = F2.readline()
    pointorigin = None
    pointdestination = None
    while lineas != "":
        elementos = lineas.split()
        for point in airspace.navPoints:
            if point.ident == int(elementos[0]):
                pointorigin = point
            if point.ident == int(elementos[1]):
                pointdestination = point
        airspace.navSegments.append(NavSegment(pointorigin, pointdestination, float(elementos[2])))
        AddNeighbor(pointorigin, pointdestination)
        lineas = F2.readline()
    F2.close()


    F3 = open(region+"_aer.txt", "r")
    fila = 0
    leerfila = F3.readline()
    i = 0
    nom = None
    dep = None
    arr = None
    while leerfila != "":
        if i == 3:
            airspace.navAirports.append(Airport(nom, dep, arr))
            i = 0
        fila = leerfila.strip()
        if (i+1)%2 != 0 and (i+1)%3 != 0:
            nom = leerfila.strip()
        else:
            for points in airspace.navPoints:
                if points.name == fila and (i+1)%2 == 0:
                    dep = points
                    break
                elif points.name == fila and (i+1)%3 == 0:
                    arr = points
                    break
        i+=1
        leerfila = F3.readline()
    airspace.navAirports.append(Airport(nom, dep, arr))
    F3.close()

def PlotAirSpace(a):
    for punto in a.navPoints:
        plt.plot(punto.lon, punto.lat, marker="o", color="black", markersize=3)
        plt.text(punto.lon + 0.05, punto.lat + 0.05, punto.name, fontsize=4, color="green")
    for linea in a.navSegments:
        plt.annotate("", (linea.destination.lon, linea.destination.lat),
                     (linea.origin.lon, linea.origin.lat),
                     arrowprops=dict(arrowstyle="->", color="cyan", lw=1.5, alpha=0.5))
        plt.text((linea.origin.lon + linea.destination.lon) / 2,
                 (linea.origin.lat + linea.destination.lat) / 2, round(linea.dist,2), fontsize=5)
    plt.margins(x=0.25, y=0.25)
    plt.grid(True)
    #plt.show()

def PlotNavPoint (a, nameOrigin):
    node1 = None
    found = False
    neighbors = []
    for node in a.navPoints:
        if node.name == nameOrigin:
            node1 = node
            found = True
    if found == False:
        return False
    plt.plot(node1.lon, node1.lat, color="blue", marker="o", markersize=3)
    plt.text(node1.lon+0.1, node1.lat+0.1, node1.name, fontsize=4)
    for point in node1.neighbors:
        plt.plot(point.lon, point.lat, color="green", marker="o", markersize=3)
        plt.text(point.lon+0.1, point.lat+0.1, point.name, fontsize=4)
        neighbors.append(point)
    for element in a.navPoints:
        if element != node1 and element not in neighbors:
            plt.plot(element.lon, element.lat, color="gray", marker="o", markersize=3)
            plt.text(element.lon+0.15, element.lat+0.15, element.name, fontsize=4)
    for segment in neighbors:
        plt.annotate("", (segment.lon, segment.lat),
                     (node1.lon, node1.lat),
                     arrowprops=dict(arrowstyle="->", color="red", lw=1.5))
        plt.text((node1.lon + segment.lon) / 2,
                 (node1.lat + segment.lat) / 2, Distance(node1,segment), fontsize=4)
    plt.grid(True)
    plt.margins(x=0.25,y=0.25)
    #plt.show()

def FindShortestPath(g, start_name, end_name):
    start_node = None
    end_node = None
    for node in g.navAirports:
        if node.name == start_name:
            start_node = node.SID
        if node.name == end_name:
            end_node = node.STAR

    if not start_node or not end_node:
        return None

    # Priority queue for open nodes: (f_score, node)
    counter = count()
    open_set = [(0, next(counter), start_node)]
    heapq.heapify(open_set)

    # Came from dictionary to reconstruct path
    came_from = {}

    # g_score[node] is the cost of the cheapest path from start to node currently known
    g_score = {node: float('inf') for node in g.navPoints}
    g_score[start_node] = 0

    # f_score[node] = g_score[node] + heuristic(node, end_node)
    f_score = {node: float('inf') for node in g.navPoints}
    f_score[start_node] = Distance(start_node, end_node)

    while open_set:
        current = heapq.heappop(open_set)[2]

        if current == end_node:
            # Reconstruct path
            path = Path()
            while current in came_from:
                AddNodeToPath(g, path, current)
                current = came_from[current]
            AddNodeToPath(g, path, start_node)
            path.nodes.reverse()
            return path

        for neighbor in current.neighbors:
            # Calculate tentative g_score
            tentative_g_score = g_score[current] + Distance(current, neighbor)

            if tentative_g_score < g_score[neighbor]:
                # This path is better than any previous one
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + Distance(neighbor, end_node)
                heapq.heappush(open_set, (f_score[neighbor], next(counter), neighbor))

    return None

def PlotPath (g, p):
    i = 1
    graph.Plot(g)
    while i < len(p.nodes):
        graph.plt.annotate("", (p.nodes[i].lon, p.nodes[i].lat),
                    (p.nodes[i-1].lon, p.nodes[i-1].lat),
                    arrowprops=dict(arrowstyle="->", color="red", lw=1.5))
        i+=1
    #plt.show()