"""
Escopo de variáveis

Dois casos de escopo:
1 - Variaveis globais;
        - São reconhecidas, ou seja, seu escopo compreende, todo o programa.
2 - Variaveis locais;
        - São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
        está limitado ao bloco onde foi declarada.

Para declarar variaveis em Python fazemos:
nome_da_variavel = valor_da_variavel
Python é uma linguagem de tipagem dinâmica. Isso significa que
ao delcararmos uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor á mesma.

"""
numero = 42
print(numero)

numero = 2
if numero > 10:
    novo = numero + 10 # A variavel novo esta delacarada localmente dentro do bloco if. Portanto é local;
    print(novo)



