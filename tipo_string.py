"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre áspas simples -> 'uma string', '123', 'a';
- Estiver entre áspas duplas -> "uma string", "124", "a";
- Estiver entres áspas simples triplas -> '''uma string'''
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = 'Angelina Jolie'
print(type(nome))
print(nome.upper())
print(nome.split()) Tranforma em uma lista de strings
print(nome[0:4])  # Slice de string

print(nome[5:15])
# [ 0,        1]
# ['Geek', 'University']
print(nome.split()[0])


"""
# - Estiver entre aspas duplas triplas -> """uma string""";
# [ 0,  1,  2,  3, 4, 5,  6,  7,  8,  9,  10,  11, 12, 13, 14]
# ['G','e','e','k','', 'U','n','i','v','e','r','s','i','t','y']
nome = 'Geek University'
"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta.
"""
print(nome[::-1])  # Inversão da String;

print(nome.replace('G', 'P'))
print(type(nome))

texto = 'socorram me subino onibus em marrocos'  # Palíndromo
print(texto)
print(texto[::-1])
