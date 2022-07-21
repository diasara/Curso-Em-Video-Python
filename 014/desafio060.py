# Faça um programa que leia um número qualquer e mostre seu fatorial.

n = int(input('Digite um número para saber o seu fatorial: '))

fatorial = 1

while not n == 1:
	fatorial *= n
	n -= 1

print('O fatorial é {}.' .format(fatorial))
