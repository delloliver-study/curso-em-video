'''
Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
----
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
from time import sleep

numero_computador = random.randint(0, 10)
tentativas = 0

print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
sleep(1)

while True:
    numero_usuario = int(input('Em que número eu pensei? '))
    tentativas += 1

    if numero_usuario == numero_computador:
        print(f'Parabéns! Você acertou em {tentativas} tentativas.')
        break
    else:
        print('Tente novamente!')