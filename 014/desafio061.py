# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura WHILE.

a = int(input('Qual o valor do primeiro termo? '))
r = int(input('Qual a razão? '))
c = 1

while c <= 10:
	v = a + (c - 1) * r
	print('{:2}° termo == {}' .format(c, v))
	c += 1


	