preco = float(input('Qual o preço do produto?\n'))
desconto = 5/100
precoDescontado = preco * (1 - desconto)
print('O preço com desconto de {:.0%} é R${:.2f}'.format(desconto, precoDescontado))