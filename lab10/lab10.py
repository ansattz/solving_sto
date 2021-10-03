# Nome: Douglas Vieira dos Santos
# DRE: 121062791

#1 - Não delete nem modifique esta linha
import readline
from random import randint
def roll(t):   
    rounds=[]
    while len(rounds) < t:
        round0=randint(1,6)
        rounds.append(round0)
    return rounds

def facerep(t):
    mydic={}
    l=roll(t)
    l1=l[1:] + [':)',]
    ls=[]
    z=0
    for i in l:
        if i == l1[z]:
            ls.append(i)
        z+=1
    for j in ls:
        mydic[j] = mydic.get(j, 0) + 1      
    v = list(mydic.values())
    return l , len(v)

def main():
    # Escolha da quantidade de lances pelo usuário
    print('')
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣀⠤⠤⢴⣶⣖⣈⣉⣻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣷⣶⡶⠚⠛⢻⣿⣯⣤⣤⣽⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠛⢛⣿⣷⣤⣤⣴⣿⣿⣿⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⡟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣷⠀⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢻⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣿⣿⡀⢹⣿⣿⣿⣿⡟⠁⠀⣿⣿⣿⣿⣿⣀⣀⣼⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠙⣿⣷⣼⣿⣿⣿⣿⣧⣤⣴⣿⣿⠿⠿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣆⣸⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⢀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⢹⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣶⣿⣿⣿⣿⡿⠁⠀⣹⣿⣿⣿⣿⣤⣴⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⡿⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡿⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    t = int(input('Quantidade de lances: '))

    print('')
    print('===== Resultados =====')
    # print('Números sorteados e número de séries de faces repetidas:\n', facerep(t))
    print('Número de séries de faces repetidas:', facerep(t)[1])
# main()


#Casos de teste da questão 1 - Não delete nem modifique esta linha
# input: 0 ====> output: 0
# input: 1 ====> output: 0
# input: 2 ====> output: 1 or 0
#     ...


#2 - Não delete nem modifique esta linha
def trap_area(a,b,c):
    return (((a+b))*c)/2

def quad(a,b,c):
    return [a**2, b**2, c**2]

def marit(a,b,c):
    return (a+b+c)/3

def seq(a,b,c):
    l=[]
    i=a
    if a < b:
        while a < b:
            a+=c
            l.append(a)
        del l[-1]
        return i + sum(l)
    else:
        return "Não foi possível realizar a operação, pois (a > b)"

def mymenu():
    print('========= Opções válidas =========')
    print('')
    print('1 - Área do trapézio de bases a e b e altura c')
    print('2 - Quadrados de a, b e c')
    print('3 - Média aritmética entre a, b e c')
    print('4 - Sequência aritmética de a com um limite superior sendo b e razão c')
    print('0 - Encerrar programa')
    print('')
    print('==================================')

while True:
    mymenu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        a = float(input('Base a: '))
        b = float(input('Base b: '))
        c = float(input('Altura c: '))
        print('')
        print('A área do trapézio é: ', trap_area(a,b,c))
        print('')
    elif opcao == '2':
        a = float(input('Valor de a: '))
        b = float(input('Valor de b: '))
        c = float(input('Valor de c: '))
        print('')
        print(str.format('Os quadrados são:\n {}: {} \n {}: {} \n {}: {} ', a, quad(a,b,c)[0], b, quad(a,b,c)[1], c, quad(a,b,c)[2]))
        print('')
    elif opcao == '3':
        a = float(input('Primeiro valor (a): '))
        b = float(input('Segundo valor (b): '))
        c = float(input('Terceiro valor (c): '))
        print('')
        print(str.format('A média aritmética entre {}, {} e {} é: ', a, b, c, marit(a,b,c)))
        print('')
    elif opcao == '4':
        a = int(input('Primeiro termo (a): '))
        b = int(input('Limite superior (b): '))
        c = int(input('Razão da sequência (c): '))
        print('')
        print(str.format('A sequência aritmética de {} com limite superior {} e com razão {} é: ', a, b, c), seq(a,b,c))
        print('')
    elif opcao == '0':
        print('')
        print('=====> Programa encerrado :)')
        break
    else:
        print('Opção inválida')
        print('')