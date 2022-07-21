# Crie um programa que leia dois valores e mostre um menu na tela:
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

c = 0

while c != 5:
	print('O que você quer fazer com eles?')
	c = int(input('[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa\n'))
	if c == 1:
		print('A soma é {}.' .format(n1 + n2))
	if c == 2:
		print('O produto é {}.' .format(n1 * n2))
	if c == 3:
		if n1 > n2:
			maior = n1
		else:
			maior = n2
		print('O maior número é {}.' .format(maior))
	if c == 4:
		n1 = int(input('Digite o primeiro valor: '))
		n2 = int(input('Digite o segundo valor: '))
