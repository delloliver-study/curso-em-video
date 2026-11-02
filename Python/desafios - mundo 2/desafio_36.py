'''
Escreva um programa para aprovar um empréstimo bancário de uma casa. O programa vai perguntar o "valor da casa", o "salário" do comprador e em "quantos anos" ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ele não pode exceder "30%" do salário ou então o empréstimo será negado.
'''
salario = float(input('Digite o valor do seu salário: R$ '))
valor_casa = float(input('Digite o valor da casa: R$ '))
anos = int(input('Em quantos anos você pretende pagar? '))
prestacao = valor_casa / (anos * 12)
if prestacao > (salario * 0.3):
    print('Empréstimo negado! A prestação de R$ {:.2f} excede 30% do seu salário.'.format(prestacao))
else:
    print('Empréstimo aprovado! A prestação de R$ {:.2f} não excede 30% do seu salário.'.format(prestacao))