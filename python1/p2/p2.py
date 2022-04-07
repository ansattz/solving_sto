# (*) Burocracia

def nome():
  return ...

def dre():
  return ...

def meu_arquivo():
  ls = ["p2", str(dre()), str(nome())] # meus dados
  s1 = str.join(" ", ls) # coloque um espaço entre eles
  s2 = str.replace(s1, " ", "_")
  print(s2 + ".py")

# Obrigado!

# (*) Questão 1
# 
# Você vai escrever três procedimentos muito similares.  O primeiro
# adiciona uma unidade a cada inteiro da lista de entrada.  O segundo
# adiciona duas unidades.  O terceiro adiciona sete unidades.  Seu
# trabalho aqui é só preencher a lacuna demarcada por ``...''.
# (Remova a lacuna e adicione o que você acha que completa o
# procedimento.  É isso que significa preencher a ``lacuna''.)

def ls_add_one(ls):
  ret = []
  for e in ls:
    list.append(ret, e+1)
  return ret

def ls_add_two(ls):
  ret = []
  for e in ls:
    list.append(ret, e+2)
  return ret

def ls_add_seven(ls):
  ret = []
  for e in ls:
    list.append(ret, e+7)
  return ret

# Certifique-se de que os procedimentos acima funcionam como se deseja
# usando o procedimento testes_add.  Se alguma linha disser False, então
# algum procedimento seu acima está incorreto.

def testes_add():
  print("ls_add_one:", ls_add_one([]) == [])
  print("ls_add_one:", ls_add_one([1]) == [2])
  print("ls_add_one:", ls_add_one([-9,80,10]) == [-8,81,11])
  print("ls_add_two:", ls_add_two([]) == [])
  print("ls_add_two:", ls_add_two([1]) == [3])
  print("ls_add_two:", ls_add_two([-9,80,10]) == [-7,82,12])
  print("ls_add_seven:", ls_add_seven([]) == [])
  print("ls_add_seven:", ls_add_seven([1]) == [8])
  print("ls_add_seven:", ls_add_seven([-9,80,10]) == [-2,87,17])

# (*) Questão 2
# 
# Uma razão de se escrever programas é automatizar um trabalho para que
# nós não precisemos nos repetir.  Por um lado os procedimentos da
# questão anterior nos evitam o trabalho de somar números; por outro,
# estamos nos repetindo o tempo todo ao escrevê-los.  Uma solução
# ingênua para o trabalho excessivo gerado pela questão 1 é abstrair o
# procedimento através de um argumento n.

def ls_add_n(ls, n):
  ret = []
  for e in ls:
    list.append(ret, e + n)
  return ret

# Agora podemos adicionar 1, 2, 7 ou qualquer número n.  Mas essa
# solução é ingênua porque ela assume que tudo que faremos daqui pra
# frente é adicionar números.  Por exemplo, complete as lacunas do
# procedimento ls_show_add_seven de forma que ele satisfaça os testes
# abaixo.

def ls_show_add_seven(ls):
  ret = []
  for e in ls:
    list.append(ret, str.format("{} + 7 = {}", e, e+7))
  return ret

def testes_show():
  print("ls_show_add_seven 1:", ls_show_add_seven([]) == [])
  print("ls_show_add_seven 2:", ls_show_add_seven([1,2]) == ["1 + 7 = 8", "2 + 7 = 9"])
  print("ls_show_add_seven 3:", ls_show_add_seven([13]) == ["13 + 7 = 20"])

# Não seria muito óbvio usar ls_add_n para computar o procedimento
# ls_show_add_seven --- isto é, usar ls_add_n sem recorrer a novos
# laços ---, embora ambos procedimentos sejam muito próximos um do
# outro.  Por isso dizemos (contextualmente) que aquela solução é
# ingênua: continuamos a recorrer a um novo laço-for em
# ls_show_add_seven(ls), iterando elemento a elemento.  (Assim a vida
# fica entediante, trabalhosa, árdua, difícil.  É por isso que tantas
# pessoas acabam detestando a ideia de programar --- falta-lhes mais
# técnica.)

