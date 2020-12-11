"""
Mostrar a raiz quadrada do número se ele for positivo.
"""
import math
num = float(input('Digite um número: '))
if num > 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz}')
if num < 0:
    print('Numero invalido')
