'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
'''
total_gasto = 0
produtos_mais_de_1000 = 0
nome_produto_mais_barato = ""
preco_produto_mais_barato = float('inf')
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$ '))
    
    total_gasto += preco
    
    if preco > 1000:
        produtos_mais_de_1000 += 1
    
    if preco < preco_produto_mais_barato:
        preco_produto_mais_barato = preco
        nome_produto_mais_barato = nome
    
    continuar = input('Deseja continuar? (S/N): ').strip().upper()
    if continuar != 'S':
        break

print(f'Total gasto na compra: R$ {total_gasto:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000: {produtos_mais_de_1000}')
print(f'Nome do produto mais barato: {nome_produto_mais_barato}')