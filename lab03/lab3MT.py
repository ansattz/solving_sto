# Douglas Vieira
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
def classificacao(cv, ce, cs, fv, fe, fs):
    """ A função retorna ou um vencedor ou um empate dado dois times;
    int, int, int, int, int, int -> str """
    cormengo1=3*cv+ce
    flaminthians1=3*fv+fe
    cormengo2=3*cv+ce+cs
    flaminthians2=3*fv+fe+fs    
    if cormengo1>flaminthians1:
        return "Cormengo"
    elif flaminthians1>cormengo1:
        return "Flaminthians"
    elif flaminthians2>cormengo2:
        return "Flaminthians"
    elif cormengo2>flaminthians2:
        return "Cormengo"
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

