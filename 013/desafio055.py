#  Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = 0

for c in range(1,6):
	peso = float(input('Digite o peso da {}° pessoa: ' .format(c)))
	if peso > maior:
		maior = peso
	else:
		if menor == 0: 
		    menor = peso
		elif peso < menor:
		    menor = peso
		
print('''menor peso = {:.2f}kg.
maior peso = {:.2f}kg''' .format(menor, maior))
