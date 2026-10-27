'''
Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
'''
temperature_celsius = float(input("Digite a temperatura em °C: "))
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
print(f"A temperatura em °F é: {temperature_fahrenheit}")