# Douglas Santos
# @ansattz


#1
def lettercount(s):
    """Conta as letras de uma frase;
    str -> int"""
    phrase = str.split(s)
    letters = len(phrase)
    return letters


#Casos de teste da questão 1
print(lettercount("Vamos terminar este lab hoje mesmo"))


# 2
def phrasecount(s):
    """Conta o número de frases que aparecem no texto;
    str -> int"""
    fpoint = str.replace(s,'...','.')
    phtype1 = str.count(fpoint,'.')
    phtype2 = str.count(s,'!')
    phtype3 = str.count(s,'?')
    
    phrases = phtype1 + phtype2 + phtype3
    return phrases

#Casos de teste da questão 2
print(phrasecount("O produto! Sim... o produto de ponto euclidiano. Fornece uma maneira de definir o tamanho ou a norma de um vetor em Rn."))



#3
def modifyph(s):
    """Caracteres de pontuação serão substituídos por espaços;
    str -> str"""
    fpoint = str.replace(s,'...','.')
    tpoint = str.replace(fpoint,'..','.')
    esppoint = str.replace(tpoint,'.',' ')
    esptravess = str.replace(esppoint,'-',' ')
    espvirg = str.replace(esptravess,',',' ')
    esppointvirg = str.replace(espvirg,';',' ')
    espexcl = str.replace(esppointvirg,'!',' ')
    espint = str.replace(espexcl,'?',' ')
    return espint

#Casos de teste da questão 3
print(modifyph("Toda base de um espaço vetorial - que pode ter o mesmo número de vetore - pode ser referenciada como a dimensão do espaço vetorial dado o seu número de vetores!"))




#4
def revphr(s):
    """Frase será retornada na ordem inversa, sem letras maiúsculas e sempre pontuação;
    str -> str"""
    modfpoint = str.replace(s,'...','.')
    fpoint = str.replace(modfpoint,'.','')
    reexcl = str.replace(fpoint,'!','')
    reint = str.replace(reexcl,'?','')
    reevirg = str.replace(reint,',','')
    repointvirg = str.replace(reevirg,';','')
    redoisp = str.replace(repointvirg,':','')
    retr = str.replace(redoisp,'-',' ')
    reasp = str.replace(retr,'"','')
    repar1 = str.replace(reasp,'(','')
    repar2 = str.replace(repar1,')','')
    withoutupp = str.lower(repar2)
    splitng = withoutupp.split()
    revletters = list(reversed(splitng))
    return " ".join(revletters)


#Casos de teste da questão 4
print(revphr("A SSI RU."))


#5
def insere(lista_numero,n):
    """A lista será ordenada (crescente) e o inteiro n será colocado na posição correta, continuando ordenada;
    list, int -> list"""
    addint = lista_numero + [n,]
    list.sort(addint)
    return addint

#Casos de teste da questão 5
print(insere([1,2,15,5,0,8,9], 4))


#6
def greatlist(lista,n):
    """Dada uma lista de inteiros e um inteiro n,
    teremos outra lista com todos os inteiros da
    lista original maiores que n ordenados (crescente);
    list, int -> list"""
    list.append(lista,n)
    list.sort(lista)
    ind = list.index(lista,n)
    return lista[ind+1:]


#Casos de teste da questão 6
print(greatlist([1,2,5,9,15,4],8))


#7
def acima_da_media(lista):
    """Retornará uma lista com inteiros acima da média da lista original;
    list -> list"""
    nullist = []
    orlist = lista[:]
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    ind = list.index(lista,media)
    if media in orlist:
        return lista[ind+2:]
    elif len(lista) > 2:
        return lista[ind+1:]
    else:
        return nullist



#Casos de teste da questão 7
print(acima_da_media([1, 6, 9, 4, 0, 8, 5, 7]))