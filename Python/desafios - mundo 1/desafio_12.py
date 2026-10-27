'''
Faça um programa que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.
'''
preco_atual = float(input('Digite o preço do produto: R$ '))
new_preco = preco_atual - (preco_atual * 0.05)
print('O produto custa R$ {}, porém está com desconto de 5%, e está custando R$ {}.'.format(preco_atual, new_preco))