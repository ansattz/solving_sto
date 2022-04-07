# Douglas Santos
# @ansattz


#1  - Não delete nem modifique esta linha
def SIGA(a,b,c,d):
    media=(b+c+d)/3
    media1dec='{0:0.1f}'.format(media)
    if media >= 7:
        return (a, media1dec, 'Aprovado', 'Parabéns!')
    elif media < 7 and media >= 5:
        return (a, media1dec, 'Aprovado')
    elif media < 5:
        return (a, media1dec, 'Reprovado')

#Casos de teste da questão 1 - Não delete nem modifique esta linha
print(SIGA('Douglas',6.5,8.7,8))
print(SIGA('Douglas',1,2.7,3))
print(SIGA('Douglas',2,5,3))
print(SIGA('Douglas',6,8.7,2))
print(SIGA('Douglas',6.5,8.1,8.1))
print(SIGA('Douglas',10,10,10))

SIGA('Douglas',6.5,8.7,8)
SIGA('Douglas',1,2.7,3)
SIGA('Douglas',2,5,3)
SIGA('Douglas',6,8.7,2)
SIGA('Douglas',6.5,8.1,8.1)
SIGA('Douglas',10,10,10)


#2  - Não delete nem modifique esta linha
def ano(ano):
    t=('Macaco','Galo','Cão','Porco','Rato','Boi','Tigre','Coelho','Dragão','Serpente','Cavalo','Carneiro')
    sig=t[(ano%12)]
    return sig

#Casos de teste da questão 2 - Não delete nem modifique esta linha
print(ano(1903))
print(ano(1932))
print(ano(1957))
print(ano(1963))
print(ano(1965))
print(ano(2016))

ano(1903)
ano(1932)
ano(1957)
ano(1963)
ano(1965)
ano(2016)


#3  - Não delete nem modifique esta linha
def numsear(s):
    if len(s) > 11:
        return ('','')
    elif len(s) ==10:
        return (s[0:2],s[2:])
    elif len(s) ==11 and int(s[2]) ==9:
        return (s[0:2],s[2:])    
    elif len(s) ==9 and int(s[0]) ==9:
        return ('',s)
    else:
        return ('','')

#Casos de teste da questão 3 - Não delete nem modifique esta linha
print(numsear("21912316165"))
print(numsear("1132316165"))
print(numsear("71912316165"))
print(numsear("323231616"))
print(numsear("912316165"))
print(numsear("11532316165"))

numsear("21912316165")
numsear("1132316165")
numsear("71912316165")
numsear("323231616")
numsear("912316165")
numsear("11532316165")


#4  - Não delete nem modifique esta linha
def format_data(s):
    dd=int(s[0:2])
    yy=int(s[6:8])
    mm=int(s[3:5])
    if mm == 0:
        return ()
    elif dd <= 31 and dd > 12 and mm > 12:
        return ()
    elif dd > 31 and mm > 12:
        return ()
    elif yy == 0 and mm < 12 and dd < 12 and dd > 0:
        return ('dd/mm/yy','mm/dd/yy')
    elif dd == 0 and mm < 12:
        return ('yy/mm/dd',)
    elif (mm == 12 and dd < 12) or (yy > 31 and mm == 12):
        return ('dd/mm/yy','mm/dd/yy')
    elif dd > 31 and mm <= 12:
        return ('yy/mm/dd',)
    elif yy > 31 and mm > 12: 
        return ('mm/dd/yy',)
    elif yy >= 0 and yy <= 31 and mm > 0 and mm <= 12:
        return ('dd/mm/yy','mm/dd/yy','yy/mm/dd')
    else:
        return ()


#Casos de teste da questão 4 - Não delete nem modifique esta linha
print(format_data('01/12/55'))
print(format_data('98/25/07'))
print(format_data('01/01/00'))
print(format_data('00/10/01'))
print(format_data('01/01/01'))
print(format_data('01/20/55'))
print(format_data('01/00/55'))
print(format_data('00/00/00'))
print(format_data('01/00/00'))
print(format_data('08/07/21'))


format_data('01/12/55')
format_data('98/25/07')
format_data('01/01/00')
format_data('00/10/01')
format_data('01/01/01')
format_data('01/20/55')
format_data('01/00/55')
format_data('00/00/00')
format_data('01/00/00')