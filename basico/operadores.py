# operadores de calculos em python

n1 = float(input('entre com um número: '))
n2 = float(input('Entre com outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
sobra = n1 % n2

print('A soma é {}.\n A multiplicação é {}.\n A divisão é {:.3f}.\n A divisão por inteiro é {}.\n A potência é {}.\n A sobra é {}.'.format(s, m, d, di, e, sobra))