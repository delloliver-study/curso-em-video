'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
'''
km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o carro foi alugado? '))
preco = dias * 60 + km * 0.15
print(f'O preço a pagar é: R$ {preco:.2f}')