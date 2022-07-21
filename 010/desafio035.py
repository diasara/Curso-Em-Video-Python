# Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

if a > abs(b - c) and a < abs(b + c) or b > abs(a - c) and b < abs(a + c) or c > abs(a - b) and c < abs(a + b):
	print('As retas formam um triângulo.')
else:
	print('As retas NÃO formam um triângulo.')
