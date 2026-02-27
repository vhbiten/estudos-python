# modulos/ bibliotecas em python

#importa tudo.
import math

#importa um metodo especifico
from math import sqrt

num = int(input('Digite um número para descobrir a raiz quadrada dele:\n'))
raiz = math.sqrt(num)
print('A raiz quadrade de {} é igual a {}'.format(num, raiz))