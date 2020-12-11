"""
Exibir dois numeros e mostrar qual é o maior.
"""

num1 = int(input('Digite o numero um: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    print('O numero um {}  é maior que o numero dois {}'.format(num1, num2))
if num2 > num1:
    print('O numero dois {} é maior que o numero um {}'.format(num2, num1))

