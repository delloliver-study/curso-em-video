'''
Crie um algortmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada.
'''
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz_quadrada = n ** 0.5
print('O dobro de {} é {}'.format(n, dobro))
print('O triplo de {} é {}'.format(n, triplo))
print('A raiz quadrada de {} é {:.2f}'.format(n, raiz_quadrada))
