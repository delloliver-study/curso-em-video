'''
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random


computer_number = random.randint(0, 5)
user_number = int(input('Tente adivinhar o número que o computador pensou (entre 0 e 5): '))
if user_number == computer_number:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! O número era {}.'.format(computer_number))