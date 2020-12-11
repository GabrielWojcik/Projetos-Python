# PEP 8 - Python Enhancement Proposal
# Propostas de melhorias para a linguagem Python
# The Zen of Python
# import this
# A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.
# [1] - Utilize Camel Case para nomes de classes; sempre inicial com letra MAISCULA.

class Calculadora:
    pass


class calculadora_cientifica:
    pass
# [2] - Utilize nomes em minúsculos separados por underline para funções ou variáveis.
def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

# [3] - Utilize 4 espaços para identação!NAO USE TAB!
if 'a' in 'banana':
    print('tem')

# [4] - Linhas em branco, 2 linhas em branco para definir uma classe!
# Métodos dentro de uma classe devem ser separados com uma única linha em branco;

# [5] - Importes devem ser sempre feitos em linhas separadas;
# import sys;
# import os;

# Não há problemas em utilizar:
# from types import StringType, ListType
# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
# from types import (
#        StingType,
#        listType,
#        SetType,
# )
# Imports devem ser colocados no topo do arquivo logo depois de quaisquer comentarios ou
# docsstrigs e antes de constantes e variaveis globais.
# [6] - Espaços em expressões e instruçoes
# Não faça:
# função (algo [ 1 ], {outro: 2 })
# Faça:
# função(algo[1], {outro: 2})

# [7] - Termine sempre uma instrução com uma nova linha
# import this
