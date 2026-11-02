'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a "base de convesrão":

- 1 p/ "binário"
- 2 p/ "octal"
- 3 p/ "hexadecimal"
'''
num = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')