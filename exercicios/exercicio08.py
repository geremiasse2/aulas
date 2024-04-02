##Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo

salario_hora = float(input('Quanto você ganha por hora trabalhada? '))
horas_trabalhadas = int(input('Quantas horas você trabalha no mês? '))
salario_bruto = salario_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
imposto_inss = salario_bruto * 0.08
imposto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - imposto_inss - imposto_sindicato

print(f'O salário bruto do profissional é: R${salario_bruto}')
print(f'Valor pago de INSS: R${imposto_inss}')
print(f'Valor pago ao sindicato: R${imposto_sindicato}')
print(f'O salário líquido é: R$ {salario_liquido}')
