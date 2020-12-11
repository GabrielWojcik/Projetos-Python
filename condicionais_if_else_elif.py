"""
Estruturas condicionais
if(Se), else(Se não), elif(Else if)
"""
idade = 26

if idade < 18:  # Um bloco só começa depois dos dois pontos ":";
    print('Menor de idade')  # Sempre com identação 4 espaços;
elif idade == 18:
    print('Tem 18 anos')     # Pode-se ter vários elif/if/else;
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')
