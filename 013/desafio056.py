# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - a média de idade do grupo;
# - qual é o nome do homem mais velho; 
# - e quantas mulheres têm menos de 20 anos.

soma = 0
count = 0

for c in range (1,5):	
	print('----- {}° pessoa -----')
	nome = str(input('Qual o seu nome? ')).strip().upper()
	idade = int(input('Qual a sua idade? ')).strip().upper()
	sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()
	
	if sexo == 'M':
		if c == 1:
			maior = idade
			nom_maior = nome
		else:
			if idade > maior:
				maior = idade
				nom_maior = nome
	

	if sexo == 'F':
		if idade < 20:
			count += 1
			
	soma += idade
	
media = soma / 4

print('''----- Resultado -----
A média de idade do grupo é {:.2f}.
O nome do homem mais velho é {}.
Existem {} mulheres com menos de 20 anos.''' .format(media, nom_maior, count))
	