# (*) Questão 3
# 
# Vimos em aula que não só listas e números /et cetera/ podem ser
# passados como argumentos para procedimentos, mas os próprios
# procedimentos também podem ser argumentos de outros procedimentos, o
# que é ilustrado por add_f(f, ls).

def add_f(f, ls):
  ret = []
  for e in ls:
    list.append(ret, f(e))
  return ret

# O procedimento add_f consome um procedimento /f/ e uma lista /ls/.
# 
# (/) Sua vez
# 
# Questão dissertativa.  Diga com suas palavras o efeito de
# 
#   add_f(add5, [1, 2, 3, 4]),
# 
# sendo que add5 é o procedimento abaixo.

def add5(n):
  return n + 5

# Coloque sua resposta no procedimento questao3_resposta.

def questao3_resposta():
  return """
Cada inteiro contido na lista passada como entrada na função add_f será
acrescentado de 5 unidades e adicionado em uma nova lista, retornando esta nova lista.
Com efeito, a regra que rege sob ls por add_f é que cada elemento de ls seja somado 5.
"""
# Agora preencha a lacuna abaixo.

def ls_add_five(ls):
  return add_f(add5, ls)

def testes_add_five():
  print("add_five 1:", ls_add_five([]) == [])
  print("add_five 2:", ls_add_five([1,2]) == [6,7])

# O relevante aqui é que não escrevemos um laço-for em ls_add_five, o
# que seria dificilmente evitável se usássemos ls_add_n.

# (/) Sua vez
# 
# Preencha a lacuna no procedimento my_ls_show_add_seven de forma que os
# testes sejam satisfeitos.

def show_add7(n):
  return str.format("{} + 7 = {}", n, n + 7)

def my_ls_show_add_seven(ls):
  return add_f(show_add7, ls)

def testes_my_show():
  print("my_ls_show_add_seven 1:", my_ls_show_add_seven([]) == [])
  print("my_ls_show_add_seven 2:", my_ls_show_add_seven([1,2]) == ["1 + 7 = 8", "2 + 7 = 9"])

# (*) Intermezzo 1
# 
# A ideia de usar procedimentos como argumentos de procedimentos é tão
# importante que têm seu próprio nome.  Quando um procedimento tem
# esse tipo de poder, dizemos que tais procedimentos são
# ``procedimentos de primeira classe''.  (O termo é uma referência a
# ``cidadão de primeira classe'', aquele que tem todos os direitos
# garantidos pela lei maior de uma sociedade.  Estrangeiros no Brasil 
# não são cidadãos de primeira classe porque, por exemplo, não podem
# votar.)
# 
# Recordemos um problema que nos serve de ilustração sobre o poder de
# expressão oriundo dessa ideia.  A questão 1 do laboratório 9 pede
# pra você escrever um procedimento que consome uma matriz /M/ e um
# número, produzindo a multiplicação de M pelo número.  (A solução que
# aplicamos lá era essencialmente dois laços-for aninhados.)

def vezes7(n):
  return n * 7

def linha_vezes7(ls):
  return add_f(vezes7, ls)

def mat_vezes7(mat):
  return add_f(linha_vezes7, mat)

# >>> mat_vezes7([[1,2,3],[4,5,6]])
# [[7,  14, 21], [28, 35, 42]]

# O que fizemos acima é simplesmente usar add_f, que é um único laço.
# A solução aparece porque reutilizamos o mesmo laço.  

# Note que ``add_f'' é um nome inadequado agora, afinal seu uso não
# está mais restrito a adições.  O nome que as linguagens de
# programação dão a esse procedimento é ``map''.  Por exemplo, usando
# o ``map'' de Python, obtemos:

# >>> list(map(linha_vezes7, [[1,2,3],[4,5,6]]))
# [[7,  14, 21], [28, 35, 42]]

# Por que ``map''?  O nome vem de cultura matemática.  Os matemáticos
# gostam de dizer que uma função ``mapeia'' seu domínio a sua imagem.
# (O domínio é transformado em sua imagem --- por virtude do trabalho
# de f.  Neste documento, daremos o nome ``mapeia'' em vez de add_f.)

