termo1 = int(input("Primeiro termo: "))
termo2 = int(input("Segundo termo: "))
termo3 = int(input("Terceiro termo: "))

media = ((termo1 + termo2 + termo3) / 3)
menortermo = min(termo1, termo2,termo3)

print(menortermo + media)

# def mmedia(x,y,z):
#     menortermo = min(x,y,z)
#     media = (x+y+z)/3
#     return menortermo + media

# menor_somam=mmedia(2,3,5)
# print(menor_somam)
