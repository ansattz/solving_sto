# -*- mode: python; python-indent-offset: 2 -*-
## (*) Laboratório 9, IDLE

def nome():
  ...

def dre():
  ...

## (*) Instruções
##
## 1. *Não* renomeie qualquer procedimento.
## 2. Use *todos* os argumentos em cada procedimento.
## 3. Adicione casos de teste como comentários.

## (*) Questão 1
##
## Exemplos:
##
## >>> m2 = [[1,1,1], [2,2,2], [3,3,0]]
## >>> mat_vezes_numero(m, -0.5)
## [[-0.5, -0.5, -0.5], [-1.0, -1.0, -1.0], [-1.5, -1.5, -0.0]]
##
## >>> m2 # note que não alteramos m2
## [[1, 1, 1], [2, 2, 2], [3, 3, 0]]
##
## >>> m1 = [[1,0,0], [0,1,0], [0,0,1]]
## 
## >>> mat_vezes_numero(m1, 1)
## [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
## 
## >>> m1
## [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
## 
## >>> mat_vezes_numero([], 17)
## []
## 
def mat_vezes_numero(mat, n):
    m=[]
    l=len(mat)
    for i in range(l):
        row=[]
        for j in range(len(mat[0])):
            row.append(mat[i][j]*n)
        m.append(row)
    return m
# mat_vezes_numero([[1, 0, 0], [0, 1, 0], [0, 0, 1]],5)
print(mat_vezes_numero( [[[1, 2, 3]], 10], 2))

## (*) Questão 2
## 
## Ver exemplos no PDF.
dic1 = {
'Leo': ['Sofia', 'Andrea', 'Bia'],
'Marcos': ['Andrea', 'Bia'],
'Sofia': ['Leo'],
'Alex': ['Andrea', 'Marcos'],
'Andrea': ['Marcos'],
'Bia':['Sofia']
}
dic2 = {
    'Bruno': ['David Hilbert'],
    'John von Neumann': ['Kurt Godel'],
    'Hermann Minkowski': ['David Hilbert'],
    'Kurt Godel': ['John von Neumann'],
    'Richard Courant': ['Hermann Minkowski'],
    'David Hilbert': ['John von Neumann', 'Bruno', 'Kurt Godel', 'Richard Courant', 'Hermann Minkowski']
}

def deu_match_v1(d):
    cmutuo=[]
    for name in d:
        for namev in d[name]:
            if name in d[namev]:
                cmutuo.append((name, namev))
    k=len(cmutuo)//2
    return cmutuo[:k]

# deu_match_v1(dic1)
# deu_match_v1(dic2)

## (*) Questão 3
##
## Exemplos:
##
## agenda = [['Bruno Campos',['21988881122', '2133992211'], 'b@c.com', '@bruno91'], 
##           ['John Smith',  ['21988883344'], 'j@s.com', '@js92'],
##           ['Bombeiros', ['193'], '', '']]
##
## >>> quem_ligou(agenda, '21988881122')
## ['Bruno Campos', ['21988881122', '2133992211'], 'b@c.com', '@bruno91']
##
## >>> quem_ligou(agenda, '190')
## []
## 
## >>> quem_ligou(agenda, '21988883344')
## ['John Smith',  ['21988883344'], 'j@s.com', '@js92']
## 
## >>> quem_ligou(agenda, '193')
## ['Bombeiros', ['193'], '', '']



agenda = [['Bruno Campos',['21988881122', '2133992211'], 'b@c.com', '@bruno91'], 
          ['John Smith',  ['21988883344'], 'j@s.com', '@js92'],
          ['Bombeiros', ['193'], '', '']]
def quem_ligou(agenda, tel):
    nl=[]
    lim=len(agenda)
    for i in range(lim):
        for j in range(len(agenda[i])):
            for k in range(len(agenda[i][j])):
                if agenda[i][j][k] == tel:
                    return agenda[i]
    return nl

# quem_ligou(agenda, '21988881122')
# quem_ligou(agenda, '19')


## (*) Questão 4
##
## Renomeie o nome do seu arquivo (que neste momento se chama lab9.py)
## para o nome determinado pelo procedimento meu_arquivo() ---
## execute-o em seu IDLE para saber.

def meu_arquivo():
  ls = ["lab9", str(dre()), str(nome())] # meus dados
  s1 = str.join(" ", ls) # coloque um espaço entre eles
  s2 = str.replace(s1, " ", "_")
  return s2 + ".py"