mapeia = add_f

# >>> mapeia = add_f
# >>> mapeia
# <function add_f at 0x01282ED0>
#
# >>> mapeia(linha_vezes7, [[1,2,3],[4,5,6]])
# [[7, 14, 21], [28, 35, 42]]

# (*) Intermezzo 2
# 
# Faremos agora uma observação sobre a assinatura de procedimentos.
#
# As questões 1--3 estão preocupadas com o padrão de consumir uma lista
# e produzir uma lista com o mesmo número de elementos.  Por exemplo,
# adicionar 7 a cada elemento de [1,2,3] produz uma lista com três
# elementos --- [8,9,10].  É o mesmo que ocorre em multiplicar uma
# matriz por um número: se a matriz possui três linhas, o resultado
# final continua a ser três linhas.  A assinatura de ambos é
# 
#   lista-de-n-elementos --> list-de-n-elementos.
# 
# Quando você identifica que um procedimento tem essa assinatura, então
# já sabe que está diante de um ``map'' e não precisará escrever mais um
# laço-for.
# 
# ,----
# | Atenção, portanto, às assinaturas.
# `----
# 
# A questão filtra_pares --- lembra dela? --- não tem essa assinatura
# porque se um número na lista de entrada for ímpar, a quantidade de
# elementos na lista de saída será menor.  Uma assinatura mais adequada
# para filtra_pares seria
# 
#   lista-com-x-elementos --> lista-com-y-elementos
# 
# Mas --- assim como mapeamentos ---, filtragem é um padrão muito
# recorrente.  Python chama filtragem de ``filter'', mas em vez de
# ``filtro'', usaremos a palavra ``coleta'' porque ``filtragem'' é uma
# noção ambígua: quando filtramos água, obtemos o quê?  Água limpa que
# sai do filtro ou as impurezas que ficam no filtro?  Pra evitar esse
# impasse, usamos ``coleta'', o que nos remete àquilo que levamos
# conosco ao fim de uma busca.

# (*) Questão 4
# 
# Preencha a lacuna abaixo de forma que só números 2 sejam coletados.

def coleta_2(ls):
  ret = []
  for e in ls:
    if e == 2:
      list.append(ret, e)
  return ret

def teste_coleta_2():
  print("coleta_2:", coleta_2([1,2,3]) == [2])
  print("coleta_2:", coleta_2([]) == [])
  print("coleta_2:", coleta_2([2,2,2]) == [2,2,2])

# Preencha a lacuna abaixo de forma que só números 3 sejam coletados.

def coleta_3(ls):
  ret = []
  for e in ls:
    if e == 3:
      list.append(ret, e)
  return ret

def teste_coleta_3():
  print("coleta_3:", coleta_3([1,2,3]) == [3])
  print("coleta_3:", coleta_3([]) == [])
  print("coleta_3:", coleta_3([2,2,2]) == [])

# (*) Questão 5
# 
# Preencha a lacuna abaixo de forma que o procedimento coleta_pares(ls)
# colete os números pares da lista /ls/.

def eh_par(n):
  """ O resto da divisão de n por 2 é zero?  Se sim, retorna True.  Se
  não, retorna False."""
  if (n%2 == 0):
      return True
  else:
      return False

def coleta_se_eh_par(ls):
  ret = []
  for e in ls:
    if eh_par(e):
      list.append(ret, e)
  return ret

# (*) Questão 6
# 
# Preencha a lacuna abaixo de forma que o procedimento
# coleta_impares(ls) colete os números ímpares da lista /ls/.

def eh_impar(n):
  return not eh_par(n)

def coleta_se_eh_impar(ls):
  ret = []
  for e in ls:
    if eh_impar(e):
      list.append(ret, e)
  return ret

# (*) Questão 7
# 
# Escreva um procedimento chamado coleta_se(f, ls).  O procedimento
# recebe um procedimento /f/ e uma lista /ls/.  Esse procedimento /f/ é
# sempre um ``predicado'' --- isto é, um procedimento que retorne True
# ou retorne False, não havendo outras possibilidades.

