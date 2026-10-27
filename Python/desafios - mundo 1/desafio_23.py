'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada
um dos dígitos separados.
faça como string e como número inteiro.
'''
n = int(input('Digite um número de 0 a 9999: '))
n_str = str(n).zfill(4)  # Preenche com zeros à esquerda
print('Unidade: {}'.format(n_str[3]))
print('Dezena: {}'.format(n_str[2]))
print('Centena: {}'.format(n_str[1]))
print('Milhar: {}'.format(n_str[0]))