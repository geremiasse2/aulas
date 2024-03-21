#Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
troca = n1
n1 = n2
n2 = troca

print(n1, n2)