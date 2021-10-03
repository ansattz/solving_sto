from random import shuffle as sf
def matriz():
    m=[]
    for i in range(0,4):
        row=[]
        for j in range(0,4):
            row.append(0)
        m.append(row)
    return m

def num():
    ls= list(range(1,8+1))
    sf(ls)
    for i in ls:
        for j in range(len(matriz())):
            for k in range(len(matriz()[j])):
                matriz().insert(k,i)
    return matriz()
    
print(num())