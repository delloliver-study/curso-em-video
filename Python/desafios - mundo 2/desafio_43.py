'''
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu "IMC" e mostre seu status, de acordo coma tabela abaixo:

- Abaixo de "18.5": Abaixo do Peso
- Entre "18.5" e "25": Peso ideal
- "25" até "30": Sobrepeso
- "30" até "40": Obesidade
- Acima de "40": Obesidade mórbida
'''
peso = float(input('Digite o peso (kg): '))
altura = float(input('Digite a altura (m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('IMC: {:.2f} - Abaixo do Peso'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC: {:.2f} - Peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('IMC: {:.2f} - Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('IMC: {:.2f} - Obesidade'.format(imc))
else:
    print('IMC: {:.2f} - Obesidade mórbida'.format(imc))