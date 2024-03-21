#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem 
# "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def saudacao_por_turno(turno):
    if turno.lower() == "m":
        return "Bom Dia!"
    elif turno.lower() == "v":
        return "Boa Tarde!"
    elif turno.lower() == "n":
        return "Boa Noite!"
    else:
        return "Valor Inválido!"

# Solicita ao usuário que informe o turno
turno_digitado = input("Em que turno você estuda? (M-matutino, V-vespertino, N-noturno): ")

# Chama a função para exibir a saudação conforme o turno
print(saudacao_por_turno(turno_digitado))

#pedir para explicar o DEF
