# Douglas Santos
# @ansattz

#1
def lookingfterms(x,y):
    """ A função retorna o número de vezes em que um termo aparece em um iterável;
    iter -> int """
    n=0
    for term in x:
        if term == y:
            n+=1
    return n
#Casos de teste da questão 1
# print(lookingfterms([1,2,5,4,5,5,2,3],5))
# print(lookingfterms([1,2,5,4,5,5,2,3],2))
# print(lookingfterms([1,2,5,4,5,5,2,3],1))
# print(lookingfterms("Geometria simplética","e"))
# print(lookingfterms("Topologia algébrica","i"))
# print(lookingfterms(('A','B','A+B','C','K','K+(A+B)','K','C'),'K'))
# print(lookingfterms(('A','B','A+B','C','K','K+(A+B)','K','C','C'),'C'))
# print(lookingfterms(('A','B','A+B','C','K','K+(A+B)','K','C'),'A'))

lookingfterms([1,2,5,4,5,5,2,3],5)
lookingfterms([1,2,5,4,5,5,2,3],2)
lookingfterms([1,2,5,4,5,5,2,3],1)
lookingfterms("Geometria simplética","e")
lookingfterms("Topologia algébrica","i")
lookingfterms(('A','B','A+B','C','K','K+(A+B)','K','C'),'K')
lookingfterms(('A','B','A+B','C','K','K+(A+B)','K','C','C'),'C')
lookingfterms(('A','B','A+B','C','K','K+(A+B)','K','C'),'A')


#2
def lftwcond(x,y,linf,lsup):
    """Recebe um iteravel e um inteiro y. Retorna a quantidade de vezes
    que y aparece entre linf e lsup;
    list, int, int, int -> int"""
    return lookingfterms(x[linf:lsup], y)


#Casos de teste da questão
# print(lftwcond([11,13,13,17,17,17,19,19,23,23,29,31,37],19,2,7))

lftwcond([11,13,13,17,17,17,19,19,23,23,29,31,37],19,2,7)

#3
def atualiza_mascara(w,lis,s):
    """Atualiza a máscara colocando a letra escolhida no lugar (caso esteja na palavra);
    str, list, str -> str"""
    i=0
    while i < len(w):
        if s == w[i]:
            del lis[i]
            lis.insert(i,s)
        i+=1
    return ' '.join(lis)

#Casos de teste da questão
# print(atualiza_mascara('carta',['-','-','-','-','-'],'a'))
# print(atualiza_mascara('carta',['-','a','-','-','a'],'t'))
# print(atualiza_mascara('carta',['-','a','-','-','a'],'k'))
# print(atualiza_mascara('john von neumann',['j','-','h','-',' ','v','-','-',' ','-','-','u','m','-','-','-'],'n'))

atualiza_mascara('carta',['-','-','-','-','-'],'a')
atualiza_mascara('carta',['-','a','-','-','a'],'t')
atualiza_mascara('carta',['-','a','-','-','a'],'k')
atualiza_mascara('john von neumann',['j','-','h','-',' ','v','-','-',' ','-','-','u','m','-','-','-'],'n')


#4a
def sig(n):
    """Calcula a soma de uma série particular até n;
    int -> float"""
    ls=[]
    for i in range(0,n+1):
        ls.append(((-1)**i)/((2*i) +1))
    return sum(ls)
    
# Casos de teste da questão
# print(sig(4))
sig(4)

#4b
import math
def sige(n):
    """Calcula a soma da série particular com erro inferior a 0,01;
    int -> float"""
    l=[]
    e=math.pi/4
    while math.fabs(sig(n) - e) > 1/100:
        l.append(math.fabs(sig(n) - e))
        n+=1
        if math.fabs(sig(n) - e) < 1/100:
            l.append(math.fabs(sig(n) - e))
            return (min(l),len(l))
    return math.fabs(sig(n) - e) , len(l)

#Casos de teste da questão
sige(27)