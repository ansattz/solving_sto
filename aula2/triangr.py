import math
c1 = int(input("Valor do cateto: "))
c2 = int(input("Valor do outro cateto: "))

hip = math.sqrt((c1)**2 + (c2)**2)

ptriang = c1 + c2 + hip
print(ptriang)