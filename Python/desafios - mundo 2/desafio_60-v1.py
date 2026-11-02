'''
Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
utilize o while para isso.
'''
numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1
while numero > 1:
    fatorial *= numero
    numero -= 1
print('O fatorial de {} é {}.'.format(numero, fatorial))