"""
Estrutura Lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
  - not;
Operadores binários:
 - and, or, is;

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True;
Para o 'or', um ou outro valor precisa ser True;
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True;
Para o 'is', o valor é comparado com um segundo;
"""
ativo = True
logado = False


if ativo:
    print('Bem-vindo')

else:
    print('Ative a sua conta')

# Ativo é Falso?
print(ativo is True)

