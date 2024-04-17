numeros = []
for numero in range(3):
    numero = int(input(f'Digite o {numero + 1}º número: '))
    numeros.append(numero)

while numeros != sorted(numeros):
    print('Os números não estão em ordem crescente, tente novamente. ')
    numeros = []
    for numero in range(3):
        numero = int(input(f'Digite o {numero + 1}º número: '))
        numeros.append(numero)

quarto_numero = int(input('Digite o quarto número: '))
numeros.append(quarto_numero)
numeros.sort(reverse=True)

print('Números em ordem descrescente: ', numeros)
