""" machineteachin.tech II """
# Exercício 1.
# Número de bombons com input sendo o quanto de dinheiro possui para comprar(x) e o preço do bombom(y).
# def num_bombons(x,y):
#    try:
#       qbombons=int(x/y)
#       print(qbombons)
#    except:
#       print("Você pode pegar os bombons de graça :).")

# num_bombons(50,0)


# Exercício 2.
# def carros(x,y=5):
#     """ A função retorna a quantidade de carros necessários dada a quantidade de pessoas
#     obedecendo a condição de que os carros que não possuem capacidade 5 sejam considerados;
#     int, int -> int """
#     ppl_pla=int(x/y)
#     if x%y>0:
#         return ppl_pla + 1
#     else:
#         return ppl_pla
# print(carros(12))


# Exercício 3.
# Quantos bolos o rapaz consegue fazer com os ingredientes.
# def bolos(x,y,z):
#     i1=int(x/2)
#     i2=int(y/3)
#     i3=int(z/5)
#     qtbolo=min(i1,i2,i3)
#     return qtbolo

# print(bolos(20,15,500))