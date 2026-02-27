largura = float(input('Qual a largura da parede?\n'))
altura = float(input('Qual a altura da parede?\n'))

area = largura*altura
rendimento = 2
consumo = area / rendimento

print('Cada litro de tinta pinta {} m², então para essa parede com área de {} você vai precisar de {} litros de tinta'.format(rendimento, area, consumo))