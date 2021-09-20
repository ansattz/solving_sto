# #Q1
def eh_quadrada(mat):
    null=[]
    l=len(mat)
    if mat == null or l == len(mat[0]):
        return True
    for i in range(l):
        if mat[i] == null:
            return True
    else:
        return False
#Q2
def conta_numero(n,mat):
    ls=[]
    l=len(mat)
    if mat == ls:
        return 0
    for i in range(l):
        for j in range(len(mat[0])):
            if mat[i][j] == n:
                ls.append(n)
    return len(ls)
#Q3
def media_matriz(mat):
    ls=[]
    l=len(mat)
    if mat == ls:
        return 0
    for i in range(l):
        for j in range(len(mat[0])):
            ls.append(mat[i][j])
    s=sum(ls)/(l * len(mat[0]))
    return round(s,2)
#Q4
def melhor_volta(mat):
    cnls1=[]
    cnls2=[]
    for i in range(len(mat)):
        cnls1.append(min(mat[i]))
        cnls2.append(mat[i].index(min(mat[i])))
    indtemp=cnls1.index(min(cnls1))
    indvolt=cnls2[indtemp]
    mat1=list(range(0,6))
    venc=mat1[indtemp]
    return (venc+1,min(cnls1),indvolt+1)
#Q5
def busca(s,mat):
    ls=[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if s == mat[i][j]:
                ls.append(mat[i])
    for k in range(len(ls)):
        if s in ls[k]:
            ls[k].remove(s)
    return ls