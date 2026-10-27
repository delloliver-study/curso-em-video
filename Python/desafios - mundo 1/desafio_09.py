'''
Faça um programa que leia um número inteiro qualquer e mostre
na tela a sua tabuada.
'''
n = int(input('Digite um número: '))
for i in range(1, 11):
    resultado = n * i
    print('{} x {} = {}'.format(n, i, resultado))