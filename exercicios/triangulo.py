a = float(input('Informe o tamanho do primeiro lado do triângulo: '))
b = float(input('Informe o tamanho do segundo lado do triângulo: '))
c = float(input('Informe o tamanho do terceiro lado do triângulo: '))
if a == b == c:
    print('O triângulo é equilátero. ')
elif a == b or a == c or b == c:
    print('O triangulo é um isósceles ')
elif a != b != c:
    print('O triangulo é um escaleno ')