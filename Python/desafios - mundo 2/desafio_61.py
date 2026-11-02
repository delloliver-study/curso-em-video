'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

Desenvolva um programa que leia o Primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.
'''
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print(termo, end=' ')
    termo += razao
    contador += 1
print('FIM')