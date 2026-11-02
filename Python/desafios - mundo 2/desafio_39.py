'''
Faça um programa que leia o ano de nascimento de jovem e informe, de acordo com sua idade:

- Se ele "ainda vai se alistar" ao serviço militar.
- Se é a "hora de se alistar".
- Se já "passou do tempo" do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nascimento

if idade < 18:
    print('Ainda vai se alistar! Faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('É a hora de se alistar!')
else:
    print('Já passou do tempo! Passaram {} anos.'.format(idade - 18))