"""
Faça um programa que receba dois numeros e se forem iguais mostre a mensagem dizendo numeros iguais.
"""
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('O  primeiro numero é o maior {}'.format(num1))
if num2 > num1:
    print('O segundo numero é o maior {}'.format(num2))
elif num1 == num2:
    print('Os numeros são iguais {} , {}'.format(num1, num2))
