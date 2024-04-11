numeros = []
numero1 = int(input("Digite um número: "))
numeros.append(numero1)

numero2 = int(input("Digite outro número: "))
if numero2 > numero1:
    numeros.append(numero2)
else:
    print("O número não pode ser menor que o anterior")    

numero3 = int(input("Digite outro número: "))
if numero3 > numero2:
    numeros.append(numero3)
else:
    print("O número não pode ser menor que o anterior")    

numero4 = int(input("Digite outro número: "))
numeros.append(numero4)

numeros.sort()
print(numeros)


