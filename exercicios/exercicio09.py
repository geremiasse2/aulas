#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Informe a área que será pintada em metros quadrados: '))
consumo_litro = area / 3
consumo_lata = consumo_litro / 18
valor_tinta = consumo_lata * 80

print(f'Para pintar a área informada será necessário {consumo_lata:.2f} latas de tinta, que custará R${valor_tinta:.2f}')