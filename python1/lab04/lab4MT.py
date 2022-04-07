# Douglas Santos
# @ansattz


# 1 Manipulação de strings
# 1.
def concatenacao(a,b):
    """ A função organiza strings de uma forma particular;
    str, str -> str """
    return a + b + b + a
print(concatenacao('x', 'd'))


# 2. 
def substitui(s,x,i):
    """ A função substitui uma letra da string original e retorna a modificação;
    str, str -> int """
    sub = s[:i] + x + s[1+i:]
    return sub
print(substitui('jogar','b',2))


# 3.
def hashtag(s):
    """ A função adiciona hashtags no começo, no meio e no final de uma string;
    str -> str """
    n= len(s)//2 
    frasehast='#' + s[:n] + '#' + s[n:] + '#'
    return frasehast

print(hashtag('abcde'))


# 4.
def tup0t(tup):
    return tup[0]%2 ==0

def tup1t(tup):
    return tup[1]%2 ==0

def tup2t(tup):
    return tup[2]%2 ==0

def tup3t(tup):
    return tup[3]%2 ==0

def filtra_pares(tup):
    """ A função filtra elementos que são pares
    e os direciona em uma nova tupla
    tup -> tup """
    ftup=()
    if tup0t(tup):
        ftup = ftup + (tup[0],)
    if tup1t(tup):
        ftup = ftup + (tup[1],)
    if tup2t(tup):
        ftup = ftup + (tup[2],)
    if tup3t(tup):
        ftup = ftup + (tup[3],)
    return ftup
print(filtra_pares((2,7,5,7)))


# 5.
def colisao(tup,tup1):
    """ A função retorna se há colisão entre dois retângulos em R^2;
    tup, tuo -> bool """
    if tup[2] < tup1[0] or tup1[2] < tup[0] or tup[3] < tup1[1] or tup1[3] < tup[1]:
        return False
    else:
        return True
print(colisao((4,8,9,9),(2,1,9,5)))


