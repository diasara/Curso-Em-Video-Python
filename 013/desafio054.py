# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade 
# e quantas já são maiores.

from datetime import date

count = 0
for c in range(1,8):
	n = int(input('Digite o ano de nascimento da {}° pessoa: ' .format(c+1)))
	if date.today().year - n >= 18:
		count += 1

print(count)
