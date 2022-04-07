# Douglas Santos
# @ansattz


def intercala(lista1,lista2):
    """ A função concatena uma intercalação de termos de uma lista de 3 termos com outra lista de 3 termos;
    list, list -> list """ 
    nullist = []
    lista3 = nullist + [lista1[0],] + [lista2[0],] + [lista1[1],] + [lista2[1],] + [lista1[2],] + [lista2[2],]
    return lista3

print(intercala([1,3,5],[2,4,6]))


def pontos_por_time(lista1):
    """ A função retorna os pontos de cada time;
    list -> list """
    dic={}
    jogo1 = lista1[0]
    jogo2 = lista1[1]
    t1 = jogo1[0]
    t2 = jogo1[1]
    goals = jogo1[2]

    t1g = goals[0]
    t2g = goals[1]
    if t1g == t2g:
        dic[t1] = 1
        dic[t2] = 1
    if t1g > t2g:
        dic[t1] = 3
        dic[t2] = 0
    if t1g < t2g:
        dic[t1] = 0
        dic[t2] = 3
    
    goals = jogo2[2]
    t2g = goals[0]
    t1g = goals[1]
    if t1g == t2g:
        dic[t1] = dic[t1] + 1
        dic[t2] = dic[t2] + 1
    if t1g > t2g:
        dic[t1] = dic[t1] + 3
        dic[t2] = dic[t2] + 0
    if t1g < t2g:
        dic[t1] = dic[t1] + 0
        dic[t2] = dic[t2] + 3
    return dic


def colchao(lista,h,l):
    """ A função retorna a uma resposta em valor booleano sobre a possibilidade de um colchão
    paralelepípedo passar por uma porta;
    list, int, int -> bool """
    if lista[1] > h and l > lista[1]:
        return True
    if lista[1] > h:
        return False
    elif lista[0] > h and lista[0] > l:
        return False
    else:
        return True
print(colchao([36,190,209],187,248))