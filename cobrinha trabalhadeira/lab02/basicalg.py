# Douglas Vieira
# @ansattz


"""Exercícios de Algebra básica."""
import math

# Primeira raiz de uma equação polinomial quadrática.
a = float(input("Coeficiente principal a: "))
b = float(input("Coeficiente segundário b: "))
c = float(input("Coeficiente independente c: "))

disc = b**2-4*a*c
real = ((-b + math.sqrt(disc))/2*a)
print(real)
import math
def rreal(a,b,c):
    disc = b**2-4*a*c
    return ((-b - math.sqrt(disc))/2*a)
    
    

# Segunda raiz de uma equação polonimial quadrática.
a = float(input("Coeficiente principal a: "))
b = float(input("Coeficiente segundário b: "))
c = float(input("Coeficiente independente c: "))

disc = b**2-4*a*c
rreal = ((-b - math.sqrt(disc))/2*a)
print(rreal)


# Sequência aritmética 
a1 = float(input("Termo inicial: "))
af = float(input("Termo final: "))
r = float(input("Razão: "))

numtermos = (af - a1 + r)/r
print(numtermos)

# def rreal(a1,af,r):
#     numtermos = (af - a1 + r)/r
#     return numtermos


# Soma de uma P.A
def pa(a,b,r):
    n = int((b - a + r)/r)
    if (n<=0):
        print("Sem possibilidade")
    else:
        spa = n*((a+b)/2)
    return spa

a = float(input("Termo inicial: "))
b = float(input("Termo final: "))
r = float(input("Razão: "))
print(pa(a,b,r))

"""Média"""
termo1 = int(input("Primeiro termo: "))
termo2 = int(input("Segundo termo: "))
termo3 = int(input("Terceiro termo: "))
media = ((termo1+termo2+termo3)/3)

print("Média desses três números inteiros é:", media)

def media3(x,y,z):
    return (x+y+z)/3
media=media3(2,5,3)
print(media)


# Menor número entre três inteiros com a soma da média
termo1 = int(input("Primeiro termo: "))
termo2 = int(input("Segundo termo: "))
termo3 = int(input("Terceiro termo: "))

media = ((termo1 + termo2 + termo3) / 3)
menortermo = min(termo1, termo2,termo3)

print(menortermo + media)

def mmedia(x,y,z):
    menortermo = min(x,y,z)
    media = (x+y+z)/3
    return menortermo + media

menor_somam=mmedia(2,3,5)
print(menor_somam)

# Maior termo menos a média entre os três.
termo1 = int(input("Primeiro termo: "))
termo2 = int(input("Segundo termo: "))
termo3 = int(input("Terceiro termo: "))

media = ((termo1 + termo2 + termo3) / 3)
maiortermo = max(termo1, termo2,termo3)

print(maiortermo - media)
