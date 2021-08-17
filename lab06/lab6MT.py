# Nome: Douglas Vieira dos Santos
# DRE: 121062791

#1 - Não delete nem modifique esta linha
def lettercount(s):
    phrase = str.split(s)
    letters = len(phrase)
    return letters


#Casos de teste da questão 1 - Não delete nem modifique esta linha
print(lettercount("Vamos terminar este lab hoje mesmo"))


# 2 - Não delete nem modifique esta linha
def phrasecount(s):
    fpoint = str.replace(s,'...','.')
    phtype1 = str.count(fpoint,'.')
    phtype2 = str.count(s,'!')
    phtype3 = str.count(s,'?')
    
    phrases = phtype1 + phtype2 + phtype3
    return phrases

#Casos de teste da questão 2 - Não delete nem modifique esta linha
print(phrasecount("O produto! Sim... o produto de ponto euclidiano. Fornece uma maneira de definir o tamanho ou a norma de um vetor em Rn."))



#3 - Não delete nem modifique esta linha
def modifyph(s):
    fpoint = str.replace(s,'...','.')
    tpoint = str.replace(fpoint,'..','.')
    esppoint = str.replace(tpoint,'.',' ')
    esptravess = str.replace(esppoint,'-',' ')
    espvirg = str.replace(esptravess,',',' ')
    esppointvirg = str.replace(espvirg,';',' ')
    espexcl = str.replace(esppointvirg,'!',' ')
    espint = str.replace(espexcl,'?',' ')
    return espint

#Casos de teste da questão 3 - Não delete nem modifique esta linha
print(modifyph("Toda base de um espaço vetorial - que pode ter o mesmo número de vetore - pode ser referenciada como a dimensão do espaço vetorial dado o seu número de vetores!"))




#4 - Não delete nem modifique esta linha
def revphr(s):
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


#Casos de teste da questão 4 - Não delete nem modifique esta linha
print(revphr("A SSI RU."))


#5 - Não delete nem modifique esta linha
def insere(lista_numero,n):
    addint = lista_numero + [n,]
    list.sort(addint)
    return addint

#Casos de teste da questão 5 - Não delete nem modifique esta linha
print(insere([1,2,15,5,0,8,9], 4))


#6 - Não delete nem modifique esta linha
def greatlist(lista,n):
    list.append(lista,n)
    list.sort(lista)
    ind = list.index(lista,n)
    return lista[ind+1:]


#Casos de teste da questão 6 - Não delete nem modifique esta linha
print(greatlist([1,2,5,9,15,4],8))


#7 - Não delete nem modifique esta linha
def acima_da_media(lista):
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



#Casos de teste da questão 7 - Não delete nem modifique esta linha
print(acima_da_media([1, 6, 9, 4, 0, 8, 5, 7]))