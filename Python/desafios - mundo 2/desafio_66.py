'''
Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
num = 0
soma = 0
while True:
    num = int(input('Digite um número inteiro (999 para parar): '))
    if num == 999:
        break
    soma += num
print(f'Foram digitados {soma} números e a soma entre eles é {soma}.')