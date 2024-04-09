#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

import getpass

usuario = input('Digite o seu seu usuário: ')
senha = input('Digite sua senha: ')

while usuario == senha:
    usuario = input('A senha não pode ser igual ao nome do usuário! Tente novamente.')
    senha = input('A senha não pode ser igual ao nome do usuário! Tente novamente.')

print('Usuário e senhas cadastrados. ')