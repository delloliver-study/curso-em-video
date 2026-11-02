'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
num = 0
while True:
    num = int(input('Digite um número para ver a tabuada (ou um número negativo para sair): '))
    if num < 0:
        break
    print(f'Tabuada do {num}:')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')