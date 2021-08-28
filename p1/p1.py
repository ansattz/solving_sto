def nome():
    ...

def dre():
    ...

def base():
    return [ 
    ("CEP", "roubo", "arma", "valor"),
    (22555, "carro",    "S",  70000),
    (22555, "carteira", "S",    300.75),
    (29506, "carro",    "N",  50000),
    (22555, "casa",     "N",  40000),
    ]

def colunas():
    return base()[0]

def registros():
    return base()[1:]

def arma(t):
    return t[2]

def filtra_arma(rs, opcao):
    nullist = []
    if arma(rs[0]) == opcao:
        nullist.append(rs[0])
    if arma(rs[1]) == opcao:
        nullist.append(rs[1])
    if arma(rs[2]) == opcao:
        nullist.append(rs[2])
    if arma(rs[3]) == opcao:
        nullist.append(rs[3])
    return nullist

def filtra_armado(rs):
    nullista = []
    if arma(rs[0]) == "S":
        nullista.append(rs[0])
    if arma(rs[1]) == "S":
        nullista.append(rs[1])
    if arma(rs[2]) == "S":
        nullista.append(rs[2])
    if arma(rs[3]) == "S":
        nullista.append(rs[3])
    return nullista

def filtra_armado_nao(rs):
    nullista = []
    if arma(rs[0]) == "N":
        nullista.append(rs[0])
    if arma(rs[1]) == "N":
        nullista.append(rs[1])
    if arma(rs[2]) == "N":
        nullista.append(rs[2])
    if arma(rs[3]) == "N":
        nullista.append(rs[3])
    return nullista

def percentuais_arma(rs):
    p_armacount = str(len(filtra_armado(rs)) / len(rs))
    p_narmacount = str(len(filtra_armado_nao(rs)) / len(rs))
    p_arma = int(p_armacount.replace('.',''))
    p_narma = int(p_narmacount.replace('.',''))
    if len(filtra_armado(rs))%len(rs) == 0 or len(filtra_armado_nao(rs))%len(rs) ==0 or len(filtra_armado(rs)) / len(rs) == len(filtra_armado_nao(rs)) / len(rs):
        return (10 * p_arma, 10 * p_narma)
    return (p_arma, p_narma)

def valor(t):
    return t[3]

def valores(rs):
    norlist = []
    norlist.append(valor(rs[0]))
    norlist.append(valor(rs[1]))
    norlist.append(valor(rs[2]))
    norlist.append(valor(rs[3]))
    return norlist

def perda(vals):
    return sum(vals)

def dict_obter(d, chave, padrao):
    return d.get(chave,padrao)

def cep(t):
    return t[0]

def contagem_de_roubos_por_cep(rs):
    lista = []
    mydic = {}
    lista.append(cep(rs[0]))
    lista.append(cep(rs[1]))
    lista.append(cep(rs[2]))
    lista.append(cep(rs[3]))
    k1 = lista.count(cep(rs[0]))
    k2 = lista.count(cep(rs[1]))
    k3 = lista.count(cep(rs[2]))
    k4 = lista.count(cep(rs[3]))
    mydic[cep(rs[0])] = k1
    mydic[cep(rs[1])] = k2
    mydic[cep(rs[2])] = k3
    mydic[cep(rs[3])] = k4
    return mydic
 
def meu_arquivo():
    ls = ["p1", str(dre()), str(nome())] # meus dados
    s1 = str.join(" ", ls) # coloque um espaço entre eles
    s2 = str.replace(s1, " ", "_")
    return s2 + ".py"