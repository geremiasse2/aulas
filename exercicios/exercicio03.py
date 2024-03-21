#Faça um Programa que leia três números inteiros e mostre o maior deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
#maior_num = max(n1, n2, n3)
valores = [n1, n2, n3]
auxiliar = -99999
for numero in valores:
    if numero > auxiliar:
        auxiliar = numero
print(auxiliar)

#print(f"O maior número digitado é {maior_num}")