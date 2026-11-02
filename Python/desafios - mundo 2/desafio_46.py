'''
Faça um programa que mostre na tela uma "contagem regressiva" para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles. mostrando a mensagem "Feliz Ano Novo!" e emoji de fogos de artifício no final.
'''
from time import sleep
import emoji

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize("Feliz Ano Novo!:fireworks:"))