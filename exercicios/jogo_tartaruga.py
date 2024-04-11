from turtle import Turtle, Screen
import random
import turtle

screen = Screen()

screen.setup(400, 300)
aposta_usuario = screen.textinput("Faça sua aposta", "Qual tartaruga vai ganhar? ")
nomes = ["Leonardo", "João", "Pedro", "Afonso", "Lidia", "Pamela"]
cores = ["red", "blue", "green", "orange", "pink", "yellow"]
tartarugas = dict()
vencedora = ""

#Definição da posição de largada
posicao_largada = (-170, 150)
espacamento = 40

#Loop para criar cada tartaruga
for nome, cor in zip(nomes, cores):
    tartarugas[nome] = turtle.Turtle()
    tartarugas[nome].shape("turtle")
    tartarugas[nome].color(cor)

#Movimento para a posição de largada
    pos_x = posicao_largada[0]
    pos_y = posicao_largada[1] - (espacamento * len(tartarugas)) 
    tartarugas[nome].setpos(pos_x, pos_y)

random.randint(1, 6)

while not vencedora:
    # Nomes é uma lista com todos os nomes das tartarugas
    for nome in nomes:
        # Obtendo a distância
        distancia = random.randint(1, 6)
        # Fazendo a tartaruga andar a distância
        tartarugas[nome].forward(distancia)

        if tartarugas[nome].pos()[0] > 160:
            vencedora = nome
            break

print(f"A tartaruga vencedora foi {vencedora}! ")

#Definição da posição da tartaruga vencedora
tartarugas[vencedora].setpos(0, 0)

#Animação de comemoração da tartaruga vencedora
while True:
    tartarugas[vencedora].right(150)

screen.exitonclick()


