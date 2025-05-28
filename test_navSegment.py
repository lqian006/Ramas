from navPoint import *
from navSegment import *

n1 = NavPoint(626, "Stitch", 21.54005)
n2 = NavPoint(2319, "MonstersInc", 23.842369, 19.00521)
s1 = NavSegment(n1, n2, 27)

print(s1.__dict__)