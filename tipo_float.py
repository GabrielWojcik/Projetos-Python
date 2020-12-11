"""
Tipo Float
Tipo real, decimal
Casas decimais
OBS: O separador de casas decimais é o ponto e não a vrigula
"""
valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(valor2)

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
