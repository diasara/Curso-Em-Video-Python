# Condições Pt. 1

carro.siga() # "carro" é objeto, "siga()" é o método.

if bloco.esquerda():
	bloco True
else:
	bloco False


tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
	print('carro novo')
else:
	print('carro velho')
print('--FIM--')

# Condição simplificada

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho') # Parece, mas NÃO é um operador ternário.
print('--FIM--')

# Prática

nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
	print('Que nome lindo você tem!')
else:
	print('Seu nome é tão normal!')
print('Bom dia, {}!' .format(nome))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

m = (n1 + n2) / 2

if m >= 6.0:
	print('Sua média foi boa! PARABÉNS!')
else:
	print('Sua média foi ruim! ESTUDE MAIS!')
#
