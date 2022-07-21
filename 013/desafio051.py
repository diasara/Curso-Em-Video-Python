# Desenvolva um programa que leia o primeiro termo e a razão 
# de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a = int(input('Qual o valor do primeiro termo? '))
r = int(input('Qual a razão? '))

for c in range(1,11):
	v = a + (c - 1) * r
	print('{:2}° termo = {}' .format(c, v))
	