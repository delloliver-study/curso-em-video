'''
Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
utilize o for para isso.
'''
numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1
for i in range(numero, 0, -1):
    fatorial *= i
print('O fatorial de {} é {}.'.format(numero, fatorial))