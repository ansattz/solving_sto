# Douglas Santos
# @ansattz


# Exercício 1.
def PosNegZero(x):
    """ Teste de tricotomia com apenas uma variável;
	A função retorna uma resposta dizendo se um número inteiro é positivo, negativo ou zero;
    int -> str """
    if x>0:
        return str(x) + " e positivo"
    elif x<0:
        return str(x) + " e negativo"
    else:
        return str(x) + " e zero"

print(PosNegZero(-1))


# Exercício 2.
def classificacao(vv, ve, vs, vv, ve, vs):
    """ A função retorna ou um venvedor ou um empate dado dois times;
    int, int, int, int, int, int -> str """
    flamengo1=3*vv+ve
    vasco1=3*vv+ve
    flamengo2=3*vv+ve+vs
    vasco2=3*vv+ve+vs    
    if flamengo1>vasco1:
        return "Flamengo"
    elif vasco1>flamengo1:
        return "Vasco"
    elif vasco2>flamengo2:
        return "Vasco"
    elif flamengo2>vasco2:
        return "Flamengo"
    else:
        return "Empate"

print(classificacao(9,5,-1,10,2,10))


# Exercício 3.
def avioes(c, p_compr, p_compet):
    """ A função retorna uma string dizendo se é suficiente a quantidade de papeis para ocorrer a competição;
    int, int -> str """
    papelpc=c*p_compet
    if papelpc>p_compr:
        return "Insuficiente"
    elif papelpc<p_compr:
        return "Suficiente"
    else:
        return "Suficiente"

print(avioes(5,40,2))

