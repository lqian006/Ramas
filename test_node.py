from node import *
p1 = Node()
p1.name = "Casa"
p1.coordx = 0.0
p1.coordy = 0.0
n2 = Node()
n2.name = "Insti"
n2.coordx = 3.0
n2.coordy = 4.0
print(p1.coordx)
print(Distance(p1,n2))
print(AddNeighbor(p1,n2))
print(p1.neighbors)
print(AddNeighbor(p1,n2))
print(p1.__dict__)
for n in p1.neighbors:
    print(p1.__dict__)
