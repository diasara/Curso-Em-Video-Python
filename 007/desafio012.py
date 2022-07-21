# Faça um algoritmo que leia um preço e mostre um novo preço com 5% de desconto

p = float(input('Digite o preço do produto: '))

print('O novo preço do produto é de R${:.2f}.' .format(p - (p * 0.05)))
