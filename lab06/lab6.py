# Douglas Vieira
# @ansattz

#1a - Não delete nem modifique esta linha
def contatinhosApp(lista,tel):
    """ A função cria uma nova lista que retorna a remoção ou não remoção de um telefone na lista de telefones;
    list, str -> list """
    j = lista[1]
    if tel in j:
        list.remove(j,tel)
        return True
    else:
        return False
    
#Casos de teste da questão 1a - Não delete nem modifique esta linha
print(contatinhosApp(['Bruno Campos', ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'],'2199112233'))
print(contatinhosApp(['Bruno Campos', ['2199112233', '2133992211'], 'brunoc91@emailquente.com.br', '@brunocampos91'],'21991'))


#2 - Não delete nem modifique esta linha
def futagainwtf(times,pontos):
    """ A função retorna uma lista com os times participantes, uma lista com os elementos sendo o time campeão e o seu ponto no campeonato, e a média de pontos por times;
    list, list -> list """
    mylist = []
    tabela = dict(zip(times, pontos))
    maxpoint = max(dict.values(tabela))
    timecampeao = times[list.index(pontos,maxpoint)]
    mediadepontos = sum(pontos)/len(pontos)
    return mylist + [times,] + [timecampeao,maxpoint] + [mediadepontos,]
        
#Casos de teste da questão 1b - Não delete nem modifique esta linha
print(futagainwtf(['FLAMENGO','VASCO','FLUMINENSE','BOTAFOGO','ABC'],[2,5,9,8,15]))
