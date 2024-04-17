altura = float(input('Informe sua altura (m): '))
peso = float(input('Informe seu peso (kg) '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Magreza')
elif 18.5 <= imc < 25:
    print('Normal ')
elif 25 <= imc < 30:
    print('Sobrepeso ')
elif 30 <= imc < 40:
    print('Obesidade ')
elif imc > 40:
    print('Obesidade mórbida ')