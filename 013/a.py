# Estrutura de repetição FOR

laço c no intervalo(1,10):
	passo
pega

for c in range(1,10): # Terreno retilínio sem obstáculos.
	passo
pega


for c in range(0,3): # Terreno retilínio com obstáculos consecutivos.
	passo
	pula
passo
pega	

for c in range(0,3): # Terreno retilínio com obstáculos consecutivos e moedas.
	if coin:
		pega
	passo
	pula
passo
pega

for c in range(inicialização, condicional, identação) # identação = incremento ou decremento.
for c in range(6, 0, -1) # A cada rodada, soma-se '-1'
# De padrão, a identação é um incremento.

n = int(input('Digite um número: '))
for c in range(0, n+1):
	print(c)
print('FIM')

i = int(input('Início: '))	
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
	print(c)
print('FIM')	

# É possível colocar inputs dentro de um FOR

s = 0
for c in range(0, 4)
	n = int(input('Digite um número: '))
	s = s + n # Ou s += n
print('O somatório é {}.' .format(s))