"""
Programa que mostra o valor da prestação de um emprestimo e quanto corresponde 20% do salario do trabalhador
se for maior que 20% o emprestimo deve ser negado.
"""
salario = int(input('Digite o seu salário R$: '))
emprestimo = int(input('Digite o valor do empréstimo desejado R$: '))
print(' ATENÇÃO!! Seu empréstimo não pode ultrapassar 20% do seu salário')
calc = salario / 5
calc1 = emprestimo / 5
print('Seu salário é de R$ {} e o seu emprestimo desejado é de R${}'.format(salario, emprestimo))
print('Com descontos de 20% seu emprestimo será de {} '.format(calc))
print('Com descontos de 20% seu emprestimo será de {} '.format(calc1))

