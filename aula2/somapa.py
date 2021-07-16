# Importar o numpy e utilizar a função numpy.arange() junto ao numpy.prod([]) ao meu entendimento presente
# se apresenta como o mais analítco, que é o objetivo desta construção.

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