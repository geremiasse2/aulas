from turtle import Turtle, Screen

screen = Screen()

screen.setup(400, 300)
aposta_usuario = screen.textinput("Faça sua aposta", "Qual tartaruga vai ganhar? ")
leonardo = Turtle()
leonardo.shape("turtle")
leonardo.color("red")

joao = Turtle()
joao.shape("turtle")
joao.color("blue")

pedro = Turtle()
pedro.shape("turtle")
pedro.color("green")

afonso = Turtle()
afonso.shape("turtle")
afonso.color("orange")
afonso.goto(-170, -100)

lidia = Turtle()
lidia.shape("turtle")
lidia.color("pink")

pamela = Turtle()
pamela.shape("turtle")
pamela.color("yellow")

joao.backward(100)

leonardo.forward(160)

screen.exitonclick()


