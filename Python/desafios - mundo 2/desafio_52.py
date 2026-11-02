'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input("Digite um número: "))
if num < 2:
    print(f"{num} não é um número primo.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")