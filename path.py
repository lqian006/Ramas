from node import *
class Path:
    def __init__(self):
        self.nodes = []
        self.cost = 0.0

def AddNodeToPath(Path, Node):
    i = 0
    node = None
    while i < len(Path.nodes):
        if Path.nodes[i].name == Node:
            return False
        else:
            node = Node
            Path.nodes.append(node)