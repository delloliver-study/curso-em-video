'''
Elabore um programa que calcule o valor a ser pago por um produto , considerando o seu "preço normal" e "condição de pagamento":

- à vista *dinheiro/pix*: "10%" de desconto
- à vista *cartão*: "5%" de desconto
- em até *2x no cartão*: preço normal (s/ juros)
- *3x ou mais* no cartão: "20%" de juros
'''
preco_normal = float(input('Digite o preço normal do produto: R$ '))
print('Escolha a condição de pagamento: ')
print('1 - à vista (dinheiro/pix): 10% de desconto')
print('2 - à vista (cartão): 5% de desconto')
print('3 - em até 2x no cartão: preço normal (s/ juros)')
print('4 - 3x ou mais no cartão: 20% de juros')
input_condicao = int(input('Digite o número da condição de pagamento: '))
if input_condicao == 1:
    preco_final = preco_normal * 0.9
    print('Preço final: R$ {:.2f}'.format(preco_final))
elif input_condicao == 2:
    preco_final = preco_normal * 0.95
    print('Preço final: R$ {:.2f}'.format(preco_final))
elif input_condicao == 3:
    preco_final = preco_normal
    print('Preço final: R$ {:.2f}'.format(preco_final))
elif input_condicao == 4:
    preco_final = preco_normal * 1.2
    print('Preço final: R$ {:.2f}'.format(preco_final))
else:
    print('Condição de pagamento inválida.')