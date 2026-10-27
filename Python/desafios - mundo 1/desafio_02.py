'''
Crie um script python que leia o dia, o mês e o ano de nascimento de uma
pessoa e mostre uma mensagem com a data formatada.

Ex: -> Dia: 17
    -> Mês: Mar
    -> Ano: 1978
    <- Você nasceu no dia 17 de Mar de 1978. Correto?
'''
dia = int(input('Dia: '))
mes = str(input('Mês: '))
ano = int(input('Ano: '))
print('Você nasceu no dia {} de {} de {}. Correto?'.format(dia, mes, ano))