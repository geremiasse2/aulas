#Ler um número e dizer se é divisível por 10, 5 e 2 ao mesmo tempo, ou não.

n1 = int(input('Digite um número: '))

if (n1 / 10) % 2 == 0 and (n1 / 5) % 2 == 0 and (n1 / 2) % 2 == 0:
    print(f'O número informado é divisível por 10, 5 e 2.')
else:
    print(f'O número não é divisível por 10, 5 e 2 ao mesmo tempo. ')
