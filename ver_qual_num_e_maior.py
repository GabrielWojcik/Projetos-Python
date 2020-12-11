"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O número {} é o maior!'.format(num1))
if num2 > num1:
    print('O número {} é o maior!'.format(num2))
