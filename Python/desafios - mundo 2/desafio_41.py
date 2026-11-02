'''
A Confederação Brasileira de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo coma idade:

- Até "9 anos": *MIRIM*
- Até "14 anos": *INFANTIL*
- Até "19 anos": *JUNIOR*
- Até "20 anos": *SÊNIOR*
- Acima: *MASTER*
'''
from datetime import date
nome = input('Digite o nome do atleta: ')
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print('Atleta: {}'.format(nome))
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Atleta: {}'.format(nome))
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Atleta: {}'.format(nome))
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Atleta: {}'.format(nome))
    print('Categoria: SÊNIOR')
else:
    print('Atleta: {}'.format(nome))
    print('Categoria: MASTER')