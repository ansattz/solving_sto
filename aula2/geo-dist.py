import math
pax = float(input("Valor do ponto A em x: "))
pay = float(input("Valor do ponto A em y: "))

pbx = float(input("Valor do ponto B em x: "))
pby = float(input("valor do ponto B em y: "))

p1 = pbx - pax
p2 = pby - pay

dist = math.sqrt((p1)**2 + (p2)**2)
print(dist)