# ``Predicar'' é dizer se alguma coisa tem ou não tem certa qualidade.
# Quando tem, True; quando não, False.  (Um dicionário qualquer nos
# corroborará.)

def coleta_se(f, ls):
  ret = []
  for e in ls:
    if f(e) == True:
      list.append(ret, e)
  return ret

def always_false(x):
  return False

def always_true(x):
  return True

# Teste seu procedimento.

def teste_coleta_se():
  print("coleta_se:", coleta_se(always_false, [1,2,3]) == [])
  print("coleta_se:", coleta_se(always_true, []) == [])
  print("coleta_se:", coleta_se(always_true, [1,2,3,4]) == [1,2,3,4])
  print("coleta_se:", coleta_se(eh_par, range(1,3+1)) == [2])
  print("coleta_se:", coleta_se(eh_impar, range(1,3+1)) == [1,3])

# (*) Questão 8 
# 
# Recorde agora a 
# 
#   ``questão(numero = 2, lab = 8, sistema = "machine-teaching")''
# 
# Ela apresenta uma tupla de compras e uma tabela de preços, o que
# podemos representar aqui por estes procedimentos.

def lista_de_compras():
  """Sou, na verdade, uma tupla de coisas a serem compradas."""
  return 'biscoito', 'chocolate', 'farinha'

def tabela_de_precos():
  return {
    'amaciante':4.99,
    'arroz':10.90,
    'biscoito':1.69,
    'cafe':6.98,
    'chocolate':3.79,
    'farinha':2.99
  }

# O objetivo da questão era somar o custo total dessa ``lista'' de
# compras.  Não é o que faremos agora: queremos apenas uma lista
# contendo os preços dos produtos.  (Somaremos a lista em breve.)

# Preencha a lacuna:

def custo(p):
  d = tabela_de_precos()
  return d[p]

# >>> custo("biscoito")
# 1.69
# >>> custo("cafe")
# 6.98

# Preencha as lacunas abaixo:

def lista_com_custo_total(tupla_de_compras):
  return mapeia(custo, tupla_de_compras)

# >>> lista_com_custo_total(lista_de_compras())
# [1.69, 3.79, 2.99]

# (*) Intermezzo 3
# 
# Note, portanto, que o procedimento mapeia não está limitado a
# listas.  Ele itera tuplas também porque ele usa um laço-for que
# itera esses tipos de dado também.  Entretanto, não seria óbvio para
# /mapeia/ produzir aqui a soma desse custo total porque /mapeia/ foi
# projetada para produzir uma lista e não um número.
# 
# Quando queremos consumir uma lista de dados e produzir uma resposta
# atômica como é o caso de consumir [1.69, 3.79, 2.99] e produzir o
# número 8.47, precisamos de uma terceira estratégia que não é um
# mapeamento e não é uma filtragem, mas uma redução de um dado
# complexo para um dado atômico.  (Lembre-se de que ``complexo'' é uma
# palavra que faz referência a uma coisa com múltiplas partes, como
# listas ou tuplas ou dicionários.  ``Átomo'' é uma palavra que faz
# referência a uma coisa indivisível, ou seja, composta de uma única
# parte como é um número no contexto Python.)
# 
# Uma estratégia que reduza uma coisa complexa a uma coisa atômica
# teria uma assinatura como
# 
#   coisa-complexa --> átomo
# 
# Por exemplo, se consumimos uma lista de números e produzimos um
# número, então uma assinatura adequada seria
# 
#   lista-de-números --> número,
# 
# que não é a assinatura nem de /mapeia/ e nem de /coleta_se/.

# (*) Questão 9
# 
# Escreveremos agora um procedimento que consume uma lista de números
# como [1.69, 3.79, 2.99] e produz a soma 1.69 + 3.79 + 2.99.  Preencha
# a lacuna.

def ls_soma(ls):
  soma = 0 # valor inicial
  for n in ls:
    soma+=n
  return soma

# >>> ls_soma([1.69,3.79, 2.99])
# 8.47

