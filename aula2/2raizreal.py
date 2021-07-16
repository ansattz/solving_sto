import math
a = float(input("Coeficiente principal a: "))
b = float(input("Coeficiente segundário b: "))
c = float(input("Coeficiente independente c: "))

disc = b**2-4*a*c
rreal = ((-b - math.sqrt(disc))/2*a)

print(rreal)

# def rreal(a,b,c):
#     disc = b**2-4*a*c
#     rreal = ((-b - math.sqrt(disc))/2*a)
#     return rreal