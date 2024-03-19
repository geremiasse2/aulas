#Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
maior_num = max(n1, n2, n3)
menor_num = min(n1, n2, n3)
print(f"O maior número digitado é {maior_num} e o menor número é {menor_num}")