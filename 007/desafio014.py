# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = celsius * 1.8 + 32

print('{:.2f} Celsius = {:.2f} Fahrenheit' .format(celsius, fahrenheit))