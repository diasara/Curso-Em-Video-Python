# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Segunda reta: '))
c = int(input('Terceira reta: '))

if a > abs(b - c) and a < abs(b + c) or b > abs(a - c) and b < abs(a + c) or c > abs(a - b) and c < abs(a + b):
	print('As retas formam um triângulo.')
	
	if a == b == c:
		print('É um triângulo EQUILÁTERO!')
	elif a == b or a == c or b == c:
		print('É um triângulo ISÓSCELES!')
	else:
		print('É um triângulo ESCALENO!')
else:
	print('As retas NÃO formam um triângulo.')
