'''
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

Desenvolva um programa que leia o Primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.
'''
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    contador += 1
print('PAUSA')
mais = int(input('Quantos termos você quer mostrar a mais? '))
while mais != 0:
    contador = 1
    while contador <= mais:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(termo))