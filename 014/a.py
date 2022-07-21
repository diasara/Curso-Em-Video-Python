# Estrutura de repetição WHILE

enquanto não maçã
	passo
pega

while not maçã: # Terreno plano sem obstáculos.
	passo
pega

enquanto não maçã
	se chão
		passo
	se buraco
		pula
	se moeda
		pega
pega

while not maçã: # Terreno plano com obstáculos e moedas.
	if chão:
		passo
	if buraco:
		pula
	if moeda:
		pega
pega




for c in range(1,10):
	print(c)
print('FIM')

# É a mesma coisa que

c = 1
while c < 10:
	print(c)
	c += 1
print('FIM')

n = 1
while n != 0:
	n = int(input('Digite um valor: '))
print('FIM')