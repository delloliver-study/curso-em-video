'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''
frase = input('Digite uma frase: ').strip().upper()
print('A letra "A" aparece {} vezes.'.format(frase.count("A")))
print('Primeira posição: {}'.format(frase.find("A") + 1))
print('Última posição: {}'.format(frase.rfind("A") + 1))