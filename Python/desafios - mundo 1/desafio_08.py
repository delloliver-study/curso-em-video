"""
Escreva um programa que leia um valor em metros e o exiba
convertido em centimetros e milimetros.
"""

m = int(input("Digite um valor em metros: "))
cen = m * 100
mm = m * 1000

print(
    "A conversão da medida {} metros, em centímetro é {} centímetros, e em milimetros é {} milimetros.".format(m, cen, mm)
)
