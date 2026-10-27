'''
Crie um programa que leia quanto dinheiro uma pessoas tem
na carteira e mostre quantos Dólares ela pode comprar.

Considere
US$ 1,00 = R$ 3,27
'''
wallet = float(input('Quanto você tem na carteira? R$ '))
dollar = wallet / 3.27

print('Com esse valor R$ {}, você consegue comprar US$ {:.2f}.'.format(wallet, dollar))