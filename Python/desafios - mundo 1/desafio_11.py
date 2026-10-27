'''
Faça um programa que leia a altura e a largura de uma parede
em metros, calcule sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta, pinta uma área
de 2m².
'''
base = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = base * altura
rendimento = 2
litros_necessarios = area / rendimento

print('Para pintar a parede com {} m²:'.format(area))
print('-> Você precisará de {:.2f} litros de tinta'.format(litros_necessarios))