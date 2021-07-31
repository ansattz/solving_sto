# Nome: Douglas Vieira dos Santos
# DRE: 121062791

# 1  - Não delete nem modifique esta linha
def abss(x):
    """ Retornar o valor absoluto de inteiros e de números complexos;
    int -> float
    complex -> float """
    md=(x**2)**0.5
    return md

print(abss(complex(-3,-4)))


#2  - Não delete nem modifique esta linha
def qrreal(a,b,c):
    """ Função que retorna a quantidade de raízes reais de uma equação polinomial de grau n=2;
    int, int, int -> str """
    disc = b**2-4*a*c
    if disc>0:
        return "Duas raízes reais."
    elif disc<0:
        return "Nenhuma raíz real."
    else:
        return "Uma raíz real."

print(qrreal(6,-12,-210))


#3  - Não delete nem modifique esta linha
def strrep(str,x):
    """ A função retorna uma string com n repetições;
    str, int -> str """
    return str*x
str="Feliz aniversário!!\n"

print(strrep(str, 50000))


#4  - Não delete nem modifique esta linha
def calen(x,y,z):
    """ A função retorna o dia, mês e o ano em notação padrão de data;
    Dia,mês e ano como entradas;
    int, int, int -> str """
    dia=str(x)+' / '
    dia1=str(0) + str(x)+' / '
    mes=str(y)+' / '
    mes1=str(0) + str(y)+' / '
    ano=str(z)
    if x<10 and y<10:
        return dia1 + mes1 + ano
    elif x<10 and y>10:
        return dia1 + mes + ano
    elif x>10 and y<10:
        return dia + mes1 + ano
    else:
        return dia + mes + ano

print(calen(2,8,21))


#5  - Não delete nem modifique esta linha
#Número mínimo de testes: 5
def funcp(x):
    """ A função retorna a imagem de um função matemática definida em partes para valores
    maiores ou iguais a 0;
    float -> float """
    f_id=x
    f_const1=2
    f_const2=3
    f_quad=x**2-10*x+28
    if x<=0:
        return 0
    elif x>0 and x<=2:
        return f_id
    elif x>2 and x<=3.5:
        return f_const1
    elif x>3.5 and x<=5:
        return f_const2
    else:
        return f_quad

print(funcp(2))


#6a - Não delete nem modifique esta linha
def desc(sb):
    """ A função retorna o valor do desconto de INSS dado o salário bruto como entrada;
    float -> float """
    dk=0.06*sb
    tk=0.08*sb
    ddk=0.1*sb
    if sb>0 and sb<=2000:
        return dk
    elif sb>2000 and sb<=3000:
        return tk
    elif sb>3000:
        return ddk
    else:
        return "Valor incorreto"


#6b - Não delete nem modifique esta linha
def desc_ir(sb):
    """ A função retorna o valor do desconto de IR dado o salário bruto como entrada;
    float -> float """
    dmk=0.11*sb
    ck=0.15*sb
    cck=0.22*sb
    if sb>0 and sb<=2500:
        return dmk
    elif sb>2500 and sb<=5000:
        return ck
    elif sb>5000:
        return cck
    else:
        return "Valor incorreto"


#6c - Não delete nem modifique esta linha
def sal(sb):
    """ A função retorna o salário líquido dado o salário bruto como entrada utilizando
    as funções de desconto de INSS e IR
    float -> float """
    sliquido=sb -(desc(sb) + desc_ir(sb))
    return sliquido
    
print(sal(20000))

