#Elabora um algorítimo que leia o nome e o peso de duas pessoas e imprima o nome da mais pesada

pessoa1 = input('Digite seu nome: ')
peso1 = float(input('Digite seu peso: '))
pessoa2= input('Digite seu nome: ')
peso2 = float(input('Digite seu peso: '))

if peso1>peso2:
    print(f"A pessoa mais pesada é {pessoa1}")
else:
    print(f"A pessoa mais pesada é {pessoa2}")