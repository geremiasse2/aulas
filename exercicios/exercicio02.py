# Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota "))
resultado = float(nota1 + nota2) / 2
if resultado == 10:
    print("Aprovado com distinção")
elif resultado >= 7:
    print("Aprovado")
else:
    print("Reprovado")
