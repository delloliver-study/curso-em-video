'''
Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
valores = []
while True:
    numero = int(input('Digite um número inteiro: '))
    valores.append(numero)
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('A média entre todos os valores é {:.2f}'.format(sum(valores) / len(valores)))
print('O maior valor lido foi {}'.format(max(valores)))
print('O menor valor lido foi {}'.format(min(valores)))