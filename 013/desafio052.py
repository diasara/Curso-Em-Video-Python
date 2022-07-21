# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

count = 0

n = int(input('Digite um número para saber se ele é primo: '))

for c in range(1, n + 1):
	if n % 2 == 0:
		count += 1

if count == 2:
	print('O número é PRIMO!')
else:
	print('O número NÃO É PRIMO!')
	