'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''
mais_de_18 = 0
homens = 0
mulheres_menos_20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa (M/F): ').strip().upper()
    
    if idade > 18:
        mais_de_18 += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    
    continuar = input('Deseja continuar? (S/N): ').strip().upper()
    if continuar != 'S':
        break

print(f'Quantidade de pessoas com mais de 18 anos: {mais_de_18}')
print(f'Quantidade de homens cadastrados: {homens}')
print(f'Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}')