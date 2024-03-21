salario = float(input("Digite o salário do colaborador: "))

if salario <= 280.00:
    salario1 = salario * 0,2
elif salario < 280.00 and salario <= 700.00:
    salario2 = salario * 0.15
elif salario < 700.00 and salario <= 1500.00:
    salario3 = salario * 0.1
elif salario > 1500:
    salario4 = salario * 0.05

print("O salário antes do reajuste é {}".format(salario))
print("O salário depois do reajuste é {}".format(salario1))
