# Q1
def freq_palavras(frases):
    """A função retorna quantas vezes uma palavra aparece numa frase;
    str -> dict"""
    ed1=frases.replace(',','')
    ed2=ed1.replace('!','')
    ed3=ed2.replace('.','')
    ed4=ed3.replace('?','')
    ed5=ed4.replace(';','')
    i=0
    nls=[]
    nnls=[]
    f=ed5.split(' ')
    f2=ed5.split(' ')
    while i < len(f):
        if f[i] == f2[i]:
            nnls.append(f.count(f[i]))
            nls.append(f2[i])
        i+=1
    return dict(zip(nls,nnls))
# Q2
def total(lis,mydic):
    """ A função retorna o valor total dos produtos disponíveis de uma lista;
    list, dict -> float """
    vtotal = 0
    for prod in lis:
        vtotal+=mydic[prod]
    return round(vtotal,3)
# Q3
def lingua_p(s):
    i=0
    ss=s.lower()
    myc=list(ss)
    while i < len(s):
        if ss[i] in 'AEIOUaeiouãéêàáíú':
            del myc[i]
            myc.insert(i,ss[i] + 'p' + ss[i])
        i+=1
    return ''.join(myc)
# Q4
def qtd_divisores(n):
    """ A função retorna a quantidade de divisores positivos inteiros de um número inteiro n;
    int -> int """
    ls=[]
    i=1
    for i in range(1,n+1):
        if n%i == 0:
            ls.append(i)
        i+=1
    return len(ls)
# Q5
def prime(n):
    """ verifica se o número é primo;
    int -> bool """
    ls=[]
    i=1
    for i in range(1,n+1):
        if n%i == 0:
            ls.append(i)
        i+=1
    if len(ls) < 2 or len(ls) > 2:
        return False
    else:
        return True
# Q6
def soma_h(n):
    """ Somatório de 1 sobre um dado número inteiro n;
    int -> float """
    ls=[]
    for i in range(1,n+1):
        if i != n+1:
            ls.append(1/i)
    return sum(ls)