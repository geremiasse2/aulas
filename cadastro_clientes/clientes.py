clientes = []


def cadastro_clientes():
    clientes.append({'nome': input('Informe o nome do cliente: '), 'telefone': input('Informe o telefone do cliente: '),
                     'email': input('Informe o email do cliente: '), 'disponivel': False})
    print('Cadastro realizado com sucesso!')


def listar_clientes():
    for index, cliente in enumerate(clientes):
        #status = '✓' if cadastro['disponivel'] else ' ' (ver por que tá dando erro)
        print(
            f'{index + 1} - {cliente["nome"]} - {cliente["telefone"]} - {cliente["email"]} ')  #pedir para explicar essa linha


def editar_cliente(indice):
    clientes[indice]['nome'] = input('Informe o novo nome do cliente: ')
    clientes[indice]['telefone'] = input('Informe o novo telefone do cliente: ')
    clientes[indice]['email'] = input('Informe o novo email do cliente: ')
    print('Cadastro alterado com sucesso!')


def disponivel(indice):
    clientes[indice][disponivel] = True


def excluir_cliente():
    for cliente in clientes:
        print(int(input('Qual cliente deseja excluir?')))
        clientes.remove(cliente)
#print('Cliente removido com sucesso ')


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
            cadastro = (input('Qual cliente deseja marcar como disponível?'))
            listar_clientes(cadastro - 1)
        case '6':
            excluir_cliente()
        case '7':
            break
        case _:
            print('Opção inválida! ')
