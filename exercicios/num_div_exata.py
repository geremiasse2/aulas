n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if (n1 / n2) % 2 == 0:
    print(f'A divisão do número {n1} por {n2} é exata.')
else:
    print(f'A divisão não é exata')
