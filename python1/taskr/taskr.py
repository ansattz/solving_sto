# Douglas Santos
# @ansattz


import readline
taskr = {}

def mostrar_disciplinas():
    if taskr:
        for disciplina in taskr:
            buscar_disciplina(disciplina)
    else:
        print('====> Não há disciplinas no banco de dados :(')
        print('')


def buscar_disciplina(disciplina):
    try:        
        print('Nome:', disciplina)
        print('Código:', taskr[disciplina]['codigo'])
        print('Professor:', taskr[disciplina]['professor'])
        print('Email:', taskr[disciplina]['email'])
        print('Sala de aula:', taskr[disciplina]['saladeaula'])
        print('Horário/Dia das aulas:', taskr[disciplina]['horariodia'])
        print('Avaliações:', taskr[disciplina]['avaliacoes'])
        print('Horário da avaliação:', taskr[disciplina]['horarioav'])
        print('========================================================')
    except KeyError:
        print('====> Disciplina não cadastrada D:')
        print('')
    except Exception as error:
        print('====> Erro')
        print('')
        print(error)


def ler_detalhes_disciplina():
    codigo = input('Código da disciplina: ')
    professor = input('Primeiro e o segundo nome do professor: ')
    email = input('O email do professor: ')
    saladeaula = input('A sala de aula: ')
    horariodia = input('Horário e dia das aulas: ')
    avaliacoes = input('Avaliações futuras da disciplina: ')
    horarioav = input('Horário das avaliações: ')
    return codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav


def incluir_editar_disciplina(disciplina, codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav):
    taskr[disciplina] = {
        'codigo': codigo,
        'professor': professor,
        'email': email,
        'saladeaula': saladeaula,
        'horariodia': horariodia,
        'avaliacoes': avaliacoes,
        'horarioav': horarioav,
    }
    salvar()
    print()
    print('====> Disciplina {} adicionada/editada com sucesso :)'.format(disciplina))
    print()


def excluir_disciplina(disciplina):
    try:
        taskr.pop(disciplina)
        salvar()
        print()
        print('====> Disciplina {} excluída com sucesso :)'.format(disciplina))
        print()
    except KeyError:
        print('====> Disciplina inexistente D:')
    except Exception as error:
        print('====> Error')
        print(error)


def exportar_disciplinas(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for disciplina in taskr:
                codigo = taskr[disciplina]['codigo']
                professor = taskr[disciplina]['professor']
                email = taskr[disciplina]['email']
                saladeaula = taskr[disciplina]['saladeaula']
                horariodia = taskr[disciplina]['horariodia']
                avaliacoes = taskr[disciplina]['avaliacoes']
                horarioav = taskr[disciplina]['horarioav']
                arquivo.write("{} | {} | {} | {} | {} | {} | {} | {}\n".format(disciplina , codigo , professor , email , saladeaula , horariodia , avaliacoes , horarioav))
        print('====> Disciplinas exportadas')
    except Exception as error:
        print('====> Ocorreu um erro ao exportar as disciplinas')
        print('')
        print(error)



def importar_disciplinas(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                codigo = detalhes[1]
                professor = detalhes[2]
                email = detalhes[3]
                saladeaula = detalhes[4]
                horariodia = detalhes[5]
                avaliacoes = detalhes[6]
                horarioav = detalhes[7]

                incluir_editar_disciplina(nome, codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav)
    except FileNotFoundError:
        print('====> Arquivo não encontrado')
    except Exception as error:
        print('====> Erro inesperado')
        print(error)

# Pré-definição da extensão e nome do arquivo de banco de dados
def salvar():
    exportar_disciplinas('databasedisc.csv')


def carregar():
    try:
        with open('databasedisc.csv', 'r') as arquivo:
            linhas = arquivo.redlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                codigo = detalhes[1]
                professor = detalhes[2]
                email = detalhes[3]
                saladeaula = detalhes[4]
                horariodia = detalhes[5]
                avaliacoes = detalhes[6]
                horarioav = detalhes[7]

                taskr[nome] = {
                        'codigo': codigo,
                        'professor': professor,
                        'email': email,
                        'saladeaula': saladeaula,
                        'horariodia': horariodia,
                        'avaliacoes': avaliacoes,
                        'horarioav': horarioav,
                    }
        print('====> Database carregado')
        print('====> {} disciplinas carregadas'.format(len(taskr)))
    except FileNotFoundError:
        print('====> Arquivo não encontrado')
    except Exception as error:
        print('====> Erro inesperado')
        print(error)


def imprimir_menu():
    print('==================================================')
    print('')
    print('1 - Mostrar todas as disciplinas')
    print('2 - Buscar disciplina')
    print('3 - Incluir disciplina')
    print('4 - Editar disciplina')
    print('5 - Excluir disciplina')
    print('6 - Exportar disciplina para CSV')
    print('7 - Importar disciplina CSV')
    print('0 - Fechar taskr')
    print('')
    print('===================================================')


# START
# As instruções de sequência e entrada para o menu do programa
carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_disciplinas()
    elif opcao == '2':
        disciplina = input('Digite o nome da disciplina: ')
        buscar_disciplina(disciplina)
    elif opcao == '3':
        disciplina = input('Digite o nome da disciplina: ')

        try:
            taskr[disciplina]
            print('====> Disciplina já cadastrada')
        except KeyError:
            codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav = ler_detalhes_disciplina()
            incluir_editar_disciplina(disciplina, codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav)
    elif opcao == '4':
        disciplina = input('Digite o nome da disciplina: ')

        try:
            taskr[disciplina]
            print('====> Editando disciplina: ', disciplina)
            codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav = ler_detalhes_disciplina()
            incluir_editar_disciplina(disciplina, codigo, professor, email, saladeaula, horariodia, avaliacoes, horarioav)
        except KeyError:
            print('====> Disciplina não cadastrada')

    elif opcao == '5':
        disciplina = input('Digite o nome da disciplina: ')
        excluir_disciplina(disciplina)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_disciplinas(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_disciplinas(nome_do_arquivo)
    elif opcao == '0':
        print('====> Fechando programa')
        break
    else:
        print('====> Opção inválida')
        print('')