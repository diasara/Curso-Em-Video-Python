# Fa�a um programa que leia um n�mero qualquer e mostre seu fatorial.

n = int(input('Digite um n�mero para saber o seu fatorial: '))

fatorial = 1

while not n == 1:
	fatorial *= n
	n -= 1

print('O fatorial � {}.' .format(fatorial))
