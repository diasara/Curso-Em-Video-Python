# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor em metros: '))

print('{} metros = {:.0f} centímetros = {:.0f} milímetros' .format(n, n * 100, n * 1000))
