"""
Leia e mostre o número ao quadrado e a raiz quadrada do número.
"""
import math
num = int(input('Digite um numero: '))
soma = num*num
print(' O quadrado do numero é {}'.format(soma))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {raiz}')
