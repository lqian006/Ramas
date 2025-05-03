from segment import *
from node import *

n1 = Node("aaa",0,0)
n2 = Node("bbb",3,4)
n3 = Node("ccc",5,6)
s1 = segment("Seg1",n1,n2)
s2 = segment("Seg2",n2,n3)
print(s1.cost)
print(s2.cost)
print(s1.origin_node.name)
print(s1.destination_node.name)
print(s2.origin_node.name)
print(s2.destination_node.name)
#Dijstra, A*, Youtube: Numpy
