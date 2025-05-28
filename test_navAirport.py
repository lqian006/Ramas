from navAirport import *
from navPoint import *

n1 = NavPoint(000, "Underground", 37.258544, -115.805308)
n2 = NavPoint(51, "Por donde viniste", -1, -1)
A = Airport("Area51", n2, n1)

print(A.SID.name)