# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância (em quilômetros) da viagem? '))

if distancia <= 200:
	passagem = 0.5 * distancia
else:
	passagem = 0.45 * distancia

print('O preço da passagem é R${:.2f}.' .format(passagem))
