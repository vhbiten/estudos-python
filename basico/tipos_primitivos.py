# tipos primitivos em python (int, float, boolean)

num1 = int(input('Qual o primeiro número?'))
num2 = float(input('Qual o segundo número?'))
s = num1 + num2
print('A soma de {} + {} é igual a {}'.format(num1, num2, s))
print('A soma vale {}'.format(num1+num2))

entrada = (input('Digite algo e descubra qual o seu tipo: '))
print(type(entrada))