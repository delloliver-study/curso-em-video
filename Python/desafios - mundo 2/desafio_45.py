'''
Crie um programa que faça o computador jogar "Jokenpô" com você
'''
from random import choice
from time import sleep

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(opcoes)
print('Opções: PEDRA, PAPEL, TESOURA')
jogador = input('Sua escolha: ').upper()

print('Computador escolheu: {}'.format(computador))
print('Jogador escolheu: {}'.format(jogador))

sleep(1)

if jogador == computador:
    print('Empate!')
elif (jogador == 'PEDRA' and computador == 'TESOURA') or \
     (jogador == 'PAPEL' and computador == 'PEDRA') or \
     (jogador == 'TESOURA' and computador == 'PAPEL'):
    print('Jogador vence!')
else:
    print('Computador vence!')
