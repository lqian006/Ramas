from path import *
from graph import *

r = CreateGraph_1()
P = Path()
AddNodeToPath(r, P, "A")
print(P.__dict__, P.cost)
AddNodeToPath(r, P, "B")
print(P.__dict__, P.cost)
AddNodeToPath(r, P, "C")
print(P.cost)
print(ContainsNode(P, "B"))
print(ContainsNode(P, "F"))
PlotPath(r, P)