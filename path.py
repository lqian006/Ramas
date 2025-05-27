from node import *
import graph

class Path:
    def __init__(self):
        self.nodes = []
        self.cost = 0.0

def AddNodeToPath(g, path, innode):
    i = 0
    node = None
    found = False
    while i < len(g.nodes) and not found:
        if innode == g.nodes[i].name:
            found = True
            node = g.nodes[i]
        i += 1
    if len(path.nodes) < 1:
        if found:
            path.nodes.append(node)
            return True
        else:
            print("No existe ese nodo en este grafo.")
            return False
    else:
        if found:
            path.nodes.append(node)
            path.cost += Distance(path.nodes[-2], path.nodes[-1])
            return True
        else:
            return False

def ContainsNode (p, n):
    found = False
    for node in p.nodes:
        if n == node.name:
            found = True
    if found:
        return True
    else:
        return False

def PlotPath (g, p):
    i = 1
    graph.Plot(g)
    while i < len(p.nodes):
        graph.plt.annotate("", (p.nodes[i].coordx, p.nodes[i].coordy),
                    (p.nodes[i-1].coordx, p.nodes[i-1].coordy),
                    arrowprops=dict(arrowstyle="->", color="red", lw=1.5))
        i+=1
    graph.plt.show()