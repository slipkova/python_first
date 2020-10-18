from physics import *

for x, i in enumerate(GRAVITIES):
    print(f"{x} - {i[0]}")


p1 = int(input("Na jaké planetě byste chtěli padat?"))
p2 = int(input("S pádem na jaké planetě byste chtěli svůj porovnávat?"))
v = float(input("Z jaké výšky chcete padat?"))
height(GRAVITIES[p1], GRAVITIES[p2], v)