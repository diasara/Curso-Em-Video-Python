# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

a = int(input('Qual o valor do primeiro termo? '))
r = int(input('Qual a razão? '))
c = 1

while c <= 10:
	v = a + (c - 1) * r
	print('{:2}° termo == {}' .format(c, v))
	c += 1

d = 1
while d != 0:
	d = int(input('Você quer mais quantos termos? '))
	
	if d != 0:
		d = c + d
		while c < d:
			v = a + (c - 1) * r
			print('{:2}° termo == {}' .format(c, v))
			c += 1
