# Escreva um programa que leia um número n inteiro qualquer e mostre na tela 
# os n primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Digite o número de termos da Sequência de Fibonacci que você quer ver: '))
ant = 0; atual = 1; c = 0

while c < n:
	if c == 0:
		print('0', end = ' -> ')
	if c == 1:
		print('1', end = ' -> ')
	if c != 0 and 1:
		prox = ant + atual
		print(prox, end = ' -> ')
		ant = atual
		atual = prox
	c += 1
