'''
Refaça o "DESAFIO 35" dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- "Equilátero": todos os lados iguais
- "Isósceles": dois lados iguais
- "Escaleno": todos os lados diferentes
'''
from time import sleep
print('Digite o comprimento dos três lados do triângulo: ')

lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os lados formam um triângulo.')
    if lado1 == lado2 == lado3:
        print('Tipo de triângulo: Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Tipo de triângulo: Isósceles')
    else:
        print('Tipo de triângulo: Escaleno')