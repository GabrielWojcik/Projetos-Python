"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java
for(int i = 0; i< limitador(10); i++){
    //execução do loop
}

Python

for item in interavel:
    // execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

Exemplos de iteráveis:
 - String
     nome = 'Geek University'
 - Lista
     lista = [1, 3, 5, 7, 9]
 - Range
    numeros = range(1, 10)
    # Exemplo de for 1 ( Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
"""
"""range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)
    
ENUMERATE

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)
    
for _, letra in enumerate(nome):  # _ descartar valor
    print(letra)
    
for valor in enumerate(nome):
    print(valor)
    
 nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

qtd = int(input('Quantas vezes esse deve rodas? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informa o {n} /{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = ' Geek University'
for letra in nome:
    print(letra, end=' ')  # Para não pular linha
    
Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

"""
"""
"""
# Original: U+1F335
# Modificado: U0001F335
emoji = 'U0001F60D'

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F335' * num)



