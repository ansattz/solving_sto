## (*) Exercício

def nome():
  ...

def dre():
  ...

## Faremos um procedimento --- chamado quantas_vezes() --- que simule
## um jogo de dois dados.  Seu procedimento deve contar quantas vezes
## os dados foram lançados até que saiam números repetidos.  (Lançar
## dois dados conta como um único lançamento.)  O que seu procedimento
## deve retornar?  Ele deve retornar a quantidade de lançamentos
## efetuados e os dois números [iguais] obtidos --- coloque os três
## valores numa tupla.  Assuma que seu dado tem 6 lados.  Use o
## procedimento randint do módulo random para simular a jogada de um
## dado.  A documentação desse procedimento você encontra em
## https://cutt.ly/dWsa2Rl.  Note que seu procedimento não recebe
## qualquer valor como entrada.


import random
def dados():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return (dice1, dice2)

def quantas_vezes():
    x, y = dados()
    n = 1
    while x != y:
      x, y = dados()
      n+=1
    return (n,) + (x, y)

print(quantas_vezes())

## (*) Sugestão de como fazer
## 
## Primeiro aprenda a usar o módulo random.  Precisamos importá-lo e
## compreender o procedimento randint(a, b).  Por exemplo, a interação
## com o shell aqui deve fazer perfeito sentido pra você.
##
## >>> import random
## >>> random.randint(1, 6)
## 2
## >>> random.randint(1, 6)
## 4
## >>> random.randint(1, 6)
## 4
## >>> random.randint(1, 6)
## 1
##
## Agora crie um procedimento chamado dados() que use o módulo random
## como acima e a cada vez que dados() é invocado, ele retorna uma
## tupla contendo dois sorteios.  Experimente seu procedimento no seu
## shell.
##
## >>> dados()
## (5, 2)
## >>> dados()
## (6, 4)
## >>> dados()
## (1, 5)
## >>> dados()
## (2, 3)
## >>> dados()
## (3, 3)
##
## Relembre agora as habilidades que você obteve no curso sobre o uso
## de tupla:
##
## >>> x, y = dados()
## >>> x
## 6
## >>> y
## 6
## 
## >>> x, y = dados()
## >>> x
## 4
## >>> y
## 1
##
## O que ocorreu aí?  Pedimos a Python que os elementos da tupla
## retornada por dados() fossem atribuídos aos nomes x e y.  Na
## primeira vez, obtivemos 6 e 6.  Na segunda, 4 e 1.
##
## Agora retorne ao exercício e use um laço ``while'' para resolvê-lo.