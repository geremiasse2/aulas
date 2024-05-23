clientes = [
    {'nome': 'geremias', 'telefone': '48999676802','email': 'geremiasse', 'disponivel': True},
    {'nome': 'b', 'telefone': 'b','email': 'b', 'disponivel': True},
    {'nome': 'c', 'telefone': 'c','email': 'c', 'disponivel': False},
]


def cadastro_clientes():
    clientes.append({'nome': input('Informe o nome do cliente: '), 'telefone': input('Informe o telefone do cliente: '),
                     'email': input('Informe o email do cliente: '), 'disponivel': True})
    print('Cadastro realizado com sucesso!')


def listar_clientes():
    for index, cliente in enumerate(clientes):
        status = '✓' if cliente['disponivel'] else ' '
        print(f'{index + 1} - {cliente["nome"]} - {cliente["telefone"]} - {cliente["email"]} - [{status}]')


def editar_cliente(indice):
    while True:
        cadastro = input('''
        O que deseja alterar?
        1 - Nome:
        2 - Telefone
        3 - Email
        4 - Sair
        ''')

        match cadastro:
            case '1':
                clientes[indice]['nome'] = input('Informe o novo nome do cliente: ')
            case '2':
                clientes[indice]['telefone'] = input('Informe o novo telefone do cliente: ')
            case '3':
                clientes[indice]['email'] = input('Informe o novo email do cliente: ')
            case '4':
                break
    print('Cadastro alterado com sucesso!')


def alternar(indice):
    print(f'O status era {clientes[indice]["disponivel"]}')
    clientes[indice]['disponivel'] = not clientes[indice]['disponivel']
    print(f'O status passou a ser {clientes[indice]["disponivel"]}')


def excluir_cliente():
    excluir = int(input('Qual cliente deseja excluir?')) - 1
    clientes.pop(excluir)
    print('Cliente removido com sucesso ')


while True:
    cadastro = input('''
    Escolha uma das opções:
    1 - Cadastrar novo cliente
    2 - Visualizar lista de clientes
    3 - Editar cliente
    4 - Marcar/desmarcar cliente como disponível
    5 - Ver clientes ativos
    6 - Excluir cliente
    7 - Sair
    ''')

    match cadastro:
        case '1':
            cadastro_clientes()
        case '2':
            listar_clientes()
        case '3':
            cadastro = int(input('Qual cliente deseja editar? '))
            editar_cliente(cadastro - 1)
        case '4':
            cadastro = int(input('Qual cliente deseja marcar como disponível?'))
            alternar(cadastro - 1)
        case '6':
            excluir_cliente()
        case '7':
            break
        case _:
            print('Opção inválida! ')
