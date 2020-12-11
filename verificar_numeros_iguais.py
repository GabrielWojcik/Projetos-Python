"""
Inserir dois numeros e mostrar uma mensagem caso os dois numeros forem iguais.
"""
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
print('O número um é {}'.format(num1))
print('O número dois é {}'.format(num2))
if num1 == num2:
    print('O número um, {} é igual ao número dois, {}'.format(num1,num2))
