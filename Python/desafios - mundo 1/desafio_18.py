'''
Faça um programa que leia o angulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse angulo.
'''
angulo = float(input("Digite o ângulo que você deseja: "))
import math
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo}° tem:")
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")