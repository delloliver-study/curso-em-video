'''
Crie um programa que leia o nome de uma cidade e diga se ela começa
com o nome "SANTO".
'''
cidade = input('Digite o nome de uma cidade: ').strip()
if cidade[:5].upper() == 'SANTO':
    print('A cidade começa com "SANTO".')
else:
    print('A cidade não começa com "SANTO".')