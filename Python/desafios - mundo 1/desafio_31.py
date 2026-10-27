'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de
até 200Km e R$0,45 para viagens mais longas.
'''
kilometros = float(input('Qual a distância da viagem em Km? '))
if kilometros <= 200:
    preco = kilometros * 0.50
else:
    preco = kilometros * 0.45
print('O preço da passagem é R$ {:.2f}.'.format(preco))