'''
Faça um algoritimo que leia o salário de um funcionario
e mostre seu novo salário, com 15% de aumento.
'''
sal = float(input('Digite o salário do funcionário: R$ '))
aumento = sal + (sal * 0.15)

print('O salário atual do funcionário é de R$ {}'.format(sal))
print('Com um aumento adicional de 15%, o novo salário do funcionério é de R$ {}'.format(aumento))