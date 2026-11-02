'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Considere a maioridade como 21 anos.
'''
from datetime import date

ano_atual = date.today().year
pessoas_maioridade = 0
pessoas_nao_maioridade = 0

for c in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        pessoas_maioridade += 1
    else:
        pessoas_nao_maioridade += 1

print(f"Quantidade de pessoas que atingiram a maioridade: {pessoas_maioridade}")
print(f"Quantidade de pessoas que ainda não atingiram a maioridade: {pessoas_nao_maioridade}")