# (*) Questão 10
# 
# Escreveremos agora um procedimento que consume uma lista de números
# como [1, 2, 3] e produz o produto 1 * 2 * 3.  Preencha a lacuna.

def ls_produto(ls):
  prod = 1 # valor inicial
  for n in ls:
    prod*=n
  return prod

# >>> ls_produto([1,2,3,4,5])
# 120

# (*) Intermezzo 4
# 
# O que esses procedimentos têm em comum?  O laço é o mesmo, mas eles
# usam valores iniciais diferentes e a operação matemática usada nos
# elementos da lista também muda.  

# Compare-os também com mapeia e coleta_se.  Uma diferença importante
# entre ls_soma, ls_produto, mapeia e coleta_se é que ls_soma e
# ls_produto usam operações matemáticas que são binárias, ao contrário
# dos procedimentos f que são passados como argumento para /mapeia/ ou
# /coleta_se/ --- aqueles são unários.
# 
# Eis uma abstração de ls_soma e ls_produto.

def reduce(f_binaria, ls, valor_inicial):
  v = valor_inicial
  for e in ls:
    v = f_binaria(v, e)
  return v

# Uma forma interessante de se pensar no procedimento ls_soma é que
# ele transforma a lista [v1, v2, v3, ..., vN] na expressão
#
#  0 + v1 + v2 + v3 + ... + vN.
#
# Aplicando a mesma ideia a ls_produto, diremos que ele transforma a
# lista [v1, v2, v3, ..., vN] na expressão
#
#  1 * v1 * v2 * v3 * ... * vN.
#
# Agora, como estamos treinados em dois casos particulares muito
# parecidos, podemos generalizá-los num padrão mais abstrato: podemos
# dizer que /reduce/ transforma uma lista de valores [v1, v2, v3, ...,
# vN] na expressão
# 
#   valor_inicial @ v1 @ v2 @ v3 @ ... @ vN
# 
# sendo ``@'' a operação binária representada por f_binaria.

# (*) Questão 11

def soma(x, y):
  return x + y

# Preencha a lacuna:

def ls_reduce_soma(ls):
  return reduce(soma, ls, 0)

# >>> ls_reduce_soma([1.69,3.79, 2.99])
# 8.47

# (*) Questão 12

def produto(x, y):
  return x * y

# Preencha a lacuna:

def ls_reduce_produto(ls):
  return reduce(produto, ls, 1)

# >>> ls_reduce_produto([1, 2, 3, 4])
# 24

# (*) Questão 13
#
# Recorde agora a 
# 
#   ``questão(número = 6, lab = 8, sistema = "machine-teaching")''
# 
# Compute a soma
# 
#   H = 1/1 + 1/2 + 1/3 + ... + 1/N.
# 
# usando a estratégia abaixo, ou seja, preencha as lacunas no
# procedimento soma_h, mas antes estude os seguintes procedimentos
# auxiliares.  Comecemos por gerar os denominadores.

def ls_1_ate_N(n):
  return list(range(1, n + 1))

# >>> ls_1_ate_N(10)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Queremos os inversos multiplicativos desses números.

def inverso_multiplicativo(i):
  return 1 / i

# >>> mapeia(inverso_multiplicativo, ls_1_ate_N(10))
# [1.0, 0.5, 0.3333333333333333, 0.25, 0.2, ..., 0.1]
#
# Agora queremos a soma deles.  Por exemplo, a soma dos dois primeiros
# é apenas 1 + 0.5.  De fato,
#
# >>> ls_reduce_soma(mapeia(inverso_multiplicativo, ls_1_ate_N(2)))
# 1.5

# Preencha as lacunas.

def soma_h(n):
  naturals = ls_1_ate_N(n)
  inversos = mapeia(inverso_multiplicativo, naturals)
  return reduce(soma, inversos, 0)

# (*) Questão 14
# 
# Preencha a lacuna abaixo para obter seu próprio procedimento
# len(ls), isto é, seu próprio procedimento que sabe calcular o
# tamanho de uma lista.

def constant_1(x):
  return 1

def my_len(ls):
  return reduce(soma, mapeia(constant_1, ls), 0)