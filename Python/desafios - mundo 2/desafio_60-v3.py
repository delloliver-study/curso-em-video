'''
Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
utilize o módulo math e a função factorial() para realizar o cálculo do fatorial.
'''
from math import factorial
numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = factorial(numero)
print('O fatorial de {} é {}.'.format(numero, fatorial))