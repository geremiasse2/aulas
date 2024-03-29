import string
import random
import os

quantidade_letra = int(input("Qual a quantidade de letras? "))
quantidade_numeros = int(input("Qual a quantidade de números? "))
quantidade_caracteres_especiais = int(input("Qual a quantidade de caracteres? "))

def gera_senha(qtde_letra, qtde_num, qtde_carac):
    letras = string.ascii_letters
    numeros = string.digits
    caracteres = string.punctuation
    letras_escolhidas = []
    numeros_escolhidos = []
    caracteres_escolhidos = []

    for _ in range(qtde_letra):
        escolha = random.choice(letras)
        letras_escolhidas.append(escolha)
  
    for _ in range(qtde_num):
        escolha = random.choice(numeros)
        numeros_escolhidos.append(escolha)

    for _ in range(qtde_carac):
        escolha = random.choice(caracteres)
        caracteres_escolhidos.append(escolha)   

    combinacao = letras_escolhidas + numeros_escolhidos + caracteres_escolhidos
    random.shuffle(combinacao)
    return combinacao
    
senha = gera_senha(quantidade_letra, quantidade_numeros, quantidade_caracteres_especiais)
senha_final = "".join(senha)
os.system("cls")
print(f"A senha gerada foi: {senha_final} ")
