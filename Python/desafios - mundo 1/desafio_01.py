"""
Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem
de boas-vindas de acordo com o valor digitado.

Ex: -> Qual é o seu nome? "Gustavo"
    <- Olá Gustavo! Prazer em te conhecer!
"""
nome = str(input('Qual é o seu nome? '))
print('Olá {}! Prazer em te conhecer!'.format(nome))