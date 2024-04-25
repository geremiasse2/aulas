tarefas = []


def criar_tarefa():
    tarefa = input('Qual tarefa deseja criar? ')
    tarefas.append({'nome': tarefa, 'completa': False})
    print('Tarefa criada com sucesso!')


def listar_tarefas():
    for index, tarefa in enumerate(tarefas):
        status = '✓' if tarefa['completa'] else ' '
        print(f'{index+1} - {tarefa["nome"]} - [{status}]')


def editar_tarefa(indice):
    tarefas[indice]['nome'] = input('Digite um novo nome: ')
    print('Tarefa alterada com sucesso!')


def completar_tarefa(indice):
    tarefas[indice]['completa'] = True


def deletar_tarefas_completas():
    for tarefa in tarefas:
        if tarefa['completa']:
            tarefas.remove(tarefa)


while True:
    escolha = input('''
    \nEscolha uma das opções: 
    1 - Criar nova tarefa
    2 - Listar tarefas
    3 - Editar tarefa
    4 - Completar tarefa
    5 - Remover tarefas completadas
    6 - Sair
    ''')

    match escolha:
        case '1':
            criar_tarefa()
        case '2':
            listar_tarefas()
        case '3':
            escolha = int(input('Qual tarefa deseja editar? '))
            editar_tarefa(escolha-1)
        case '4':
            escolha = int(input('Qual tarefa deseja completar?'))
            completar_tarefa(escolha-1)
        case '5':
            deletar_tarefas_completas()
        case '6':
            break
        case _:
            print('Opção inválida ')

