'''
Crie um script python que leia 2 numeros e tente mostrar o resultado.

Ex: -> Primeiro numero "6"
    -> Segundo número "3"
    <- A soma é 9
'''
valor_a = int(input('Primeiro Valor = '))
valor_b = int(input('Segundo Valor = '))
soma = valor_a + valor_b
print('A soma é {}'.format(soma))
print('A soma entre {} e {} é {}'.format(valor_a, valor_b, soma))