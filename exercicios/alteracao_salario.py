salario = float(input('Qual o salario atual?\n'))
aumento = 15/100
salarioNovo = salario * (1 + aumento)

print('Com um aumento de {:.0%} o novo salário será de R$ {:.2f}'.format(aumento, salarioNovo))